# Flutter-Intl---arb-to-csv
Converter for Flutter developers which process all arb translation files to one csv file suitable for translation in Excel spreadsheets.
This document presents process of converting localization strings into formats suitable for translation **(csv/excel)**. This is applicable only when using https://plugins.jetbrains.com/plugin/13666-flutter-intl plugin.

## Converting to csv/excel format
- Use https://github.com/kovaccc/Flutter-Intl---arb-to-csv script to convert all .arb translation files to one csv where keys and values are separated with commas
- You will need to input absolute path to your application file and reference file where all strings are up-to-date which is in most cases **intl_en.arb** file
- No worries if you entered wrong one, this script will pass through all .arb files in **l10n** directory and pick up all missing keys and put it into csv
- You can find output csv in same directory **l10n**
- You can see result of running this script: 

<img width="365" alt="image" src="https://user-images.githubusercontent.com/75457058/204285860-e74adb74-89c3-4551-bd7a-b1cf9a5b3d24.png">

<img width="748" alt="image" src="https://user-images.githubusercontent.com/75457058/204285982-e50c5cbd-9266-4636-9300-709727b6f296.png">

<img width="572" alt="image" src="https://user-images.githubusercontent.com/75457058/204286542-822dcbb6-5f53-47b3-893a-5ee0ce33a5cd.png">

- You can also load output csv file in excel sheet: 

<img width="1140" alt="image" src="https://user-images.githubusercontent.com/75457058/204287633-92d30843-ad04-4ff6-b9bc-abbda3913086.png">

<img width="583" alt="image" src="https://user-images.githubusercontent.com/75457058/204288018-da6cd1fd-81dd-415e-9d1b-a4bddfbe20b7.png">

<img width="583" alt="image" src="https://user-images.githubusercontent.com/75457058/204288190-6e94e5a8-2e44-40f1-9751-657ffc28e617.png">

<img width="583" alt="image" src="https://user-images.githubusercontent.com/75457058/204288299-bb8bf50d-7c78-4d57-813b-4b5ad11c0f70.png">

<img width="1391" alt="image" src="https://user-images.githubusercontent.com/75457058/204288611-c5204926-a909-4158-b0fd-99cbcd1d5b8a.png">


