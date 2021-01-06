#!/usr/bin/python3.8
import os


def get_files_paths()
    """
    Read the paths to be send to backup
    """

  to_backup = []
   with open('folders_to_backup.txt') as folders_to_backup:
        for folder_path in folders_to_backup:
            path = folder_path.strip()
            to_backup.append(path)

    return to_backup


def main():
    """
    Coloca os arquivos na pasta de backup
    """    
    to_backup = get_files_paths()

    for file_path in to_backup:
        file_name = file_path.split('/')
        try:
            os.system(f'rm -r ~/.backups/{file_name}')
        except:
            print('Arquivo adicionado ao backup')
        
        os.system(f'cp {file_path} ~/.backups/{file_name}')



if __name__ == '__main__':
    main()
