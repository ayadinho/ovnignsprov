def main():
   #hälsningsfras
   print("Beräknar differensen av jämna/udda tal")

   # Initiera variabler för att lagra summan av udda och jämna tal
   sum_odd = 0
   sum_even = 0

   # Loopa igenom de första 1000 udda talen 
   for i in range(1, 2000, 2):
       sum_odd += i

   # Loopa igenom de första 1000 jämna talen 
   for i in range(2, 2000, 2):
       sum_even += i

   # Beräkna differensen mellan summan av udda och jämna tal
   difference = sum_odd - sum_even

   # Skriv ut differensen
   print("Differensen mellan summan av udda och jämna tal är", difference)



main()