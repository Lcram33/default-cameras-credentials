import os
import sys


def remove_duplicate_and_sort(list_input):
    list_output = list(set(list_input))
    
    if '' in list_output:
        list_output.remove('')

    list_output.sort()

    return list_output

args = sys.argv[1:]
if len(args) != 1:
    sys.exit()

path = (os.getcwd() + args[0][1:len(args[0])]) if args[0].startswith('.') else args[0]

if not os.path.exists(path) or os.path.isdir(path):
    print("Invalid path (does not exists or not a file) !")
    sys.exit()

print("Backuping to " + path + ".old")
os.rename(path, path + '.old')

print("Modifying list...")
with open(path + '.old', 'r') as f:
    data = f.read().split('\n')

with open(path, 'w') as f:
    f.write('\n'.join(remove_duplicate_and_sort(data)))

print("Done !")
