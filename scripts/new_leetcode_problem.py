#!/usr/bin/env python3
"""Scaffold one LeetCode problem folder for the Protein Programmer workflow."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "python-leetcode"


@dataclass(frozen=True)
class ReviewSchedule:
    created_at: date

    @property
    def r1(self) -> date:
        return self.created_at

    @property
    def r2(self) -> date:
        return self.created_at + timedelta(days=1)

    @property
    def r3(self) -> date:
        return self.created_at + timedelta(days=4)

    @property
    def r4(self) -> date:
        return self.created_at + timedelta(days=11)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a LeetCode problem folder with solution, notes, and repetition files."
    )
    parser.add_argument("problem_id", help="LeetCode problem ID, e.g. 704")
    parser.add_argument("title", help='Problem title, e.g. "Binary Search"')
    parser.add_argument(
        "--pattern",
        default="",
        help='Primary pattern, e.g. "Binary Search"',
    )
    parser.add_argument(
        "--difficulty",
        default="",
        help='Difficulty label, e.g. "Easy"',
    )
    parser.add_argument(
        "--stage",
        default="New",
        choices=["New", "Review", "Stable", "Mastered"],
        help="Lifecycle stage for this problem folder.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Directory where the problem folder will be created.",
    )
    return parser.parse_args()


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled-problem"


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def solution_template(problem_id: str, title: str) -> str:
    return f'''"""LeetCode {problem_id}: {title}."""


class Solution:
    def solve(self, *args, **kwargs):
        raise NotImplementedError(
            "Replace this placeholder with the accepted LeetCode method signature."
        )
'''


def repetition_template(problem_id: str, title: str, label: str) -> str:
    return f'''"""Repetition {label} for LeetCode {problem_id}: {title}."""


class Solution:
    def solve(self, *args, **kwargs):
        raise NotImplementedError(
            "Rewrite the solution from memory during this repetition pass."
        )
'''


def notes_template(
    problem_id: str,
    title: str,
    slug: str,
    pattern: str,
    difficulty: str,
    stage: str,
    schedule: ReviewSchedule,
) -> str:
    repo_path = f"python-leetcode/{problem_id}-{slug}"
    return f"""# {problem_id}. {title}

- Difficulty: {difficulty or "TBD"}
- Pattern: {pattern or "TBD"}
- Stage: {stage}
- Repo Path: `{repo_path}`
- Created At: {schedule.created_at.isoformat()}

## Problem summary

- Tulis ulang soal ini dengan bahasamu sendiri.
- Catat input, output, constraint, dan contoh penting.

## Pattern

- Pattern utama:
- Kenapa pattern ini cocok:
- Pattern lain yang sempat kepikiran:

## Brute force idea

- Ide pertama yang paling natural:
- Kenapa terlalu lambat atau terlalu ribet:

## Final insight

- Insight yang membuka jalan ke solusi final:
- Invariant atau rule penting yang harus diingat:

## Mistakes made

- Bug pertama:
- Miskonsepsi utama:
- Hal yang ingin dihindari di repetisi berikutnya:

## Complexity

- Time:
- Space:

## Repetition log

| Date | Repetition | Time finished | Need hint? | Main bug or mistake | Confidence (1-5) | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| {schedule.created_at.isoformat()} | Attempt 0 |  |  |  |  | {schedule.r1.isoformat()} |
| {schedule.r1.isoformat()} | R1 |  |  |  |  | {schedule.r2.isoformat()} |
| {schedule.r2.isoformat()} | R2 |  |  |  |  | {schedule.r3.isoformat()} |
| {schedule.r3.isoformat()} | R3 |  |  |  |  | {schedule.r4.isoformat()} if masih goyah |

## Next review

- Current target: {schedule.r1.isoformat()}
- Rule:
  - R1 di hari yang sama
  - R2 +1 hari
  - R3 +3 sampai 5 hari
  - R4 +7 sampai 14 hari kalau masih goyah
"""


def main() -> int:
    args = parse_args()
    slug = slugify(args.title)
    schedule = ReviewSchedule(created_at=date.today())

    root = args.output_root.resolve()
    problem_dir = root / f"{args.problem_id}-{slug}"
    attempts_dir = problem_dir / "attempts"

    ensure_directory(attempts_dir)

    created_files = []
    skipped_files = []

    file_specs = {
        problem_dir / "solution.py": solution_template(args.problem_id, args.title),
        problem_dir / "notes.md": notes_template(
            args.problem_id,
            args.title,
            slug,
            args.pattern,
            args.difficulty,
            args.stage,
            schedule,
        ),
        attempts_dir / "r1.py": repetition_template(args.problem_id, args.title, "R1"),
        attempts_dir / "r2.py": repetition_template(args.problem_id, args.title, "R2"),
        attempts_dir / "r3.py": repetition_template(args.problem_id, args.title, "R3"),
    }

    for path, content in file_specs.items():
        if write_if_missing(path, content):
            created_files.append(path)
        else:
            skipped_files.append(path)

    print(f"Problem folder: {display_path(problem_dir)}")
    if created_files:
        print("Created:")
        for path in created_files:
            print(f"  - {display_path(path)}")
    if skipped_files:
        print("Skipped (already existed):")
        for path in skipped_files:
            print(f"  - {display_path(path)}")

    print("Next reviews:")
    print(f"  - R1: {schedule.r1.isoformat()}")
    print(f"  - R2: {schedule.r2.isoformat()}")
    print(f"  - R3: {schedule.r3.isoformat()}")
    print(f"  - R4: {schedule.r4.isoformat()} (optional)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
