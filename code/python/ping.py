#!/usr/bin/env python3

print(os.popen("ping -c 1 8.8.8.8").readlines())

import subprocess

print(subprocess.getoutput("ping -c 1 8.8.8.8"))
