"""Write one dad joke to /output/entry.txt."""

from pathlib import Path


JOKE = "I told the ocean I was feeling down. It said, 'Don't worry, I'll tide you over.'"


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if len(JOKE) > 200:
        raise ValueError("JOKE must be at most 200 characters")

    output_path.write_text(JOKE)


if __name__ == "__main__":
    main()
