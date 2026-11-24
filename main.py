from pathlib import Path


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        'My agent asked itself its own name twice, burned 4,600 tokens, and still answered "GPT-6".',
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
