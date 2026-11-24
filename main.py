from pathlib import Path


output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    "I told the ocean I was feeling down. It said, 'Don't worry, I'll tide you over.'"
)
