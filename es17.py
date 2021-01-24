n_c = {}
nazioni = ["Italia", "Spagna", "Portogallo", "Francia", "Egitto", "Libia"]
capitali = ["Roma", "Madrid", "Lisbona", "Parigi", "Il Cairo", "Tripoli"]

for n, c in zip(nazioni, capitali):
    n_c[c] = n

capitale = input("Scrivi la capitale di cui vuoi conoscere la nazione ")

if capitale not in n_c:
    print("Nel programma non è presente la nazione associata a tale capitale")
else:
    nazione = n_c[capitale]
    print(nazione, "è la nazione della capitale inserita")

