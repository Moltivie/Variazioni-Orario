import telegram



# METODO
# OUTPUT DELLE NOTE

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")


# tables[0] rappresenza la tabella "Note XX-XX-XXXX"
tr = tables[0].findAll("tr")

# Lambda array dei docenti assenti del giorno XX-XX-XXXX
array_note = [x.text for x in tr]

# Stampa delle note
if (len(array_note) == 1):
    print("Nessuna nota.")

# Rimozione del primo elemento rappresentante l'haeder della tabella corrente
else: 
    array_note.pop(0)
    print(array_note)


# ======================================================================================


# METODO
# OUTPUT DEI PROFESSORI ASSENTI

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")


# tables[1] rappresenza la tabella "Assenze Docenti del giorno XX-XX-XXXX"
tr = tables[1].findAll("tr")

# Lambda array dei docenti assenti del giorno XX-XX-XXXX
array_assenze_docenti = [x.text for x in tr]

# Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
array_assenze_docenti.pop(0)
array_assenze_docenti.pop(0)

# Stampa dei docenti assenti

if not array_assenze_docenti:
    print("Nessun docente assente.")
else:
    print(array_assenze_docenti)


# ======================================================================================


# METODO
# OUTPUT VARIAZIONI DEL GIORNO

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")


# tables[2] rappresenza la tabella "Variazioni del giorno XX-XX-XXXX"
tr = tables[2].findAll("tr")

# Lambda array delle variazioni dell'orario del giorno XX-XX-XXXX
array_variazioni = [x.text for x in tr]

# Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
array_variazioni.pop(0)
array_variazioni.pop(0)

# Stampa delle variazioni

if not array_variazioni:
    print("Nessuna variazione dell'orario.")

else:
    print(array_variazioni)


# ======================================================================================


# METODO
# OUTPUT SOSTITUZIONE AULE

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")


# tables[3] rappresenza la tabella "Sostituzione Aule XX-XX-XXXX"
tr = tables[3].findAll("tr")

# Lambda array delle sostituzioni delle aule del giorno XX-XX-XXXX
array_sostituzione_aule = [x.text for x in tr]

# Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
array_sostituzione_aule.pop(0)
array_sostituzione_aule.pop(0)

# Stampa delle sostituzioni aule

if not array_sostituzione_aule:
    print("Nessuna variazione delle aule.")

else:
    print(array_sostituzione_aule)


# ======================================================================================


# METODO
# OUTPUT ENTRATE POSTICIPATE - USCITE ANTICIPATE

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")


# tables[4] rappresenza la tabella "Entrate posticipate / Uscite anticipate XX-XX-XXXX"
tr = tables[4].findAll("tr")

# Lambda array delle entrate posticipate - uscite anticipate del giorno XX-XX-XXXX
entr_post_usc_antic = [x.text for x in tr]

# Rimozione dei primi due elementi rappresentanti gli haeder della tabella corrente
entr_post_usc_antic.pop(0)
entr_post_usc_antic.pop(0)

# Stampa delle variazioni

if not entr_post_usc_antic:
    print("Nessuna nota sulle entrate posticipate e/o uscite anticipate.")

else:
    print(entr_post_usc_antic)


# ======================================================================================

# METODO 
# OUTPUT INVIA RAW API A TELEGRAM

# Request della pagina html
req = requests.get(_base_url)

# Parser della pagina html in BeautifulSoup
soup = bs(req.content, "html.parser")


# Restituisce tutte le tabelle nella pagina
tables = soup.findAll("table")

# tables[0] rappresenza la tabella "Note XX-XX-XXXX"
tr = tables[0].findAll("tr")

# Lambda array dei docenti assenti del giorno XX-XX-XXXX
array_note = [x.text for x in tr]

# Invia delle note tramite Telegram
if (len(array_note) == 1):
    print("Nessuna nota.")

# Rimozione del primo elemento rappresentante l'haeder della tabella corrente
else: 
    array_note.pop(0)
    print(array_note)

