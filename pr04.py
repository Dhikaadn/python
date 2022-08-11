# struktur program
import os #contoh library built-in python
import math #contoh library built-in python
 
# fungsi dalam 1 file yang sama dengan entry point
# diletakkan sebelum entry point
def TesFunc():
    return "Hai"
 
def TesProc():
	print("Alo")
 
# entry point dengan prosedur main
def main():
    print("hello world!")
    print(TesFunc())
    TesProc()
 
# panggil entry point
if __name__ == '__main__': 
    main()

