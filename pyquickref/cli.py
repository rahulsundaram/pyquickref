"""Command-line interface for PyQuickRef."""

import argparse
import difflib
import sys

import pyquickref.examples  # noqa: F401  — trigger @example registration
from pyquickref import __version__
from pyquickref.core import list_examples, run_examples, run_lesson
from pyquickref.registry import get_example, get_lesson, get_lessons, get_registry

EPILOG = """\
examples:
  pyquickref                          run all lessons in order
  pyquickref list_comprehend          run one example
  pyquickref factory_pattern asyncio_example
  pyquickref --lesson 1               run lesson 1 only
  pyquickref --list                   show the lesson plan
"""


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="pyquickref",
        description="Python quick reference — runnable examples, lesson by lesson.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "examples",
        nargs="*",
        metavar="EXAMPLE",
        help="examples to run (omit to run all lessons)",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        dest="list_examples",
        help="show the lesson plan and all examples",
    )
    parser.add_argument(
        "-n",
        "--lesson",
        type=int,
        metavar="N",
        help="run a specific lesson (e.g. --lesson 1)",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for the pyquickref CLI."""
    args = parse_args()

    if args.list_examples:
        list_examples()
        return

    if args.lesson is not None:
        lesson = get_lesson(args.lesson)
        if lesson is not None:
            run_lesson(lesson, "data")
        else:
            nums = [str(ls.number) for ls in get_lessons()]
            print(f"Unknown lesson: {args.lesson}")
            print(f"Available: {', '.join(nums)}")
            sys.exit(1)
        return

    functions_to_run: list[str] | None = None

    if args.examples:
        all_names = list(get_registry())
        bad = [name for name in args.examples if get_example(name) is None]
        if bad:
            for name in bad:
                print(f"Unknown example: '{name}'")
                close = difflib.get_close_matches(name, all_names, n=3, cutoff=0.4)
                if close:
                    print("\n  Did you mean one of these?")
                    for c in close:
                        print(f"    {c}")
                    print()
            sys.exit(1)
        functions_to_run = args.examples

    run_examples(functions_to_run)


if __name__ == "__main__":
    main()
