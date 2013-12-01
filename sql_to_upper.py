#!/usr/bin/python

import re
from sys import argv

def gather_keywords():
  keywords = []
  with open('keywords.txt', 'r') as inf:
    for word in inf:
      keywords.append(word.rstrip('\n').lower())
  return keywords

def exact_match(w, kw_list):
  for word in kw_list:
    if word == w:
      return True
  return False

def change_case(sql, kw_list):
  with open(sql, 'r') as inf, open(sql + '.NEW', 'w') as outf:
    for line in inf:
      orig_line = line
      words = re.findall(r'(\w+)', line.rstrip('\n'))
      for w in words:
        if exact_match(w, kw_list):
          orig_line = re.sub(r'\b' + w + r'\b', w.upper(), orig_line)
      outf.write(orig_line)

def main():
  if len(argv) < 2:
    print 'Must supply a SQL file to fix'
    exit()
  else:
    reserved = gather_keywords()
    for sqlf in argv[1:]:
      print 'Changing file {0} to {0}.NEW'.format(sqlf)
      change_case(sqlf, reserved)

if __name__ == '__main__':
  main()
