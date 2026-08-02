from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
NOTES_DIR = BASE_DIR / "notes"
def get_relevant_notes(weak_topics):
    relevant_notes = ""
    for topic in weak_topics:
        filename = topic.strip().lower().replace(" ", "_") + ".txt"
        file_path = NOTES_DIR / filename
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            relevant_notes += f"\n\n===== {topic} NOTES =====\n"
            relevant_notes += content
        else:
            print(f"Note not found for: {topic}")
    return relevant_notes