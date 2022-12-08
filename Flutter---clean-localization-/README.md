# Flutter Localization 
This document presents process of converting localization strings from excel/csv file into  **.arb files** required for use in the application. This is applicable only when using https://plugins.jetbrains.com/plugin/13666-flutter-intl plugin.

## Converting to .arb format
- Save excel as **.csv** file. Use UTF-8 type to get right representation of signed letters from another languages

<img width="1508" alt="image" src="https://user-images.githubusercontent.com/75457058/204299969-7b96c445-0f96-4cde-9aaa-d2513f956cd3.png">

<img width="698" alt="image" src="https://user-images.githubusercontent.com/75457058/206386721-e5dd2075-af05-4f12-a3a6-647d5ba2f453.png">

- use [arb generator](https://pub.dev/packages/arb_generator) to generate updated .arb files in localization directory of your application. Delimiter parameter is optional and it defaults to ",". You will maybe need to comment some of your dependencies to be able to use this package

```sh
arb_generator:
  input_filepath: "translations.csv"
  output_filepath: "lib/l10n"
  filename_prepend: "intl_"
  csv_settings:
    delimiter: ";"
    base_index: 1
```

- you will get output .arb files looking like this

<img width="867" alt="image" src="https://user-images.githubusercontent.com/75457058/206392711-77a6d971-4ecf-4c29-953f-3afcbc385e0f.png">

- Run [this script](https://github.com/kovaccc/Flutter---clean-localization-) to remove unused descriptions and other unused strings from your .arb files by adding it to your application directory (clean_intl.py). You will maybe need to adjust root_folders variable in the script depending on your project structure

<img width="290" alt="image" src="https://user-images.githubusercontent.com/75457058/206390556-20998396-003e-44a0-8e40-967711d43a8a.png"> 

- You will get cleaned .arb files

<img width="867" alt="image" src="https://user-images.githubusercontent.com/75457058/206394093-efc3ca77-70bd-48c5-81ff-1b21e406eb1f.png">
