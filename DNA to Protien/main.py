

from Bio.Seq import Seq

Dna=input("enter DNA sequence ")
Dna =Seq(Dna)
Mrna=Dna.translate()
protein=Mrna.translate()
print(protein)



