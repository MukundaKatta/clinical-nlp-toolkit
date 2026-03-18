"""CLI for clinical-nlp-toolkit."""
import sys, json, argparse
from .core import ClinicalNlpToolkit

def main():
    parser = argparse.ArgumentParser(description="NLP toolkit for clinical notes — entity extraction, coding, and summarization")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = ClinicalNlpToolkit()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"clinical-nlp-toolkit v0.1.0 — NLP toolkit for clinical notes — entity extraction, coding, and summarization")

if __name__ == "__main__":
    main()
