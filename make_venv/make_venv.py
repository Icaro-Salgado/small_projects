#!/usr/bin/python3.9
import sys
import os

def main():

    if len(sys.argv) > 3:
        return 'Argumentos inválidos'
    
    python_version = sys.argv[2] if len(sys.argv) == 3 else '3.8'
    name = sys.argv[1]
    
    os.system(f'python{python_version} -m venv ~/.venvs/{name}')



if __name__ == '__main__':
    main()
