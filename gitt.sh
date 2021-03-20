#!/bin/bash
git add *
VAR="$1"
if [ -n "$VAR" ]
then
git commit -m "$VAR"
else
git commit -m "Bugfix"
fi
git push origin main

