import re

seq1 = "ATGsA"
seq2 = "ATGAAAA"

busca = re.match(seq1,seq2)

if busca:
		print ("sequencia identicas")
		print busca.group()
else: 
	print ("sequencias diferentes")