from core.engine import AutoCompleteEngine

if __name__ == "__main__":
    engine = AutoCompleteEngine()
    engine.load_words("data/words.txt")

    while True:
        prefix = input("\n Enter search prefix (or 'exit'): ").strip().lower()
        if prefix == 'exit':
            break
        suggestions = engine.get_suggestions(prefix)
        print(f"Suggestions: {', '.join(suggestions) if suggestions else 'No matches found'}")
