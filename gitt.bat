git add *
IF "%~1" == "" GOTO Def
git commit -m "%1"
GOTO Fin
:Def
git commit -m "Bugfix"
:Fin
git push origin master
