#!/usr/bin/python
print "content-type: text/html\n"
import cgi,cgitb,random,sys,traceback,math
cgitb.enable()

f = open('graphcode.txt', 'r+')
f.truncate()

#open('graphcode.txt', 'w').close()

print '''<head>
<meta http-equiv="refresh" content="0;URL=EGraph.html">
</head>'''
