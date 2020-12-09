#!/usr/bin/env python3
# Purpose: Say hello
print('Hello, World!')

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print(f'Hello, {args.name}!')