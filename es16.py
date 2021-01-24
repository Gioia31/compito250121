nazioni = ["Italia", "Spagna", "Portogallo", "Francia", "Egitto", "Libia"]
capitali = ["Roma", "Madrid", "Lisbona", "Parigi", "Il Cairo", "Tripoli"]

n_c = {}
for n, c in zip(nazioni, capitali):
    n_c[n] = c

nazione = input("Inserici la nazione di cui vuoi sapere la capitale ")

if nazione in n_c:
    print(n_c[nazione])
else:
    print("La capitale di questa nazione non è presente nel programma")