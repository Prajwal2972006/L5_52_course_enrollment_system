"""Course enrollment system with safer input handling and clearer structure."""

from __future__ import annotations

import hashlib
import secrets
from pathlib import Path
from typing import Any

COURSES: dict[str, dict[str, Any]] = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

TUITION_ACCOUNTING = {"total": 0.0}


def enroll_student(
    course_id: str,
    student_name: str,
    credits_registered: int = 3,
    audit_trail: list[str] | None = None,
) -> bool:
    """Enroll a student if the course exists and has seats available."""
    if audit_trail is None:
        audit_trail = []

    course = COURSES.get(course_id)

    if course is None or course["is_closed"] or course["seats"] <= 0:
        return False

    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")

    if (
        isinstance(credits_registered, bool)
        or not isinstance(credits_registered, int)
        or credits_registered <= 0
    ):
        raise ValueError("Credits registered must be a positive integer.")

    course["seats"] -= 1
    course["is_closed"] = course["seats"] == 0
    TUITION_ACCOUNTING["total"] += course["fee"]

    audit_trail.append(
        f"Enrolled student {student_name} in course {course_id} "
        f"with {credits_registered} credits successfully."
    )
    return True


def drop_course(course_id: str) -> bool:
    """Restore one seat for a valid course and mark it as open."""
    course = COURSES.get(course_id)

    if course is None:
        return False

    course["seats"] += 1
    course["is_closed"] = False
    return True


def check_course_status(course_id: str) -> bool:
    """Return True only when the course exists and is open with seats."""
    course = COURSES.get(course_id)

    return (
        course is not None
        and not course["is_closed"]
        and course["seats"] > 0
    )


def calculate_scholarship_tuition(
    course_id: str,
    discount_rate: float,
) -> float:
    """Calculate tuition after a discount rate between 0 and 1."""
    course = COURSES.get(course_id)

    if course is None:
        raise ValueError(f"Unknown course: {course_id}")

    if (
        isinstance(discount_rate, bool)
        or not isinstance(discount_rate, (int, float))
        or not 0.0 <= discount_rate <= 1.0
    ):
        raise ValueError("Discount rate must be between 0 and 1.")

    return round(course["fee"] * (1.0 - discount_rate), 2)


def generate_student_hash(roll_no: str) -> str:
    """Return a SHA-256 digest for a student roll number."""
    if not roll_no.strip():
        raise ValueError("Roll number cannot be empty.")

    return hashlib.sha256(roll_no.encode("utf-8")).hexdigest()


def generate_enrollment_otp() -> int:
    """Generate a four-digit enrollment OTP using a secure random source."""
    return secrets.randbelow(9000) + 1000


def export_course_roster(filename: str = "course_roster.txt") -> None:
    """Export the current course catalog to a text file."""
    output_path = Path(filename)
    output_path.write_text(
        f"{COURSES}\n",
        encoding="utf-8",
    )
    print(f"Course roster exported to: {output_path}")


def get_open_courses_summary(
    course_catalog: dict[str, dict[str, Any]],
) -> int:
    """Count courses that are open and have at least one seat."""
    return sum(
        1
        for details in course_catalog.values()
        if not details["is_closed"] and details["seats"] > 0
    )


def main() -> None:
    """Run a small demonstration of the course enrollment features."""
    audit_trail: list[str] = []

    enrolled = enroll_student("CS101", "Kritika", 4, audit_trail)
    print("Enrollment successful:", enrolled)
    print("Audit trail:", audit_trail)

    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))
    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 0.25),
    )
    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()

    print("Open courses:", get_open_courses_summary(COURSES))
    print("Total Tuition:", TUITION_ACCOUNTING["total"])
    print("Registrar token: not configured in this demo.")


if __name__ == "__main__":
    main()
    