# Flutter version change

A simple CLI tool for changing and downloading Flutter versions.

## Getting started

Clone this repo to a desired location:
```
git clone https://github.com/DMesek/flutter_version_change.git
```

### Installing FVC

In order to access this tool from anywhere, add the fvc file to your path. Or simply run the following command in the flutter_version_change folder:
```
./fvc install
```

Now you can run the `fvc` command from anywhere.

### Configuring the Flutter version folder

Before you get started you can change the default folder where all the Flutter versions are going to be downloaded and from where the tool is going to list the availabe versions.

The default Flutter version folder is `${HOME}/flutter/versions`. In order to change it run:
```
fvc config --version-folder $PATH_TO_VERSION_FOLDER
```

## Supported commands

`fvc`: change active Flutter version.

`fvc download --channel {stable,dev,beta}`: lists availble versions for specified channel, downloads the selected version into Flutter version folder.

`fvc config --version-folder $PATH_TO_VERSION_FOLDER`: change the directory where the versions are downloaded.

`fvc help`: list the supported commands.