import os
import re


folder_location = r'C:\Users\User\Desktop\MK\Source'
list_of_all_subfolders = []

for root, dirs, files in os.walk(folder_location):
    for dir in dirs:
        list_of_all_subfolders.append(dir)

# print(*list_of_all_subfolders, sep='\n')

# original
# pattern = r'(\d+)(\s*-\s*|\s*-|-\s*|-\s*)([A-Za-z]+)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)([A-Za-z\s]+(?=\S)[A-Za-z\s])(?:\s*-\s*|\s*-|\s*-|-\s*)?(?:\d)?'
# added revision as a group
pattern =   r'(\d+)(\s*-\s*|\s*-|-\s*|-\s*)([A-Za-z]+)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)(\d+)(\s*-\s*|\s*-|-\s*|-\s*)([A-Za-z\s]+(?=\S)[A-Za-z\s])(?:\s*-\s*|\s*-|\s*-|-\s*)?((\d)?)'

for subfolder in list_of_all_subfolders:
    match = re.search(pattern, subfolder)

    if match:
        date = match.group(1)
        number = match.group(3) + match.group(4) + '-' + match.group(6) + '-' + match.group(8)
        name = match.group(10)
        revision = 0
        try:
            revision = match.group(11)
        except IndexError:
            pass
        print(f'{date}, {number}, {name}, {revision}')
    else:
        print('No match')



