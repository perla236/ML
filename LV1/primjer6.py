broj_ham = 0
broj_spam = 0
suma_rijeci = 0
broj_rijeci_ham = 0
broj_rijeci_spam = 0

broj_spam_usklicnik = 0

with open('SMSSpamCollection.txt', encoding='utf-8') as datoteka:
    for linija in datoteka:
        dijelovi = linija.strip().split('\t')
        oznaka = dijelovi[0]
        tekst = dijelovi[1]

        if oznaka == 'ham':
            broj_ham += 1
            broj_rijeci_ham += len(tekst.split())
        else:
            broj_spam += 1
            broj_rijeci_spam += len(tekst.split())
            if tekst.endswith('!'):
                broj_spam_usklicnik += 1

        suma_rijeci += len(tekst.split())

pros_rijeci_ham = broj_rijeci_ham / broj_ham
pros_rijeci_spam = broj_rijeci_spam / broj_spam

print(f"Prosječan broj riječi u ham porukama: {pros_rijeci_ham:.2f}")
print(f"Prosječan broj riječi u spam porukama: {pros_rijeci_spam:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {broj_spam_usklicnik}")
