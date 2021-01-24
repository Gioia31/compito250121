
nazioni = ["Italia", "Spagna", "Portogallo", "Francia", "Egitto", "Libia"]
capitali = ["Roma", "Madrid", "Lisbona", "Parigi", "Il Cairo", "Tripoli"]

def main():
    richiesto = str(input("Inserisci la nazione di cui vuoi sapere la capitale "))

    if richiesto in nazioni:
        nazione = nazioni.index(richiesto.capitalize())
        capitale = capitali[nazione]
        print("La capitale della nazione ", richiesto, "è ", capitale)
    
    else: 
        print("La capitale di questa nazione non è presente nel programma")
main()
