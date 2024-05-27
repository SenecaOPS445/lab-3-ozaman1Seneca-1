#!/usr/bin/env python3
# Author ID: ozaman1

import subprocess

process = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def free_space():
    readout = process.communicate()
    readableproc = readout[0].decode('utf-8').strip()
    return readableproc

print(free_space())