# MiniShell - Sistemas Operativos

## Descripción
Este programa implementa un intérprete de comandos básico (mini shell) en Python. 
Permite ejecutar programas del sistema mediante la creación de procesos hijos usando `fork()` 
y la ejecución de comandos con `execvp()`.

El shell también maneja señales del sistema como `SIGINT` (Ctrl+C) y `SIGCHLD`.

## Características
- Muestra un prompt `minishell>`
- Lee comandos ingresados por el usuario
- Crea procesos hijos con `fork()`
- Ejecuta comandos usando `execvp()`
- Maneja `SIGINT` para evitar que el shell termine con Ctrl+C
- Maneja `SIGCHLD` para recolectar procesos hijos
- Incluye comando interno `exit` para terminar el shell

## Requisitos
- Sistema Unix/Linux
- Python 3

## Ejecución

Ejecutar el programa con:
python3 minishell.py
 
## Ejemplo de ejecución
minishell> ls
minishell> ps aux
minishell> echo Hola mundo
minishell> sleep 5
minishell> exit
Saliendo del minishell...

## Dificultades encontradas

Una dificultad fue que el sistema Windows no soporta `fork()`.  
La solución fue ejecutar el programa usando **WSL (Windows Subsystem for Linux)** para poder utilizar las funciones de Unix requeridas.

## Autor
Hans Martínez
