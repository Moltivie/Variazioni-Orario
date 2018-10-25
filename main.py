import requests, os, sys
from bs4 import BeautifulSoup as bs



class FauserCrawlr(object):

    def __init__(self):
        self._base_url = "http://www.fauser.gov.it/area-studenti/2-uncategorised/132-variazione-orario"
        # Request della pagina html
        self.req = requests.get(self._base_url)
        # Parser della pagina html in BeautifulSoup
        self.soup = bs(self.req.content, "html.parser")
        # Restituisce tutte le tabelle nella pagina
        self.tables = self.soup.findAll("table")


    def CrawlNote(self):
        
        # tables[0] rappresenza la tabella "Note XX-XX-XXXX"
        tr = self.tables[0].findAll("tr")

        # Lambda array dei docenti assenti del giorno XX-XX-XXXX
        array_note = [x.text for x in tr]

        # Stampa delle note
        if (len(array_note) == 1):
            print("Nessuna nota.")
            os.system("pause")

        # Rimozione del primo elemento rappresentante l'haeder della tabella corrente
        else: 
            array_note.pop(0)
            print([x for x in array_note])
            os.system("pause")


    def CrawlProfessori(self):

        # tables[1] rappresenza la tabella "Assenze Docenti del giorno XX-XX-XXXX"
        tr = self.tables[1].findAll("tr")

        # Lambda array dei docenti assenti del giorno XX-XX-XXXX
        array_assenze_docenti = [x.text for x in tr]

        # Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
        array_assenze_docenti.pop(0)
        array_assenze_docenti.pop(0)

        # Stampa dei docenti assenti

        if not array_assenze_docenti:
            print("Nessun docente assente.")
            os.system("pause")
        else:
            print(array_assenze_docenti)
            os.system("pause")


    def CrawlVariazioniGiorno(self):

        # tables[2] rappresenza la tabella "Variazioni del giorno XX-XX-XXXX"
        tr = self.tables[2].findAll("tr")

        # Lambda array delle variazioni dell'orario del giorno XX-XX-XXXX
        array_variazioni = [x.text for x in tr]

        # Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
        array_variazioni.pop(0)
        array_variazioni.pop(0)

        # Stampa delle variazioni

        if not array_variazioni:
            print("Nessuna variazione dell'orario.")
            os.system("pause")

        else:
            print(array_variazioni)
            os.system("pause")


    def CrawlVariazioniAule(self):

        # tables[3] rappresenza la tabella "Sostituzione Aule XX-XX-XXXX"
        tr = self.tables[3].findAll("tr")

        # Lambda array delle sostituzioni delle aule del giorno XX-XX-XXXX
        array_sostituzione_aule = [x.text for x in tr]

        # Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
        array_sostituzione_aule.pop(0)
        array_sostituzione_aule.pop(0)

        # Stampa delle sostituzioni aule

        if not array_sostituzione_aule:
            print("Nessuna variazione delle aule.")
            os.system("pause")

        else:
            print(array_sostituzione_aule)
            os.system("pause")


    def CrawlEntratePostUsciteAntic(self):

        # tables[4] rappresenza la tabella "Entrate posticipate / Uscite anticipate XX-XX-XXXX"
        tr = self.tables[4].findAll("tr")

        # Lambda array delle entrate posticipate - uscite anticipate del giorno XX-XX-XXXX
        entr_post_usc_antic = [x.text for x in tr]

        # Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
        entr_post_usc_antic.pop(0)
        entr_post_usc_antic.pop(0)

        # Stampa delle variazioni

        if not entr_post_usc_antic:
            print("Nessuna nota sulle entrate posticipate e/o uscite anticipate.")
            os.system("pause")

        else:
            print(x for x in entr_post_usc_antic)
            os.system("pause")


if __name__ == "__main__":



    def menu():
        
        # Pulisci lo schermo
        os.system("cls")

        print("""
         ______                         _____                    _      
        |  ____|                       / ____|                  | |     
        | |__ __ _ _   _ ___  ___ _ __| |     _ __ __ ___      _| |_ __ 
        |  __/ _` | | | / __|/ _ \ '__| |    | '__/ _` \ \ /\ / / | '__|
        | | | (_| | |_| \__ \  __/ |  | |____| | | (_| |\ V  V /| | |   
        |_|  \__,_|\__,_|___/\___|_|   \_____|_|  \__,_| \_/\_/ |_|_|       Copyright © 2018 Aiman\n\n\n
        """)

        
        print("""SELEZIONA UNA SCELTA:
            [1] Visualizza le note
            [2] Visualizza i docenti assenti
            [3] Visualizza le variazioni dell'orario
            [4] Visualizza le sostituzioni delle aule
            [5] Visualizza le entrate posticipate e le uscite anticipate
            [9] Esci
            """)

        # Creo oggetto
        obj = FauserCrawlr()

        try:
            rawinput = int(input("> "))

        except Exception as identifier:
            print("[!] Inserisci un numero da 1 a 5")

        finally:
            os.system("cls")

            if(rawinput == 1):
                obj.CrawlNote()
            elif(rawinput == 2):
                obj.CrawlProfessori()
            elif(rawinput == 3):
                obj.CrawlVariazioniGiorno()
            elif(rawinput == 4):
                obj.CrawlVariazioniAule()
            elif(rawinput == 5):
                obj.CrawlEntratePostUsciteAntic()
            elif(rawinput == 9):
                sys.exit()




    while(True):
        menu()




