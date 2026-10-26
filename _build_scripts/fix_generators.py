import re

for fname in ['populate_python_days_1_2.py', 'populate_python_days_3_4_5.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace literal \n in print("\n with \\n
    # in source code: 'print("\n' -> 'print("\\n'
    fixed = re.sub(r'print\("(\\n|\n)', r'print("\\\\n', content)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print("Fixed generator:", fname)
