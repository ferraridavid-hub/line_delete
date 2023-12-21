#!/usr/bin/env python3

# Davìd Ferrari 21/12/23

# DISCUSSIONE:
# 
# Si leggono tutte le linee del file, si contano, e si genera un insieme casuale di indici univoci
# per rappresentare la posizione delle linee da eliminare, sulla base della percentuale indicata.
# Successivamente, si contano i caratteri contenuti nelle linee non rappresentate dai suddetti indici
# e si generano valori univoci per rappresentare i caratteri da eliminare
# (In questo caso il valore indica la posizione del carattere rispetto all'intero file).
# Infine, si scrivono solo le linee la cui posizione non è contenuta negli indici delle linee da eliminare,
# previa sostituzione degli eventuali caratteri da modificare contenuti in ciascuna di esse.
# Come errore, ho ritenuto sufficientemente esplicativo il messaggio stampato da traceback
#### 
# NB: ho deciso di escludere i simboli '\n' dalla sostituzione (in e out) per rendere più evidente la rimozione delle linee.
# 	  Nel caso più completo si potrebbe modificare la variabile SYMBOLS con string.printable e considerare l'intera lunghezza delle linee lette da file
#     senza escludere l'ultimo carattere di ognuna dal computo totale. 


import os
from glob import glob
import random as rand
import string
import traceback

SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " " + "\t" 

def delete_lines( directory, extensions='.*', lines_perc=5, char_perc=5):
    files = []
    for ext in extensions:
        files += [y for x in os.walk(directory) for y in glob(os.path.join(x[0], '*' + ext))]
            
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            total_lines = len(lines)
            lines_to_remove = rand.sample(range(total_lines), round(total_lines * lines_perc / 100))
            
			# Remaining characters 
            total_characters = sum(len(line) - line.count('\n') for i, line in enumerate(lines) if not i in lines_to_remove)
            chars_to_remove = rand.sample(range(total_characters), round(total_characters * char_perc / 100))
            chars_to_remove.sort()
            

        with open(file, "w") as f:
             # Chars of previous lines
             processed_chars = 0
             for i, line in enumerate(lines):
                  if i not in lines_to_remove:
                       while chars_to_remove and chars_to_remove[0] - processed_chars < len(line) - line.count('\n'):
                            line=line.replace(line[chars_to_remove[0] - processed_chars], rand.choice(SYMBOLS))
                            chars_to_remove.pop(0)
                       f.write(line) 
                       processed_chars += len(line) - line.count('\n')
                       
if __name__ == '__main__':
     TEST_PATH = '/home/david/coding/python/test_engim'
     try: 
         delete_lines(directory=TEST_PATH, lines_perc=50, extensions=[".engim"], char_perc=0)
     except:
          traceback.print_exc(limit=0)
