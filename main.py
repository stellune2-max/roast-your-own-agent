from pathlib import Path


ROAST = 'My agent asked itself its own name twice, burned 4,600 tokens, and still answered "GPT-6".'


def main():
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip() or ROAST.splitlines() != [ROAST]:
        raise ValueError("The roast must be one non-blank line of 1 to 200 characters.")

    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
