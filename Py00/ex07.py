# Creare una variabile ed assegnale un valore di tipo boolean. Stampa ad output il valore della variabile e il tipo della 
# variabile stessa con un andare a capo tra il valore e il tipo.
#
# Esempi di output:
# outuput 1 -->   True
#                 <class 'bool'>
# outuput 2 -->   False
#                 <class 'bool'> 
#
# Funzione ammesse: print(), type()


# Scrivi il tuo codice qui sotto ...

def print_bool(input_value):
    if (input_value == True):
        print("True")
        print(type(input_value))
    else:
        print("False")
        print(type(input_value))