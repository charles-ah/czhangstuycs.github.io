#!/usr/bin/python
print "content-type: text/html\n"
import cgi,cgitb,random,sys,traceback,math
#cgitb.enable()

form=cgi.FieldStorage()
graphcode=open('graphcode.txt','r').read()
f=open('graphcode.txt','w')
equation = (form['equation'].value).split('^')
equation = '**'.join(equation)

def coord(equation):
    coordlist=[]
    i = -15
    while i <=15:
        x=i
        coordlist.append(x)
        try:
                   coordlist.append(eval(equation))
        except Exception as e:
            print e

 
        i += 0.1
    return coordlist
    
#print coord(equation)

print '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
  <title>Grapher</title>

  <!-- CSS  -->
  <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
</head>

<body bgcolor="#e8ebf5">
<center>
	<a href="EGraph.html" id="download-button" class="btn-large waves-effect waves-light teal">Add Graphs</a>
    <a href="clear.py" id="download-button" class="btn-large waves-effect waves-light teal">Clear Graphs</a>
    <svg height="1000" width="1400">
      <line x1="700" y1="100" x2="700" y2="700" style="stroke:rgb(255,0,0);stroke-width:1" />
      <line x1="0" y1="400" x2="1400" y2="400" style="stroke:rgb(255,0,0);stroke-width:1" />
'''
for i in range(0,1400,10):
    print  '''<line x1="'''+str(i)+'''" y1="395" x2="'''+str(i)+'''" y2="405" style="stroke:rgb(0,0,255);stroke-width:1" />
'''
for i in range(110,690,10):
    print  ''' <line x1="695" y1="'''+str(i)+'''" x2="705" y2="'''+str(i)+'''" style="stroke:rgb(0,0,225);stroke-width:1" />
'''
def graph(coordlist):
    svg=graphcode
    #svg='''  <path d="'''
    # svg += "M 700 400"
    rand1=str(random.randint(0,255))
    rand2=str(random.randint(0,255))
    rand3=str(random.randint(0,255))
   
    for i in range(0,len(coordlist)-3,2):
        svg+="<line x1= '"+str((10*coordlist[i]+700))+"' y1= '"+str((-10*coordlist[i+1]+400))+"' x2='"+str((10*coordlist[i+2]+700))+"' y2='"+str((-10*coordlist[i+3]+400))+"' style='stroke:rgb("+rand1+","+rand2+","+rand3+");stroke-width:' />"
    svg+=''' style="stroke:#660000; fill:none;" />'''
    
    f.write(svg)
    return svg

print graph(coord(equation))
print '''
    </svg>
</center>
</body>
</html>
'''
