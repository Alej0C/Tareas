@echo off
title Memoria USB
echo Bienvenido al programa
Set /p input=Ingrese el nombre de la unidad de su Memoria USB:
echo Pulse cualquier tecla para continuar..!
pause>nul
format /q %input%:
echo Tu Memoria USB se ha formateado correctamente.
echo ¡Presione cualquier tecla para salir del programa!
pause>nul
exit