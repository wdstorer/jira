# jira

## release_board.py
This script will automate the process of creating a version release and set it as the Fix Version for resolved issues on the Jira board. 

* This is currently only designed to release boards for single projects. 

```
$ ./release_board.py -h
usage: release_board.py [-h] [--slackchannel SLACKCHANNEL]
                        projectname [versionname] [releasedate]

positional arguments:
  projectname           Jira project name
  versionname           Version (Defaults to current date yyyy-mm-dd)
  releasedate           Date of release (Defaults to current date yyyy-mm-dd)

optional arguments:
  -h, --help            show this help message and exit
  --slackchannel SLACKCHANNEL
                        specify the slack channel to notify about the board
                        release
