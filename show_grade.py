"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "be4986a2e88d8f124a3abd828c5247c9"
GRADE_HASH = "ee9f13758ecc7d2eddb8082fd25122b2fbf9967fd5c00e7481e4aa0f003df403"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
