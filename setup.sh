#!/bin/bash
if [ $# -eq 1 ]; then
  if [ -f $1 ]; then
    cut -d ' ' -f 1,2 $1 | tr ' ' ',' > words.dat
  else
    echo "$1 is not found"
  fi
else
  echo "Usage: setup.sh <input dictionary name>"
  echo "dictionary format is assumed ATOK"
fi
