"""
Test that the syllable splitter works properly
"""

import collections
import pytest
from syllablizer import (
    preprocess,
    build_next_syllables,
    generate_sentence,
    generate_text,
)

test_syllablizer

for word in tests:

WORD_CASES = [
    ("passive",["pas","sive"])
    ("influential",["in","flu","en","tial"])
    ("provisions",["pro","vi","sions"])
    ("partners",["part","ners"])
    ("bluebell",["blue","bell"])
    ("rationale",["ra","tion","ale"])
    ("Coca-Cola",["co","ca","co","la"])
    ("account",["ac","count"])
    ("banana",["ba","na","na"])
    ("flakes",["flakes"])
    ("tiny",["ti","ny"])
    ("draft",["draft"])
    ("Africa",["af","ri","ca"])
    ("concrete",["con","crete"])
    ("described",["de","scribed"])
    ("recognition",["rec","og","nit","ion"])
    ("niche",["niche"])
    ("condominiums",["con","do","min","i","ums"])
    ("recorded",["rec","ord","ed"])
    ("September",["sep","tem","ber"])
    ("ceremony",["cer","e","mo","ny"])
    ("student",["stu","dent"])
    ("apple",["ap","ple"])
    
]

assert(syllablize(WORD_CASES[0]) == WORD_CASES[1])
