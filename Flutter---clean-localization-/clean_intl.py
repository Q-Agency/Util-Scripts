import json
import os


def check_if_key_exists(key_name, dart_files):
    pattern = re.compile(r'(S\s*\.\s*current\s*\.\s*' + key_name + '|S\s*\.\s*of\(context\)\s*\.\s*' + key_name + ')[\s.,():;\]\}]')
    for file in dart_files:
        with open(file, 'r') as f:
            if pattern.search(f.read()):
                return True
    return False


def find_localization_map_by_intl_file_name(localization_maps, file_name):
    for local_map in localization_maps:
        for key_name, value in local_map.items():
            if "locale" in key_name and value in file_name:
                return local_map


def get_searched_dart_files(root_folders):
    dart_files = []
    for folder in root_folders:
        for root, _, files in os.walk(folder):
            for name in files:
                if name.endswith(".dart"):
                    file_name = root + "/" + name
                    dart_files.append(file_name)
    return dart_files


root_folders_input = input(
    "Enter folders that need to be checked delimited with space (e.g. lib/features lib/common): ")

# if you entered wrong directory names scrypt will finish
dart_files = get_searched_dart_files(root_folders_input.split())
if len(dart_files) == 0:
    print("There is no valid input folder for strings to be checked, please rerun scrypt with valid app folders")
    exit()

# all files in lib/l10n/ directory
l10n_file_names = next(os.walk("lib/l10n/"), (None, None, []))[2]

# create all .arb paths
arb_paths = []
for file in l10n_file_names:
    if "arb" in file:
        arb_paths.append("lib/l10n/" + file)

# load arb files from app to maps
localization_maps = []
for file in arb_paths:
    arb_file = open(file, "r", encoding='utf-8-sig')
    localization_maps.append(json.load(arb_file))

# filter all localization maps so output contains only used strings
filtered_localization_maps = []
for localization_map in localization_maps:
    filtered_localization_map = {}
    for key_name, value in localization_map.items():
        if check_if_key_exists(key_name, dart_files) or "locale" in key_name:
            # Condition to not write duplicate keys
            if key_name not in filtered_localization_map:
                filtered_localization_map[key_name] = value
    filtered_localization_maps.append(filtered_localization_map)

# write back only filtered keys to all arb files, encoding because of ' and signed letters
for file in arb_paths:
    with open(file, "w", encoding='utf-8-sig') as outfile:
        print(find_localization_map_by_intl_file_name(filtered_localization_maps, file))
        json.dump(find_localization_map_by_intl_file_name(filtered_localization_maps, file), outfile, indent=2,
                  ensure_ascii=False)
