# exercise 1
# There are three (3) “r” letters in the word “strawberry”.

# exercise 2
# A limerick is a five-line poem with a very specific structure and rhyme scheme. Here’s the breakdown:

# Rhyme Scheme: AABBA (Lines 1, 2, and 5 rhyme; lines 3 and 4 rhyme)
# Rhythm: Generally, limericks have a bouncy, light rhythm.
# Content: They're often humorous, nonsensical, or a little bit silly.
# Here’s the typical structure:
#
# Line 1: Introduces a person and/or place.
# Lines 2 & 3: Develop the situation or create a humorous image.
# Lines 4 & 5: Provide a punchline or a surprising twist.
# Example:
#
# There once was a fellow named Lou, (A) Who loved to eat olives, it’s true. (A) He’d gobble them down, (B) All over the town, (B) A most olive-loving view! (A)

# exercise 3
import datetime
import pytz


def utc_now_str():
    """
    Returns the current date and time in UTC as a string.
    """
    now_utc = datetime.datetime.now(pytz.utc)
    return now_utc.strftime("%Y-%m-%d %H:%M:%S")


current_utc_time = utc_now_str()
print(f"Current UTC time: {current_utc_time}")

# exercise 4
numbers = (i for i in range(1, 6))
print(numbers)
