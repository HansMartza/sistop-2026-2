#Autor: Martinez Sanchez Hans  Fecha: 21/Marzo/2026
import threading
import time
import random

# Semáforos
santaSem = threading.Semaphore(0)
reindeerSem = threading.Semaphore(0)
elfSem = threading.Semaphore(0)
elfTex = threading.Semaphore(1)

# Mutex
mutex = threading.Lock()

# Contadores
elfCount = 0
reindeerCount = 0

# Santa Claus
def santa():
    global elfCount, reindeerCount
    while True:
        santaSem.acquire()
        
        with mutex:
            if reindeerCount == 9:
                print(" Santa: Preparando el trineo!")
                for _ in range(9):
                    reindeerSem.release()
                reindeerCount = 0
            
            elif elfCount == 3:
                print(" Santa: Ayudando a los elfos!")
                for _ in range(3):
                    elfSem.release()

# Elfos
def elf(id):
    global elfCount
    while True:
        time.sleep(random.randint(1, 5))
        print(f" Elfo {id} tiene un problema")

        elfTex.acquire()

        with mutex:
            elfCount += 1
            if elfCount == 3:
                print(" 3 elfos despiertan a Santa")
                santaSem.release()
            else:
                elfTex.release()

        elfSem.acquire()

        with mutex:
            elfCount -= 1
            if elfCount == 0:
                elfTex.release()

        print(f" Elfo {id} vuelve a trabajar")

# Renos
def reindeer(id):
    global reindeerCount
    while True:
        time.sleep(random.randint(5, 10))
        print(f" Reno {id} regresó")

        with mutex:
            reindeerCount += 1
            if reindeerCount == 9:
                print(" Todos los renos llegaron, despiertan a Santa")
                santaSem.release()

        reindeerSem.acquire()
        print(f" Reno {id} enganchado al trineo")

# Crear hilos
threading.Thread(target=santa).start()

for i in range(9):
    threading.Thread(target=reindeer, args=(i,)).start()

for i in range(10):
    threading.Thread(target=elf, args=(i,)).start()
import time
import random

# Semáforos
santaSem = threading.Semaphore(0)
reindeerSem = threading.Semaphore(0)
elfSem = threading.Semaphore(0)
elfTex = threading.Semaphore(1)

# Mutex
mutex = threading.Lock()

# Contadores
elfCount = 0
reindeerCount = 0

# Santa Claus
def santa():
    global elfCount, reindeerCount
    while True:
        santaSem.acquire()
        
        with mutex:
            if reindeerCount == 9:
                print(" Santa: Preparando el trineo!")
                for _ in range(9):
                    reindeerSem.release()
                reindeerCount = 0
            
            elif elfCount == 3:
                print(" Santa: Ayudando a los elfos!")
                for _ in range(3):
                    elfSem.release()

# Elfos
def elf(id):
    global elfCount
    while True:
        time.sleep(random.randint(1, 5))
        print(f" Elfo {id} tiene un problema")

        elfTex.acquire()

        with mutex:
            elfCount += 1
            if elfCount == 3:
                print(" 3 elfos despiertan a Santa")
                santaSem.release()
            else:
                elfTex.release()

        elfSem.acquire()

        with mutex:
            elfCount -= 1
            if elfCount == 0:
                elfTex.release()

        print(f" Elfo {id} vuelve a trabajar")

# Renos
def reindeer(id):
    global reindeerCount
    while True:
        time.sleep(random.randint(5, 10))
        print(f" Reno {id} regresó")

        with mutex:
            reindeerCount += 1
            if reindeerCount == 9:
                print(" Todos los renos llegaron, despiertan a Santa")
                santaSem.release()

        reindeerSem.acquire()
        print(f" Reno {id} enganchado al trineo")

# Crear hilos
threading.Thread(target=santa).start()

for i in range(9):
    threading.Thread(target=reindeer, args=(i,)).start()

for i in range(10):
    threading.Thread(target=elf, args=(i,)).start()
