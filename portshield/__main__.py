import argparse
from .core import record_review
from .demo import run


def main():
    parser = argparse.ArgumentParser(description="PortShield AI synthetic local prototype")
    commands = parser.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo", help="Generate the synthetic assessment")
    demo.add_argument("--output", default="artifacts")
    review = commands.add_parser("review", help="Record human review of a generated report")
    review.add_argument("--report", required=True)
    review.add_argument("--reviewer", required=True)
    review.add_argument("--decision", choices=["acknowledge", "request_more_evidence"], required=True)
    review.add_argument("--reason", required=True)
    args = parser.parse_args()
    if args.command == "demo":
        print(f"Synthetic assessment: {run(args.output)}")
    else:
        record_review(args.report, args.reviewer, args.decision, args.reason)
        print("Demo review recorded. No operational action authorized.")


if __name__ == "__main__":
    main()
