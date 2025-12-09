#!/usr/bin/env python
"""mapper.py"""
import sys

# los datos se leen de la entrada estándar
for line in sys.stdin:
  # Eliminar espacios en blanco
  line = line.strip()
  # separar "palabras"
  words = line.split()
  # incrementar contadores
  for word in words:
    # escribir el reaultado a la salida estándar
    # esta salida será la entrada para el reducer.py
    # separado por tabulador, cada palabra cuenta 1
    print ('%s\t%s' % (word, 1))

