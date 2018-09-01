import os
import sys
import re

cli_args = sys.argv[1:]
path = '/home/osmc'
new_dir, dir_name = '', os.path.join(path, 'TV Shows')

if '-s' in cli_args:
    season = cli_args[cli_args.index('-s')+1]
else:
    season = 1

if '-n' in cli_args:
    new_dir = True

files = [f for f in os.listdir(os.path.join(path, 'Downloads')) if f.endswith('.mkv') and f.startswith('[HorribleSubs] ')]

for file in files:
    new_name = file.replace('[HorribleSubs] ', '')
    name_index = re.search(r" - [0-9]{2} \[", new_name).start()
    if new_dir:
        if new_name[0:name_index] not in os.listdir(os.path.join(path, 'TV Shows')):
            new_dir = os.path.join(path, 'TV Shows', new_name[0:name_index])
            os.mkdir(new_dir)
        if new_name[0:name_index] in os.listdir(os.path.join(path, 'TV Shows')):
            dir_name = os.path.join(path, 'TV Shows', new_name[0:name_index])
    #new_name = f'{new_name[:name_index]} - S0{season}E{new_name[name_index + 3:]}'
    new_name = '{} - S0{}E{}'.format(new_name[:name_index], season, new_name[name_index + 3:])
    os.rename(os.path.join(path, 'Downloads', file), os.path.join(dir_name, new_name))
    print(new_name)
