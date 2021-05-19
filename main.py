## -*- coding: utf-8 -*-

import math
import time
def nouvellegrille():
    return [[" "for i in range(12)]for j in range(12)],[i for i in range(1,145)]
    

    
def affiche(grille):# permet   d’ afficher   une grille
    print(" 1  2  3  4  5  6  7  8  9  10  11  12")
    print("_____________________________________")
    for i in range(12):
        for j in range(12):
            print ('|',grille[i][j], end='')
        print('|',i+1)
        print("_____________________________________")
    print(" 1  2  3  4  5  6  7  8  9  10  11  12")
        
    
def Actions(grille):
    casesaanalyser=[]
    for i in range(12):
        for j in range(12):
                if grille[i][j]!=" ":
                    for n in range(-1,2):
                        for m in range(-1,2):
                            X=i-n
                            Y=j-m
                            
                            if (X,Y) not in casesaanalyser and X<=11 and X>=0 and Y<=11 and Y>=0 :
                                if grille[X][Y]==" ":
                                    casesaanalyser.append((X,Y))
    return casesaanalyser
    

def placerlecoup(grille,y,x,couppossible):
    nbr=0
    coup=((y-1)*12)+(x-1)+1
    for i in range(12):
        for j in range(12):
            if (grille[i][j] == 'X' or grille[i][j] == 0):
                nbr += 1
    if coup in couppossible:
        if nbr%2==0:
            grille[y-1][x-1]='X'
        else:
            grille[y-1][x-1]=0
        couppossible.remove(coup)
    else:
        print("jouez un coup valide s'il vous plait")
    return couppossible
    
def queljoueurjoue(joueur1,joueur2,grille):
    nbr=0
    for i in range(12):
        for j in range(12):
            if (grille[i][j] == 'X' or grille[i][j] == 0):
                nbr += 1
    if nbr % 2 == 0:
        return joueur1 + '(X)'
    else:
        return joueur2 + '(0)'


def place(grille):
    nbr = 0
    for i in range(12):
        for j in range(12):
            if (grille[i][j] == 'X' or grille[i][j] == 0):
                nbr += 1
    return nbr


def gagner(grille, profondeur):
    g = ""
    for i in range(12):
       for j in range(12):
           if grille[i][j]!=" ":
               if j<=8:
                   if grille[i][j]==grille[i][j+1]==grille[i][j+2]==grille[i][j+3]:
                      g=grille[i][j]
               if i<=8:
                   if grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j]:
                      g=grille[i][j]
               if i<=8 and j<=8:
                   if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]==grille[i+3][j+3]:
                      g=grille[i][j]
               if i<=8 and j>=3:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2]==grille[i+3][j-3]:
                      g=grille[i][j]     
              
    if g==0:
        return -1
    if g=='X':
        return 1
    return 0


def jeuprincipale():
    choix=0
    while choix!="5":
        grille,couppossible=nouvellegrille()
        print("1) jouez l'un contre l'autre")
        print("2) Jouez contre BOB (vous commence)")
        print("3) Jouez contre BOB (BOB commence)")
        print("4) ia vs ia")
        print("5) Quitter")
        choix=(input("?"))
          
        if choix=="1":
            joueur1=input("Entrez votre nom joueur 1 : ")
            joueur2=input("Entrez votre nom joueur 2 : ")
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
                print("a vous de jouer", queljoueurjoue(joueur1, joueur2, grille), "quel coup voulez vous faire ")
                print(len(couppossible))
                x=int(input("Entrez un x : "))
                y=int(input("Entrez un nombre y: "))
                couppossible=placerlecoup(grille,y,x,couppossible)
                print(couppossible)
        if choix=="2":
            premiercoup=True
            joueur1=input("Entrez votre nom joueur 1 : ")
            joueur2="ordi"
            tempstotal=0
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
                print(queljoueurjoue(joueur1, joueur2, grille))
                if queljoueurjoue(joueur1, joueur2, grille) != "ordi(0)":
                    print("a vous de jouer", queljoueurjoue(joueur1, joueur2, grille), "quel coup voulez vous faire ")
                    print(len(couppossible))
                    x = int(input("Entrez un x : "))
                    y = int(input("Entrez un nombre y: "))
                    couppossible = placerlecoup(grille, y, x, couppossible)
                else:
                    if premiercoup==False:
                        meilleurcoup=None
                        α=-math.inf
                        β=math.inf
                        debut=time.time()
                        a=Actions(grille)
                        for A in a:
                            grille[A[0]][A[1]]=0
                            if gagner(grille,0)<0:
                                meilleurcoup=[A[0],A[1]]
                                grille[A[0]][A[1]]=' '
                                break
                            grille[A[0]][A[1]]=' '
                        if meilleurcoup==None:
                            meilleurcoup=minValue(grille,0,α,β,3)[1]
                        fin=time.time()
                        tempstotal+=(fin-debut)
                        print(fin-debut)
                        
                    else:
                         meilleurcoup=[y,x]
                         premiercoup=False
                     
                    couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                    print("Bob a jouer:",meilleurcoup[1]+1,",",meilleurcoup[0]+1)
        
        
        
        if choix=="3":
            premierscoups=0
            premiercoup=True
            joueur2=input("Entrez votre nom joueur 1 : ")
            joueur1="ordi"
            tempstotal=0
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
                if queljoueurjoue(joueur1, joueur2, grille) =="ordi(X)":
                    if premiercoup==False:
                        meilleurcoup=None
                        α=-math.inf
                        β=math.inf
                        debut=time.time()
                        if premierscoups>=2:
                            print("r")
                            a=Actions(grille)
                            for A in a:
                                grille[A[0]][A[1]]='X'
                                if gagner(grille,0)>0:
                                    meilleurcoup=[A[0],A[1]]
                                    grille[A[0]][A[1]]=' '
                                    break
                                grille[A[0]][A[1]]=' '
                            if meilleurcoup==None:
                                meilleurcoup=maxValue(grille,1,α,β,3)[1]
                            fin=time.time()
                            print(fin-debut)
                            tempstotal+=(fin-debut)
                        if premierscoups<2:
                            premierscoups+=1
                            meilleurcoup=maxValue(grille,1,α,β,3)[1]
                            deuxiemecoup=False
                            
                    else:
                         meilleurcoup=[5,5]
                         premiercoup=False
                    couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                    print("Bob a jouer:",meilleurcoup[1]+1,",",meilleurcoup[0]+1)
                else:
                    print("a vous de jouer", queljoueurjoue(joueur1, joueur2, grille), "quel coup voulez vous faire ")
                    x = int(input("Entrez un x : "))
                    y = int(input("Entrez un nombre y: "))
                    couppossible = placerlecoup(grille, y, x, couppossible)
            
            print("BOB a jouer en",round(tempstotal,3)," secondes au total ")
            
            
            
            
        if choix=="4":
            premiercoup=True
            joueur1="ordi1"
            joueur2="ordi2"
            while gagner(grille,0)==0 and len(couppossible)!=0:
                x = (input("Entrez un x : "))
                if premiercoup==True:
                    x=5
                    y=5
                    meilleurcoup=[x,y]
                    couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                    meilleurcoup=[y+1,x+1]
                    couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                    premiercoup=False
                else:
                    
                    if queljoueurjoue(joueur1,joueur2,grille)!="ordi2(0)":
                            α=-math.inf
                            β=math.inf
                            debut=time.time()
                            meilleurcoup=maxValue(grille,0,α,β,3)[1]
                            fin=time.time()
                            print(fin-debut)
                            couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                            print(meilleurcoup[0]+1,",",meilleurcoup[1]+1)
                            affiche(grille)
                    
                    else:
                            α=-math.inf
                            β=math.inf
                            debut=time.time()
                            meilleurcoup=minValue(grille,0,α,β,3)[1]
                            fin=time.time()
                            print(fin-debut)
                            couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                            print(meilleurcoup[1]+1,",",meilleurcoup[0]+1)
                            affiche(grille)
        
        
        
        if choix!="5":
            affiche(grille)
            if gagner(grille,0)>0:
                       print("bravo", joueur1,"vous avez gagner")
            if gagner(grille,0)<0:
                       print("bravo", joueur2,"vous avez gagner")
            if gagner(grille,0)==0:
                       print("egalité")
                            
            
def heuristique(grille,profondeur):
    j1='X'
    j2=0
    score=0
    for i in range(12):
       for j in range(12):
           if grille[i][j]!=" ":     
               
               if j<=8:
                   if grille[i][j]==grille[i][j+1]==grille[i][j+2]==grille[i][j+3]:
                      if grille[i][j]==j1:
                            return ( 1000+profondeur)
                      if grille[i][j]==j2:
                            return- ( 1000+profondeur)       
               if i<=8:
                   if grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j]:
                       if grille[i][j]==j1:
                            return ( 1000+profondeur)
                       if grille[i][j]==j2:
                            return- ( 1000+profondeur) 
               if i<=8 and j<=8:
                   if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]==grille[i+3][j+3]:
                      if grille[i][j]==j1:
                            return ( 1000+profondeur)
                      if grille[i][j]==j2:
                            return- ( 1000+profondeur) 
               if i<=8 and j>=3:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2]==grille[i+3][j-3]:
                      if grille[i][j]==j1:
                            return ( 1000+profondeur)
                      if grille[i][j]==j2:
                            return- ( 1000+profondeur)
               
               if i<=9 and i>=1:
                   if grille[i-1][j]==grille[i+2][j]==" "and grille[i][j]==grille[i+1][j]:
                      if grille[i][j]==j1:
                            score+=2
                      if grille[i][j]==j2:
                            score+= -2          
            
               if j<=9 and j>=1:
                   if grille[i][j-1]==grille[i][j+2]==" "and grille[i][j]==grille[i][j+1]:  
                         if grille[i][j]==j1:
                            score+=2
                         if grille[i][j]==j2:
                            score+= -2
               
              
               if i<=9 and j<=9 and j>=1 and i>=1:
                   if grille[i][j]==grille[i+1][j+1] and grille[i+2][j+2]==grille[i-1][j-1]==" ":
                          if grille[i][j]==j1:
                            score+=2
                          if grille[i][j]==j2:
                            score+=-2
                
               if i<=9 and j<=10 and j>=2 and i>=1:
                    if grille[i][j]==grille[i+1][j-1] and grille[i+2][j-2]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=2
                      if grille[i][j]==j2:
                            score+=-2
                   
               if i<=8:
                  if grille[i+3][j]==" " and grille[i][j]==grille[i+1][j]==grille[i+2][j]:
                      if grille[i][j]==j1:
                            score+=50
                      if grille[i][j]==j2:
                            score+=-50
                      
               if j<=8:
                   if grille[i][j+3]==" "and grille[i][j]==grille[i][j+1]==grille[i][j+2]:  
                         if grille[i][j]==j1:
                            score+=50
                         if grille[i][j]==j2:
                            score+=-50
               if i<=8 and j<=8:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2] and grille[i+3][j-3]==" ":
                      if grille[i][j]==j1:
                            score+=50
                      if grille[i][j]==j2:
                            score+=-50
                            
               if i<=8 and j>=3:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2] and grille[i+3][j-3]==" ":
                      if grille[i][j]==j1:
                            score+=50
                      if grille[i][j]==j2:
                            score+=-50
                            
               
               if i<=8 and i>=1:
                  if grille[i+3][j]==grille[i-1][j]==" "and grille[i][j]==grille[i+1][j]==grille[i+2][j]:
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
                      
               if j<=8 and j>=1:
                   if grille[i][j-1]==grille[i][j+3]==" "and grille[i][j]==grille[i][j+1]==grille[i][j+2]:  
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
              
               if i<=8 and j<=8 and j>=1 and i>=1:
                   if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2] and grille[i+3][j+3]==grille[i-1][j-1]==" ":
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
        
                         
               if i<=8 and j<=8 and j>=1 and i>=1:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2] and grille[i+3][j-3]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=10
                      if grille[i][j]==j2:
                            score+=-10
               
               
    return score
    
    
            
def maxValue(grille,profondeur,α,β,pronfondeurmaxi):
    if place(grille)==144 or gagner(grille,profondeur)!=0 or profondeur>pronfondeurmaxi:  
        return [heuristique(grille,profondeur)]
    meilleurscore=-math.inf
    coup=None
    for a in Actions(grille):
                     grille[a[0]][a[1]]="X"
                     score=minValue(grille,profondeur+1,α,β,pronfondeurmaxi)[0]
                     grille[a[0]][a[1]]=" "
                     if meilleurscore<score:
                         meilleurscore=score
                         coup=[a[0],a[1]]
                     if meilleurscore>=β:
                         return meilleurscore,coup
                     α=max(α,meilleurscore)              
    return meilleurscore,coup
    
def minValue(grille,profondeur,α,β,pronfondeurmaxi):   #fonction de minimisation 
    if place(grille)==144 or gagner(grille,profondeur)!=0 or profondeur>pronfondeurmaxi:  
        return [heuristique(grille,profondeur)]
    meilleurscore=math.inf 
    coup=None
    for a in Actions(grille):
                  grille[a[0]][a[1]]=0
                  score=maxValue(grille,profondeur+1,α,β,pronfondeurmaxi)[0]
                  grille[a[0]][a[1]]=" "
                  if meilleurscore>score:
                     meilleurscore=score
                     coup=[a[0],a[1]]
                  if meilleurscore<=α:
                    return meilleurscore,coup
                  β=min(β,meilleurscore)
    return meilleurscore,coup


jeuprincipale()
