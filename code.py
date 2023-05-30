def positions(wordToGuess,character,pos):
    #functia data determina pozitiile pe care se afla caracterul "character" in cuvantul "wordToGuess"
    #si memoreaza valorile indecsilor in lista pos
        for i in range(len(wordToGuess)):#parcurgem cuvantul dat
            if (character == wordToGuess[i]) or (character.upper()==wordToGuess[i]):#si pentru caracterul primit ca parametru
                                                                                    # determinam pozitiile acestuia
                pos.append(i)#si le adaugam la lista pos
        if len(pos)==0:#daca caracterul nu a existat in cuvantul dat
            pos.append(-1)#adaugam valoarea -1

def numberOfAttempts(guess,wordToGuess,letters):
    count=0 #count va memora numarul de litere deja existente in guess pentru a nu le mai verifica
    for char in guess:  # parcurgem fiecare caracter din cuvantul necunoscut
            if char.isalpha() == 1:  # si daca caracterul e litera
                if (char.lower() in letters) or (char in letters): #s-ar putea ca o litera sa fi fost deja marcata cu "-"
                                        #si atunci ca sa nu dea eroare intrebam daca caracterul e in lista
                                        # ex: **OHO**; pt primul o inlocuieste cu "-",iar pentru al doilea ar da eroare
                    x=letters.index(char.lower()) #indiferent ca e caracter mare sau mic, cautam pozitia celui mic in letters
                    letters[x]='-' #si pe pozitia respectiva marcam ca exista deja litera
                    count += 1
    """ OPTIMIZARE! => In momentul in care guess e complet determinat nu mai are rost sa continuam verificarea celorlalte litere care 
     au mai ramas deci numarul de incercari va scadea cu numarul de litere care au ramas neverificate """
    x=0
    for i in range(len(letters)-1,-1,-1): # parcurgem letters de la final la inceput
        if (letters[i] not in wordToGuess) and (letters[i].upper() not in wordToGuess): #daca litera nu exista
            if letters[i]!='-': # daca e diferita de "-"
                x+=1 #o contorizam
            else:               #in caz contrar mergem la pasul urmator deoarece literele marcate cu "-" sunt contorizate in count
                continue
        else:       # cand dam de o litera care se afla in cuvant
            break   # ne oprim
    return 31-x-count # la final returnam acest numar

def game(guess,wordToGuess,letters):
    #functia game determina literele care se afla in cuvant si il construieste pe guess(cuvantul necunoscut)
    pos = []
    print("NEXT WORD IS:",guess)
    for i in range(len(letters)):
        if letters[i]=='-': #daca litera de pe pozitia i a fost data inital in cuvantul necunoscut(guess)
            i+=1 #atunci incrementam valoarea lui i pentru a nu mai verifica daca acea litera exista in cuvant
        else:
            print("Is the letter ", letters[i],"in the word?")
            positions(wordToGuess,letters[i],pos)  #determinam pozitiile pe care se afla litera de pe pozitia i
            if pos[0]!=-1:
                print("YES! Positions are: ",pos) #daca litera se afla pe unele pozitii le afisam
                for j in range(len(pos)):
                    if letters[i].upper()==wordToGuess[pos[j]]:
                        letters[i]=letters[i].upper()
                    guess=guess[:pos[j]]+letters[i]+guess[pos[j]+1:]
                    #inlocuim caracterele * cu litera gasita pe pozitiile determinate
            else:
                print("NO!") #daca litera nu se afla in cuvant afisam un mesaj corespunzator
            pos.clear()
            print(guess)
            if guess in wordToGuess:   #cand determinam tot cuvantul ne oprim
                return ;

def main():
        count=1200
        with open('text.csv', 'r', encoding='UTF-8') as file:
            for line in file:
                list = line.split(';')
                letters=['a','c','r','i','g','m','î','n','e','p','d','b','u','o','h','l','ă','f'
                         ,'s','ș','t','â','ț','v','z','j','q','k','w','x','y']
                print(count, "attempts left")  # afisam numarul ramas de incercari
                noAttempts = numberOfAttempts(list[1],list[2],letters)   #determinam numarul de incercari pentru cuvantul curent
                game(list[1],list[2],letters)   #realizam jocul
                count=count-noAttempts  #scade numarul de incercari cu numarul determinat mai sus "noAttempts"
                print("Numarul total rezultat de incercari este: ",1200-count) #la final afisam numarul total de incercari necesare pentru acest fisier
if __name__ == '__main__':
        main()