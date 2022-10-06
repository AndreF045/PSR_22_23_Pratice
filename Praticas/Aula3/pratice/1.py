#!/usr/bin/env python3

from colorama import Fore, Style, Back

class animal():
  def __init__(self,name, age, clube):
    self.name = name
    self.age = age
    self.clube = clube
    
  def parabens(self):
    print("parabens " + self.name)

  
  def __str__(self):
    text = "ola eu sou " + Fore.YELLOW + self.name + Style.RESET_ALL + " e sou do " + Fore.BLUE + self.clube

   
  
    return text



def main():
  
  p1 = animal(name = "ze", age =15, clube = "porto")
  print(p1)
  p1.parabens()

















if __name__ == "__main__":
  main()


