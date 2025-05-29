#!/usr/bin/env python3
'''Lab 3 Inv 2 Part 2 - free disk space checker'''
# Author ID: rbhandari17@myseneca.ca

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
