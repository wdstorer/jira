# jira

## release_board.py
This script will automate the process of creating a version release and adding the resolved issues from a Jira board to the release. 

```
$ ./release_board.py -h
usage: release_board.py [-h] projectname [versionname] [releasedate]

positional arguments:
  projectname  Jira project name
  versionname  Version (Defaults to current date yyyy-mm-dd)
  releasedate  Date of release (Defaults to current date yyyy-mm-dd)

optional arguments:
  -h, --help   show this help message and exit```
