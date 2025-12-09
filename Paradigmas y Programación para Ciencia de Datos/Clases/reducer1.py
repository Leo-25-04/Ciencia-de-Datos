#!/usr/bin/env python
"""reducer.py"""
import sys

current_word = None
current_count = 0
word = None
for line in sys.stdin:
  line = line.strip()
  # separar los datos obtenidos de mapper.py
  word, count = line.split('\t', 1)
  # convertir la cuenta a entero
  try:
    count = int(count)
  except ValueError:
    # si no era un entero, se ignora
    continue
  # este IF funciona porque Hadoop ordena la salida del mapper
  # por la clave (word) antes de que la reciba el reducer
  if current_word == word:
    current_count += count
  else:
    if current_word:
      print ('%s\t%s' % (current_word, current_count))
    current_count = count
    current_word = word
# es necesario escribir la última palabra
if current_word == word:
  print ('%s\t%s' % (current_word, current_count))

