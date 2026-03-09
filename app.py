import os
from pathlib import Path
import gradio as gr
from faster_whisper import WhisperModel

# -----------------------
# Configuration
# -----------------------
DEFAULT_MODEL_SIZE = "base"   # tiny | base | small | medium | large-v3
DEVICE = os.getenv("FW_DEVICE", "cpu")   # "cpu" or "cuda"
COMPUTE_TYPE = os.getenv("FW_COMPUTE_TYPE", "int8")  # cpu: int8/int8_float16/float32 ; cuda: float16/int8_float16

# Lazy model cache to avoid re-loading on every call
_MODEL_CACHE = {}

def load_model(size: str):
    key = (size, DEVICE, COMPUTE_TYPE)
    if key not in _MODEL_CACHE:
        print(f"Loading model: size={size}, device={DEVICE}, compute_type={COMPUTE_TYPE}")
        _MODEL_CACHE[key] = WhisperModel(
            model_size_or_path=size,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
            cpu_threads=0  # let library choose
        )
    return _MODEL_CACHE[key]

def transcribe_file(
    audio_path,
    model_size,
    language,
    beam_size,
    vad_filter,
    temperature,
):
    """
    Gradio-friendly generator: yields partial text as segments are decoded.
    """
    print(f"Transcribe called with audio_path={audio_path}")
    if audio_path is None:
        yield "No audio received."
        return

    # Check if file exists
    if not os.path.isfile(audio_path):
        yield f"Audio file not found: {audio_path}"
        return

    try:
        model = load_model(model_size)
    except Exception as e:
        yield f"⚠️ Model loading error: {e}"
        return

    # If language is "auto", pass None so the model detects language
    lang = None if (language is None or language == "auto") else language

    try:
        print("Starting transcription...")
        segments, info = model.transcribe(
            audio_path,
            language=lang,
            beam_size=beam_size,
            vad_filter=vad_filter,
            temperature=temperature,
            best_of=beam_size,   # common heuristic
            condition_on_previous_text=True,
            word_timestamps=False
        )
        print("Transcription started, streaming segments...")
        transcript = []
        for seg in segments:
            transcript.append(seg.text.strip())
            print(f"Segment: {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
            yield " ".join(transcript)

        final_text = " ".join(transcript).strip()
        print("Transcription complete.")
        yield final_text if final_text else "(No speech detected.)"

    except Exception as e:
        print(f"Transcription error: {e}")
        yield f"⚠️ Transcription error: {e}"

def app_ui():
    with gr.Blocks(title="AI Speech-to-Text (Whisper, Offline)") as demo:
        gr.Markdown(
            """
            # 🎤 AI Speech-to-Text Assistant (Offline)
            **Whisper (faster-whisper)** + **Gradio**  
            - Works offline (no cloud)  
            - Punctuation & casing included  
            - Use your browser's mic (no PyAudio/PortAudio)
            """
        )

        with gr.Row():
            model_size = gr.Dropdown(
                choices=["tiny", "base", "small", "medium", "large-v3"],
                value=DEFAULT_MODEL_SIZE,
                label="Model size (accuracy vs speed)",
                info="Smaller = faster on CPU. 'base' or 'small' are good starting points."
            )
            language = gr.Dropdown(
                choices=["auto","en","hi","kn","ta","te","mr","bn","gu","ml","pa","ur"],
                value="auto",
                label="Language",
                info="Use 'auto' for automatic detection."
            )
        with gr.Row():
            beam_size = gr.Slider(1, 5, value=2, step=1, label="Beam size (quality vs speed)")
            vad_filter = gr.Checkbox(value=True, label="Noise/VAD filtering (Silero)")
            
        with gr.Row():
            temperature = gr.Slider(0.0, 1.0, value=0.0, step=0.1, label="Decoding temperature")

        gr.Markdown("### 🎙️ Record or upload audio")
        with gr.Row():
            mic = gr.Microphone(
                type="filepath",
                label="Record from microphone",
                interactive=True
            )
            file_up = gr.Audio(
                type="filepath",
                label="Or upload an audio file (wav/mp3/m4a/ogg)",
                sources=["upload"]
            )

        out_text = gr.Textbox(
            label="Transcript",
            lines=10,
            interactive=False
        )

        # Buttons
        transcribe_mic = gr.Button("Transcribe Microphone Recording")
        transcribe_file_btn = gr.Button("Transcribe Uploaded File")

        # Wire events: streaming output by setting streaming=True for generator
        transcribe_mic.click(
            fn=transcribe_file,
            inputs=[mic, model_size, language, beam_size, vad_filter, temperature],
            outputs=out_text
        )

        transcribe_file_btn.click(
            fn=transcribe_file,
            inputs=[file_up, model_size, language, beam_size, vad_filter, temperature],
            outputs=out_text
        )

        gr.Markdown(
            """
            **Tips**
            - On CPU, start with `tiny`/`base` for real-time feel.
            - For best accuracy, use `small`/`medium`.  
            - Keep your mic close and minimize background noise.
            """
        )

    return demo

if __name__ == "__main__":
    demo = app_ui()
    demo.launch(share=False)
