import os

files = [
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-01_Python_Basics_Lists_Strings/live_demo/demo_basics_and_loops.py',
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-02_Collections_Functions_Functional/live_demo/demo_dictionaries.py',
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-02_Collections_Functions_Functional/live_demo/demo_tuples_and_sets.py',
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-03_Recursion_Modules_StdLib/live_demo/demo_numpy_basics.py',
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-03_Recursion_Modules_StdLib/live_demo/demo_recursion_visualizer.py',
    r'c:/Users/Rose/Videos/GLA Trainings/Python_BCSG0072_Master_Curriculum/Day-03_Recursion_Modules_StdLib/live_demo/demo_standard_library.py'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == 'print("':
            # Next line probably has \n" + ...
            if i + 1 < len(lines):
                next_line = lines[i+1]
                # combine them
                combined = 'print("\\n" + ' + next_line.lstrip()
                if combined.startswith('print("\\n" + "'):
                    # e.g. print("\n" + "="*60)
                    pass
                new_lines.append(combined)
                i += 2
                continue
        new_lines.append(line)
        i += 1
    with open(f, 'w', encoding='utf-8') as fp:
        fp.writelines(new_lines)
    print("Cleaned:", f)
