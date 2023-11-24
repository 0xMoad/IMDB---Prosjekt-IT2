print(r"""
      
         __  __  ___    _    ____    ____  _     ___ _  ___  _______ ____  
        |  \/  |/ _ \  / \  |  _ \  / ___|| |   |_ _| |/ / |/ / ____|  _ \ 
        | |\/| | | | |/ _ \ | | | | \___ \| |    | || ' /| ' /|  _| | |_) |
        | |  | | |_| / ___ \| |_| |  ___) | |___ | || . \| . \| |___|  _ < 
        |_|__|_|\___/_/   \_\____/__|____/|_____|___|_|\_\_|\_\_____|_| \_\
        | __ )  / \  | |   | |   | ____|  _ \                              
        |  _ \ / _ \ | |   | |   |  _| | |_) |                             
        | |_) / ___ \| |___| |___| |___|  _ <                              
        |____/_/   \_\_____|_____|_____|_| \_\                             
      
      """)
      

def display_menu():
    print("Velkommen til vår IT oppgave!:")
    print("1. Spill Higher or Lower!")
    print("2. Se data om tidenes beste filmer!")
    print("3. Avslutt")

def higher_or_lower():
    print("Spillet starter...")

def film_data():
    print("Laster data...")


# Main game loop
while True:
    display_menu()

    valg = input("Skriv inn ditt valg (1-4): ")

    if valg == '1':
        higher_or_lower()
    elif valg == '2':
        film_data()
    elif valg == '3':
        print("Avslutter...")
        break
    else:
        print("ugyldig svar")
