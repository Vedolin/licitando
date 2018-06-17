from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def process(str_cmp, str_exact):
    return fuzz.ratio(str_exact, str_cmp)
