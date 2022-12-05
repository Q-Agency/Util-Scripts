#!/bin/bash

VERSION_BASE_URL=https://storage.googleapis.com/flutter_infra_release/releases/
VERSION_JSON_URL="${VERSION_BASE_URL}releases_macos.json"

VERSION_LABEL_FOLDER="/tmp/availableVersionLabels"
VERSION_FOLDER="/tmp/availableVersions"

curl $VERSION_JSON_URL | python json_parser.py $1 $VERSION_FOLDER $VERSION_LABEL_FOLDER
cat $VERSION_FOLDER

echo "Enter index of desired version: "
read inputVersion

selectedArchive=`cat ${VERSION_LABEL_FOLDER} | tail -n $inputVersion | head -n 1`
selectedVersion=`echo $selectedArchive | cut -d '_' -f3`
echo "Downloading ${selectedVersion}..."


rm $VERSION_FOLDER
rm $VERSION_LABEL_FOLDER

source fvc.config
DOWNLOADED_FILE_PATH="${flutterVersionFolder}/${selectedVersion}"
versionLabel=${selectedVersion::${#selectedVersion}-4}
echo $DOWNLOADED_FILE_PATH
curl "${VERSION_BASE_URL}${selectedArchive}" -o "$DOWNLOADED_FILE_PATH"

echo "Downloaded ${selectedVersion} into ${flutterVersionFolder}"
echo "Unzipping ${selectedVersion}. Please wait..."
`unzip ${DOWNLOADED_FILE_PATH} -d ${flutterVersionFolder} > /dev/null`
mv "${flutterVersionFolder}/flutter" "${flutterVersionFolder}/${versionLabel}"
rm "${DOWNLOADED_FILE_PATH}"
echo "Done."


