#CALCULATING AT CONTENT

#Write a program that will print out the AT content of this DNA sequence. Hint: you can use normal mathematical symbols like add (+), 
#subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python. 


#gett DNA from file dna.txt
dna_file = open("dna.txt", "r") #open file and dna file is now a file object from file class
dna_sequence = dna_file.read() #using read method from File class to read content of the file
dna_file.close()


#dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_seq_lenght = len(dna_sequence) #lenght of the sequence
countT = dna_sequence.count("T") #counts how many T's present in sequence
countA = dna_sequence.count("A") #counts how many A's present in sequence
sum = countT + countA
division = sum / float(dna_seq_lenght) #divides the number of A's and T's by the total amount of nucleotides in sequence
multiply = division * 100
print("The AT content in the DNA sequence is " + str(multiply) + "%")

print(countA)