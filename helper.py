from os.path import dirname, abspath
import os 

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

current_d = dirname(abspath(__file__))
Codewars = current_d + '\Codewars'
Codewars_README = os.path.normpath(Codewars + '\README.md')

open(Codewars_README, 'w').close()

for x in get_immediate_subdirectories(os.path.normpath(Codewars)):
    challenges = get_immediate_subdirectories(os.path.normpath(Codewars + '\\' + x))

    with open(Codewars_README, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("## " + str(x))
        f.write("\n")
        f.write("\n")
        f.close()

    for y in challenges:
        with open(Codewars_README, "a", encoding="utf-8") as f:
            f.write("- " + str(y))
            f.write("\n")
        f.close()

