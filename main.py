## -*- coding: utf-8 -*-

import math
def nouvellegrille():
    return [[" "for i in range(12)]for j in range(12)],[i for i in range(1,145)]
    
    
    
def affiche(grille):# permet   d’ afficher   une grille
    print("_____________________________________")
    for i in range(12):
        for j in range(12):
            print ("|",grille[i][j], end='')
        print("|")
        print("_____________________________________")
        
    
    

def placerlecoup(grille,x,y,couppossible):
    nbr=0
    coup=((y-1)*12)+(x-1)+1
    for i in range(12):
        for j in range(12):
            if (grille[i][j]=='X' or grille[i][j]==0):
                nbr+=1
    if coup in couppossible:
        if nbr%2==0:
            grille[x-1][y-1]='X'
        else:
            grille[x-1][y-1]=0
        couppossible.remove(coup)
    else :
        print("jouez un coup valide s'il vous plait")
    return couppossible
        
def queljoueurjoue(joueur1,joueur2,grille):
    nbr=0
    for i in range(12):
        for j in range(12):
            if (grille[i][j]=='X' or grille[i][j]==0):
                nbr+=1
    if nbr%2==0:
        return joueur1+'(X)'
    else:
        return joueur2+'(0)'

def place(grille):
    nbr=0
    for i in range(12):
        for j in range(12):
            if (grille[i][j]=='X' or grille[i][j]==0):
                nbr+=1
    return nbr
def gagner(grille,profondeur):
    g=""
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
        return -100-(profondeur/100)
    if g=='X':
        return 100+(profondeur/100) 
    return 0
    
    
        

def jeuprincipale():
    choix=0
    alpha=-math.inf
    beta=math.inf
    while choix!="3":
        grille,couppossible=nouvellegrille()
        print("1) jouez l'un contre l'autre")
        print("2) Jouez contre une IA")
        print("3) Quitter")
        choix=(input("?"))
          
        if choix=="1":
            joueur1=input("Entrez votre nom joueur 1 : ")
            joueur2=input("Entrez votre nom joueur 2 : ")
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
                print("a vous de jouer",queljoueurjoue(joueur1,joueur2,grille),"quel coup voulez vous faire ")
                print(len(couppossible))
                x=int(input("Entrez un x : "))
                y=int(input("Entrez un nombre y: "))
                couppossible=placerlecoup(grille,y,x,couppossible)
        if choix=="2":
            joueur1="regis"#input("Entrez votre nom joueur 1 : ")
            joueur2="ordi"
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
                print(queljoueurjoue(joueur1,joueur2,grille))
                if queljoueurjoue(joueur1,joueur2,grille)!="ordi(0)":
                    print("a vous de jouer",queljoueurjoue(joueur1,joueur2,grille),"quel coup voulez vous faire ")
                    print(len(couppossible))
                    x=int(input("Entrez un x : "))
                    y=int(input("Entrez un nombre y: "))
                    couppossible=placerlecoup(grille,y,x,couppossible)
                else:
                    meilleurcoup=[]
                    meilleurscore=math.inf
                    for i in range(12):
                        for j in range(12):
                            if grille[i][j]==" ":
                                grille[i][j]=0
                                score=minimax(grille,0,False,True,alpha,beta)
                                grille[i][j]=" "
                                if score<meilleurscore:
                                    meilleurscore=score
                                    meilleurcoup=[i+1,j+1]
                                    print(meilleurscore)
                    couppossible=placerlecoup(grille,meilleurcoup[0],meilleurcoup[1],couppossible)
                    print(meilleurcoup[0],",",meilleurcoup[1])
        if choix!=3:
            affiche(grille)
            if gagner(grille,0)==1:
                       print("bravo", joueur1,"vous avez gagner")
            if gagner(grille,0)==-1:
                       print("bravo", joueur2,"vous avez gagner")
            if gagner(grille,0)==0:
                       print("egalité")
                            
            
def calculscore(grille):
    g=0
    for i in range(12):
       for j in range(12):
           if grille[i][j]!=" ":
               if j<=9:
                   if grille[i][j]==grille[i][j+1]==grille[i][j+2]:
                      g=grille[i][j]
               if i<=10:
                   if grille[i][j]==grille[i+1][j]==grille[i][j+2]:
                      g=grille[i][j]
               if i<10 and j<=8:
                   if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]:
                      g=grille[i][j]
               if i<10 and j>=1:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2]:
                      g=grille[i][j]
    if g==0:
        return -1
    if g=='X':
        return 1
    return 0
    
    
            
def minimax(grille,profondeur,minisation,ordijoueur2,alpha,beta):
    if gagner(grille,profondeur)!=0: 
        return gagner(grille,profondeur)
    if place(grille)==144:
        return 0
    if profondeur>1:
        return calculscore(grille)
    
    
    
    if minisation==False: #fonction de maximisation
         meilleurscore=-math.inf
         for i in range(12):
             for j in range(12):
                 if grille[i][j]==" ":
                     grille[i][j]="X"
                     score=minimax(grille,profondeur+1,True,ordijoueur2,alpha,beta)
                     grille[i][j]=" "
                     meilleurscore=max(score,meilleurscore)
                     if meilleurscore>=beta:
                         return beta
                     meilleurscore=max(alpha,meilleurscore)
         return meilleurscore
    
    
    
    
    if minisation==True:      #fonction de minimisation 
         meilleurscore=math.inf
         for i in range(12):
             for j in range(12):
                if grille[i][j]==" ":
                  grille[i][j]=0
                  score=minimax(grille,profondeur+1,False,ordijoueur2,alpha,beta)
                  grille[i][j]=" "
                  meilleurscore=min(score,meilleurscore)
                  if meilleurscore<=alpha:
                    return alpha
                  beta=min(beta,meilleurscore)
         return meilleurscore
        
    
    