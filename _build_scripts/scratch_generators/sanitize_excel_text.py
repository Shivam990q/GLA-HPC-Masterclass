import re

def clean_for_excel(text):
    if not isinstance(text, str):
        return text
    # Replace markdown backticks with single quotes: `cmd` -> 'cmd'
    cleaned = re.sub(r'`([^`]+)`', r"'\1'", text)
    # Remove any stray backtick characters
    cleaned = cleaned.replace('`', '')
    # Replace LaTeX math symbols with clean Unicode
    cleaned = cleaned.replace(r'\times', '×').replace(r'\cdot', '·')
    cleaned = cleaned.replace(r'\le', '≤').replace(r'\ge', '≥')
    cleaned = cleaned.replace(r'\approx', '≈')
    # Remove math dollar signs if any e.g. $S(N)$ -> S(N)
    cleaned = re.sub(r'\$([A-Za-z0-9_\(\)\+\-\*\/\s\=]+)\$', r'\1', cleaned)
    return cleaned

test_cases = [
    "Which command outputs absolute path? `pwd`",
    "What does `chmod 750` do on `/scratch`?",
    "Formula $S(N) = s + p \\times N$",
    "Variable `$?` represents exit code",
    "`set -e` with `set -o pipefail`"
]

for tc in test_cases:
    print(f"RAW:   {tc}")
    print(f"CLEAN: {clean_for_excel(tc)}\n")
