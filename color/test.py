#!/usr/bin/env python3

from termcolor import colored, cprint

print('Info: This is info level color.')
print(colored('Warn: ', 'yellow'), 'This is warning color.')
cprint('Error: This is error level color.', 'red')
