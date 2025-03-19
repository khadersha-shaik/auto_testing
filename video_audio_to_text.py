import os
import whisper
import openai
import subprocess

openai.api_key = "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"  # Replace with your OpenAI API Key

def extract_audio(video_path, audio_path="audio.wav"):
    """Extracts audio from a video file using FFmpeg."""
    command = f'ffmpeg -i "{video_path}" -vn -acodec pcm_s16le -ar 16000 -ac 1 "{audio_path}"'
    subprocess.run(command, shell=True)

def transcribe_audio(audio_path):
    """Converts audio to text using Whisper AI."""
    model = whisper.load_model("large")
    result = model.transcribe(audio_path)
    return result["text"]

def refine_text_with_gpt4(text):
    """Enhances transcription using GPT-4 AI."""
    prompt = f"Improve this AI-generated transcription for clarity and formatting:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def convert_media_to_text(file_path):
    """Detects if input is video or audio, then transcribes it."""
    if file_path.endswith((".mp4", ".mkv", ".avi", ".mov")):
        extract_audio(file_path)
        file_path = "audio.wav"

    if file_path.endswith((".wav", ".mp3", ".aac", ".flac")):
        raw_text = transcribe_audio(file_path)
        refined_text = refine_text_with_gpt4(raw_text)
        with open("final_transcript.txt", "w") as f:
            f.write(refined_text)
        print("Final Transcription:", refined_text)

# Run the AI-based transcription
convert_media_to_text("video.mp4")  # Replace with your file name
