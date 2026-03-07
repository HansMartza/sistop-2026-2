import os
import signal
import sys
import shlex

# Manejo de procesos hijos terminados
def sigchld_handler(signum, frame):
    try:
        while True:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
            print(f"[Proceso {pid} terminado]")
    except ChildProcessError:
        pass


# Ignorar Ctrl+C en el shell
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Manejar SIGCHLD solo si existe en el sistema
if hasattr(signal, "SIGCHLD"):
    signal.signal(signal.SIGCHLD, sigchld_handler)


while True:
    try:

        comando = input("minishell> ")

        if comando.strip() == "exit":
            print("Saliendo del minishell...")
            sys.exit(0)

        args = shlex.split(comando)

        if not args:
            continue

        pid = os.fork()

        if pid == 0:
            # proceso hijo
            signal.signal(signal.SIGINT, signal.SIG_DFL)

            try:
                os.execvp(args[0], args)
            except FileNotFoundError:
                print("Comando no encontrado")

            sys.exit(1)

        else:
            # proceso padre
            os.waitpid(pid, 0)

    except EOFError:
        print()
        break


