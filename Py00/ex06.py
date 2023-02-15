# Creare una variabile ed assegnale un valore di tipo int. Stampa ad output il valore della variabile e il tipo della 
# variabile stessa con un andare a capo tra il valore e il tipo.
#
# Esempi di output:
# outuput 1 -->   15
#                 <class 'int'> 
# outuput 2 -->   1
#                 <class 'int'>
# outuput 3 -->   1928
#                 <class 'int'>
#
# Funzione ammesse: print(), type()


# Scrivi il tuo codice qui sotto ...

def print_type_int(input_value):
    x = input_value
    print(str(x))
    print(type(x))