#!/usr/bin/env python3
"""
by Om to automate the scp work to get the jar files and 
check for there META-INF/MANIFEST.MF file. 
"""
import requests 
import os 
import re
from paramiko import SSHClient
from scp import SCPClient

file=open("/home/kali/Desktop/ofc/jarLibs.txt")
jarList=file.readlines()
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('<IP>',port=<22>/<2022>/<2024>,username='admin',password='admin') # change the hostname and port number

scp=SCPClient(ssh.get_transport())

for i in jarList:
                i = i.strip()
                scp.get(str(i))


scp.close()


