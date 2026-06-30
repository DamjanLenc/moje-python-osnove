# Seznam, kamor bomo shranjevali opravila
opravila = ["Kupi mleko", "Naredi nalogo za Python"]

while True:
    print("\n--- MOJA TO-DO APLIKACIJA ---")
    print("1. Pokaži opravila")
    print("2. Dodaj opravilo")
    print("3. Izhod")
    
    izbira = input("Izberi možnost (1-3): ")
    
    if izbira == "1":
        # Tukaj bomo izpisali opravila
        print("\nTvoja opravila:")
        for o in opravila:
            print(f"- {o}")
            
    elif izbira == "2":
        # Tukaj bomo dodali novo opravilo
        novo = input("Vnesi novo opravilo: ")
        opravila.append(novo)
        print(f"Opravilo '{novo}' je bilo dodano!")
        
    elif izbira == "3":
        print("Hvala za uporabo! Se vidimo.")
        break # Prekine zanko in zapre program
        
    else:
        print("Napačna izbira, poskusi znova.")