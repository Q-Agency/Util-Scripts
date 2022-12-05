import sys
import json

RELEASES = "releases"
CHANNEL = "channel"
VERSION = "version"
NUMBER_OF_VERSIONS = 20

channel = sys.argv[1]
version_file = sys.argv[2]
version_labels_file = sys.argv[3]
data = sys.stdin.read()

all_versions = json.loads(data)[RELEASES]
filtered_versions = [v for v in all_versions if v[CHANNEL] == channel]
filtered_version_names = map(lambda v: v[VERSION], filtered_versions)

f = open(version_file, "a")
f2 = open(version_labels_file, "a")
for i in range(NUMBER_OF_VERSIONS, -1, -1):
    f.write('[{index}] {version}\n'.format(index=i+1, version=filtered_version_names[i]))
    f2.write('{version}\n'.format(version=filtered_versions[i]['archive']))
