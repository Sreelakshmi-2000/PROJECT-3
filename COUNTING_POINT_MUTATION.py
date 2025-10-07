#PROBLEM 1
dna_sequence_01 = "GAGCCTACTAACGGGAT"
dna_sequence_02 = "CATCGTAATGACGGCCT"
difference_count = 0 
for i in range(len(dna_sequence_01)):
    if dna_sequence_01[i] != dna_sequence_02[i]:  
        difference_count += 1
print(difference_count)


        
 
