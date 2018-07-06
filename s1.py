from constants import *

class roman(object):

     def __init__(self,integere):

        self.integer=integere
        self.rom_str = ""
     def change(self):
        while self.integer >0:
            for item in num_list:
                if item > self.integer:
                    ind = num_list.index(item)-1
                    num_rom = num_list[ind]
                    str_rom = romannum [num_rom]
                    break

            self.integer=self.integer-10
            self.rom_str= self.rom_str+str_rom

     def check(self):
         if
        print( self.rom_str)




t = roman(5)
t.change()

