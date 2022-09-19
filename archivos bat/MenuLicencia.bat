@echo off
TITLE Bienvenid@ %USERNAME% a @lm_blog menu
MODE con:cols=80 lines=40

:inicio
SET var=0
cls
echo ------------------------------------------------------------------------------
echo  %DATE% ^| %TIME%
echo ------------------------------------------------------------------------------
echo  1    Opcion 1  
echo  2    Opcion 2  
echo  3    Opcion 3  
echo  4    Opcion 4  
echo ------------------------------------------------------------------------------
echo.

SET /p var= ^> Seleccione una opcion [1-4]:

if "%var%"=="0" goto inicio
if "%var%"=="1" goto op1
if "%var%"=="2" goto op2
if "%var%"=="3" goto op3
if "%var%"=="4" goto salir


::Mensaje de error, validación cuando se selecciona una opción fuera de rango
echo. El numero "%var%" no es una opcion valida, por favor intente de nuevo.
echo.
pause
echo.
goto:inicio

:op1
    echo.
    echo. Eliminacion de licencia
    echo.
        ::Aquí van las líneas de comando de tu opción
        slmgr -upk
    echo.
    pause
    goto:inicio

:op2
    echo.
    echo. Agregar licencia nueva
    echo.
        ::Aquí van las líneas de comando de tu opción
        set /p input=Digite la licencia:
        slmgr -ipk %input% 
    echo.
    pause
    goto:inicio

:op3
    echo.
    echo. Ver estado de activacion
    echo.
        ::Aquí van las líneas de comando de tu opción
        slmgr -Rilc
    echo.
    pause
    goto:inicio
  
:salir
    @cls&exit