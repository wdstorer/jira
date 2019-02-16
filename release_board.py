#!/usr/bin/python
import requests
import json
import sys
import datetime
import config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("projectname", type=str, help="Jira project name", default="huh")
parser.add_argument("versionname", nargs='?', type=str, help="Version (Defaults to current date yyyy-mm-dd)", default=datetime.datetime.today().strftime('%Y-%m-%d'))
parser.add_argument("releasedate", nargs='?', type=str, help="Date of release (Defaults to current date yyyy-mm-dd)", default=datetime.datetime.today().strftime('%Y-%m-%d'))
args = parser.parse_args()

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": "Basic " + config.authorizationkey
}

def httpgetrequest(url):
  response = requests.request(
    "GET",
    url,
    headers=headers
  )
  return response

def httppostrequest(url,payload):
  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers
  )
  return response

def httpputrequest(url,payload):
  response = requests.request(
    "PUT",
    url,
    data=payload,
    headers=headers
  )
  return response

def getprojectid(projectname):
  response = httpgetrequest(config.jiraurl + "/rest/api/3/project")
  for c in json.loads(response.text):
    if c['key'] == projectname:
        pid = c['id']
  if pid == '':
    print "pid not found for project name %s" % (projectname)
    sys.exit()       
  else:
    return pid

def createversion(projectname, versionname, releasedate):
  pid = getprojectid(projectname)
  payload = json.dumps( {
    "description": "Automated weekly board release",
    "name": versionname,
    "released": True,
    "releaseDate": releasedate, 
    "projectId": pid
  } )

  response = httppostrequest(config.jiraurl + "/rest/api/3/version",payload)

def releaseboard(projectname, versionname, releasedate):
  createversion(projectname, versionname, releasedate)
  
  # Get resolved tickets and set fixVersion
  response = httpgetrequest(config.jiraurl + "/rest/agile/latest/board/38/issue?jql=status=resolved%20and%20fixVersion%20is%20empty&fields=id")
  issues = []
  for c in json.loads(response.text)['issues']:
    issues.append(c['key'])

  for issue in issues:
    payload = json.dumps( {
      "update": {"fixVersions": [{"set": [ { "name": versionname} ] }]}
    } )
    response = httpputrequest(config.jiraurl + "/rest/api/3/issue/" + issue, payload)

project = args.projectname
versionname = args.versionname
releasedate = args.releasedate

releaseboard(project,versionname,releasedate)
