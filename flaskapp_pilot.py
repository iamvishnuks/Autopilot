import threading
import psutil
import os
import subprocess

def autopilot():
	flag=0
  path=#give the path of the app.py which you want to monitor in single quotes
	threading.Timer(5.0, autopilot).start()
	for pid in psutil.pids():
	   p=psutil.Process(pid)
	   if p.name()=="python" and path in p.cmdline():
	   	print "running", pid
	   	flag=1
	   	break
	if flag==0:
		subprocess.Popen(["nohup","python", path])
		flag=1

autopilot()
