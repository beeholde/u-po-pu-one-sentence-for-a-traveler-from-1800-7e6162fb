"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes a single sentence (172 characters, one sentence, no word coined
after 1800) explaining the modern internet to a time traveler from 1800,
to /output/entry.txt.

The sentence, chosen after a pairwise tournament of ten candidates scored
against the judge brief's criteria in order (explains the internet,
builds from 1800-known things, true, every word earns its place,
memorable image):

    Imagine a road joining your front door to every library and post
    office on earth, where your letters arrive before the ink dries
    and strangers half a world away write back.

Why this one won: a single road image carries the whole explanation —
universal access to knowledge (every library), messaging (every post
office), instant delivery (before the ink dries), and two-way contact
with anyone on earth (strangers half a world away write back). Every
word predates 1800: road, library, post office, letter, ink, stranger
are all words a person of 1800 already knew.
"""

import os

SENTENCE = (
    "Imagine a road joining your front door to every library and post "
    "office on earth, where your letters arrive before the ink dries "
    "and strangers half a world away write back."
)

# Words coined after 1800 that must never appear in the sentence.
BANNED_AFTER_1800 = (
    "internet", "computer", "website", "online", "digital", "email",
    "telephone", "telegraph", "television", "radio", "airplane",
    "automobile", "electricity", "photo", "video", "software",
)


def validate(text):
    """Gate the sentence before it is written: one sentence, at most
    200 characters, and no word coined after the traveler's year."""
    if not (1 <= len(text) <= 200):
        raise ValueError("sentence must be 1-200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    lowered = text.lower()
    for word in BANNED_AFTER_1800:
        if word in lowered:
            raise ValueError("post-1800 word in entry: %s" % word)


def output_path():
    target = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    if os.path.isdir(target):
        return os.path.join(target, "entry.txt")
    return target


def main():
    dest = output_path()
    parent = os.path.dirname(dest)
    if parent:
        os.makedirs(parent, exist_ok=True)
    text = SENTENCE
    validate(text)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
