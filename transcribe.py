import whisper
import sys
import json

def transcribe_media(file_path):
    model = whisper.load_model("small")
    result = model.transcribe(file_path)

    output_file = file_path + ".json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"Transcription saved at: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <media_file>")
    else:
        transcribe_media(sys.argv[1])