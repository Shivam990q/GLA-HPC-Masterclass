# demo_strings_mastery.py
# Complete live demonstration of ALL 18 String Methods + Special Inspection Methods

s = "  hello GLA University 2026!  "
print(f"Original String: '{s}'")

# 1-5: Case Transformations
print("1. upper()      :", s.upper())
print("2. lower()      :", s.lower())
print("3. title()      :", s.title())
print("4. capitalize() :", s.capitalize())
print("5. swapcase()   :", s.swapcase())

# 6-8: Trimming Whitespace
print("6. strip()      :", f"'{s.strip()}'")
print("7. lstrip()     :", f"'{s.lstrip()}'")
print("8. rstrip()     :", f"'{s.rstrip()}'")

# 9-11: Splitting, Joining & Replacing
clean_s = s.strip()
words = clean_s.split()
print("9. split()      :", words)
print("10. join()      :", "-".join(words))
print("11. replace()   :", clean_s.replace("2026", "2027"))

# 12-14: Search & Counting
print("12. find('GLA') :", clean_s.find("GLA"))
print("13. index('GLA'):", clean_s.index("GLA"))
print("14. count('e')  :", clean_s.count("e"))

# 15-18: Character Validation
print("15. startswith  :", clean_s.startswith("hello"))
print("16. endswith    :", clean_s.endswith("!"))
print("17. isdigit()   :", "2026".isdigit())
print("18. isalpha()   :", "GLA".isalpha())

# Other String Methods: center, zfill, isalnum, isspace, partition
print("center(40, '-') :", "PYTHON".center(40, "-"))
print("zfill(8)        :", "42".zfill(8))
print("isalnum()       :", "GLA2026".isalnum())
print("isspace()       :", "   ".isspace())
print("partition('GLA'):", clean_s.partition("GLA"))
