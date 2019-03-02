import csv
import sys
import argparse
import re
from collections import Counter
CATEGORIES = {
  "water": 0,
  "vehicle": 0,
  "signage": 0
}
parser = argparse.ArgumentParser(description='parse and slice a csv properly')
parser.add_argument('--file', action="store", required=True, help="csv file")
parser.add_argument('--fields', action="store", required=True, help="list of fields like 1,2,3,6")
parser.add_argument('--delimiter', action="store", required=False, default=",", help="list of fields")
parser.add_argument('--enclosure', action="store", required=False, default='"', help="list of fields")
parser.add_argument('--find', action="store", required=False, help="list of fields")
parser.add_argument('--replace', action="store", required=False, help="list of fields")
args = parser.parse_args()
cap_words = []

with open(args.file, 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=args.delimiter, quotechar=args.enclosure)
  for i, row in enumerate(reader):
    if i != 0:
      words = re.findall(r'\w+', row[int(args.fields)])
      cap_words += [word.upper() for word in words]
word_counts = Counter(cap_words)
for key,value in sorted(word_counts.items(), key=lambda x: x[1]):
  print(key)
  if re.match('water|irrigat|sprinkl', key, re.IGNORECASE):
    CATEGORIES['water'] += value
  elif re.match('sign|banner', key, re.IGNORECASE):
    CATEGORIES['signage'] += value
  elif re.match('vehicle|truck|auto| car ', key, re.IGNORECASE):
    CATEGORIES['vehicle'] += value

print(CATEGORIES)