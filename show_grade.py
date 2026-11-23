"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "99952f0cd87672afe3cc82fca65db464"
GRADE_HASH = "87506b78abf5054c724f2df8e437d2bfb7ed25ebad93413e59416507242bb7e3"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
