with open('scratch/generate_gla_day1_50_mcqs_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Balance Q02 to d:
text = text.replace(
    '"c": "4.096 TFLOPS",\n            "d": "8.192 TFLOPS"\n        },\n        "answer": "c",',
    '"c": "8.192 TFLOPS",\n            "d": "4.096 TFLOPS"\n        },\n        "answer": "d",'
)

# In Q10, 300 GB/s was 'c'. Let's swap with 'd'
text = text.replace(
    '"c": "300 GB/s",\n            "d": "600 GB/s"\n        },\n        "answer": "c",',
    '"c": "600 GB/s",\n            "d": "300 GB/s"\n        },\n        "answer": "d",'
)

# In Q18, swap b with d
text = text.replace(
    '"b": "Directory: 750 (\'rwxr-x---\'), File: 640 (\'rw-r-----\')",\n            "c": "Directory: 770 (\'rwxrwx---\'), File: 660 (\'rw-rw----\')",\n            "d": "Directory: 700 (\'rwx------\'), File: 600 (\'rw-------\')"\n        },\n        "answer": "b",',
    '"b": "Directory: 700 (\'rwx------\'), File: 600 (\'rw-------\')",\n            "c": "Directory: 770 (\'rwxrwx---\'), File: 660 (\'rw-rw----\')",\n            "d": "Directory: 750 (\'rwxr-x---\'), File: 640 (\'rw-r-----\')"\n        },\n        "answer": "d",'
)

# In Q24, 31 was 'b'. Let's swap with 'd'
text = text.replace(
    '"b": "31",\n            "c": "35",\n            "d": "42"\n        },\n        "answer": "b",',
    '"b": "42",\n            "c": "35",\n            "d": "31"\n        },\n        "answer": "d",'
)

# In Q46, '64 total ranks, 16 ranks per node' was 'c'. Let's swap with 'd'
text = text.replace(
    '"c": "64 total ranks, 16 ranks per node",\n            "d": "128 total ranks, 32 ranks per node"\n        },\n        "answer": "c",',
    '"c": "128 total ranks, 32 ranks per node",\n            "d": "64 total ranks, 16 ranks per node"\n        },\n        "answer": "d",'
)

with open('scratch/generate_gla_day1_50_mcqs_excel.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated script successfully!')
