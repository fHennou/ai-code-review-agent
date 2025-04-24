import argparse
from agent.analyzer import analyze_code

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--file", required=True, help="Path to the Python file to review")
    parser.add_argument("--mode", default="strict", choices=["strict", "mentor", "test_focus"], help="Prompt mode")
    parser.add_argument("--provider", default="openai", help="LLM provider (e.g., openai, ollama)")

    args = parser.parse_args()

    try:
        review = analyze_code(args.file, args.mode, args.provider)
        print("\n🧠 Review Output:\n")
        print(review)

        # Save to markdown
        with open("reviews/review_output.md", "w") as f:
            f.write("# Code Review\n\n")
            f.write(f"## File: {args.file}\n\n")
            f.write(review)

        print("\n Review saved to: reviews/review_output.md")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
