## -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:54:38 2021

@author: regis
"""
import math
import time
def nouvellegrille():
    return [[" "for i in range(12)]for j in range(12)],[i for i in range(1,145)]
    
    
    
def affiche(grille):# permet   d’ afficher   une grille
    print(" 1  2  3  4  5  6  7  8  9  10  11  12")
    print("_____________________________________")
    for i in range(12):
        for j in range(12):
            print ("|",grille[i][j], end='')
        print("|",i+1)
        print("_____________________________________")
    print(" 1  2  3  4  5  6  7  8  9  10  11  12")
        
    
    

def placerlecoup(grille,y,x,couppossible):
    nbr=0
    coup=((y-1)*12)+(x-1)+1
    for i in range(12):
        for j in range(12):
            if (grille[i][j]=='X' or grille[i][j]==0):
                nbr+=1
    if coup in couppossible:
        if nbr%2==0:
            grille[y-1][x-1]='X'
        else:
            grille[y-1][x-1]=0
        couppossible.remove(coup)
    else :
        print("jouez un coup valide s'il vous plait")
    return couppossible
def jouerordi(coup,grille,joueur,couppossible):
    x=coup%12
    if x==0:
        x=12
    y=int(coup/12)
    grille[y-1][x-1]
    couppossible.remove(coup)
    return grille,couppossible
    
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
        return -(100+profondeur/100)
    if g=='X':
        return (100+profondeur/100) 
    return 0
    
    
        

def jeuprincipale():
    choix=0
    while choix!="4":
        grille,couppossible=nouvellegrille()
        print("1) jouez l'un contre l'autre")
        print("2) Jouez contre une IA")
        print("3) ia vs ia")
        print("4) Quitter")
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
                print(couppossible)
        if choix=="2":
            premiercoup=True
            joueur1=input("Entrez votre nom joueur 1 : ")
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
                    if premiercoup==False:
                        α=-math.inf
                        β=math.inf
                        debut=time.time()
                        meilleurcoup=minValue(grille,0,α,β)[1]
                        fin=time.time()
                        print(fin-debut)
                    else:
                         meilleurcoup=[y,x]
                         premiercoup=False
                     
                    couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                    print(meilleurcoup[0]+1,",",meilleurcoup[1]+1)
                    
        if choix=="3":
            premiercoup=True
            joueur1="ordi1"
            joueur2="ordi2"
            while gagner(grille,0)==0 and len(couppossible)!=0:
                affiche(grille)
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
                            meilleurcoup=maxValue(grille,0,α,β)[1]
                            fin=time.time()
                            print(fin-debut)
                            couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                            print(meilleurcoup[0]+1,",",meilleurcoup[1]+1)
                            affiche(grille)
                    
                    else:
                            α=-math.inf
                            β=math.inf
                            debut=time.time()
                            meilleurcoup=minValue(grille,0,α,β)[1]
                            fin=time.time()
                            print(fin-debut)
                            couppossible=placerlecoup(grille,meilleurcoup[0]+1,meilleurcoup[1]+1,couppossible)
                            print(meilleurcoup[0]+1,",",meilleurcoup[1]+1)
                            affiche(grille)
        
        
        
        if choix!="4":
            affiche(grille)
            if gagner(grille,0)==1:
                       print("bravo", joueur1,"vous avez gagner")
            if gagner(grille,0)==-1:
                       print("bravo", joueur2,"vous avez gagner")
            if gagner(grille,0)==0:
                       print("egalité")
                            
def deuxtrucalligner(grille):
    j1='X'
    j2=0
    score=0
    for i in range(12):
       for j in range(12):
           if grille[i][j]!=" ":
               if i<=9 and i>=1:
                  if grille[i-1][j]==grille[i+2][j]==" "and grille[i][j]==grille[i+1][j]:
                      if grille[i][j]==j1:
                            score+=1
                      if grille[i][j]==j2:
                            score+= -1
                  if grille[i-1][j]==grille[i+1][j]==" " and  grille[i][j]==grille[i+2][j]:
                      if grille[i][j]==j1:
                            score+=-1
                      if grille[i][j]==j2:
                            score+= 1
                      
               if j<=9 and j>=1:
                   if grille[i][j-1]==grille[i][j+2]==" "and grille[i][j]==grille[i][j+1]:  
                         if grille[i][j]==j1:
                            score+=1
                         if grille[i][j]==j2:
                            score+= -1
                   if grille[i][j-1]==grille[i][j+1]==" "and grille[i][j]==grille[i][j+2]:  
                        if grille[i][j]==j1:
                            score+=-1
                        if grille[i][j]==j2:
                            score+= 1
              
               if i<=9 and j<=9 and j>=1 and i>=1:
                   if grille[i][j]==grille[i+1][j+1] and grille[i+2][j+2]==grille[i-1][j-1]==" ":
                          if grille[i][j]==j1:
                            score+=1
                          if grille[i][j]==j2:
                            score+=-1
                   if grille[i][j]==grille[i+2][j+2] and grille[i+1][j+1]==grille[i-1][j-1]==" ":
                          if grille[i][j]==j1:
                            score+=-1
                          if grille[i][j]==j2:
                            score+=1
               if i<=9 and j<=9 and j>=1 and i>=1:
                    if grille[i][j]==grille[i+1][j-1] and grille[i+2][j-2]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=1
                      if grille[i][j]==j2:
                            score+= -1
                    if grille[i][j]==grille[i+2][j-2] and grille[i+1][j-1]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=-1
                      if grille[i][j]==j2:
                            score+= 1
               if i<=8 and i>=1:
                  if grille[i-1][j]==grille[i+3][j]==" "and grille[i][j]==grille[i+1][j]==grille[i+2][j]:
                      if grille[i][j]==j1:
                            score+=10
                      if grille[i][j]==j2:
                            score+= -10
                  if grille[i-1][j]==grille[i+2][j]==" "and grille[i][j]==grille[i+1][j]==grille[i+3][j]:
                      if grille[i][j]==j1:
                            score+=-10
                      if grille[i][j]==j2:
                            score+= 10
                      
               if j<=8 and j>=1:
                   if grille[i][j-1]==grille[i][j+3]==" "and grille[i][j]==grille[i][j+1]==grille[i][j+2]:  
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+= -10
                   if grille[i][j-1]==grille[i][j+2]==" "and grille[i][j]==grille[i][j+1]==grille[i][j+3]:  
                         if grille[i][j]==j1:
                            score+=-10
                         if grille[i][j]==j2:
                            score+=10
              
               if i<=8 and j<=8 and j>=1 and i>=1:
                   if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2] and grille[i+3][j+3]==grille[i-1][j-1]==" ":
                          if grille[i][j]==j1:
                            score+=50
                          if grille[i][j]==j2:
                            score+= -50
                   if grille[i][j]==grille[i+1][j+1]==grille[i+3][j+3] and grille[i+2][j+2]==grille[i-1][j-1]==" ":
                          if grille[i][j]==j1:
                            score+=50
                          if grille[i][j]==j2:
                            score+=-50
               if i<=8 and j<=8 and j>=1 and i>=1:
                    if grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2] and grille[i+3][j-3]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=50
                      if grille[i][j]==j2:
                            score+= -50
                    if grille[i][j]==grille[i+1][j-1]==grille[i+3][j-3] and grille[i+2][j-2]==grille[i-1][j+1]==' ':
                      if grille[i][j]==j1:
                            score+=50
                      if grille[i][j]==j2:
                            score+=-50
               if j>=2 and j<=9:             
                 if grille[i][j]!=grille[i][j+1] and grille[i][j+1]!=" " and grille[i][j+1]==grille[i][j-1] and grille[i][j+2]==grille[i][j-2]==" ":
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
               if i>=2 and i<=9:
                  if grille[i][j]!=grille[i+1][j] and grille[i+1][j]!=" " and grille[i+1][j]==grille[i-1][j] and grille[i+2][j]==grille[i-2][j]==" ":
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
               if j>=2 and j<=9 and  i>=2 and i<=9:
                   if grille[i][j]!=grille[i+1][j+1] and grille[i+1][j+1]!=" " and grille[i+1][j+1]==grille[i-1][j+1] and grille[i+2][j+2]==grille[i-2][j-2]==" ":
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
                   if grille[i][j]!=grille[i+1][j-1] and grille[i+1][j-1]!=" " and grille[i+1][j-1]==grille[i-1][j+1] and grille[i+2][j-2]==grille[i-2][j+2]==" ":
                         if grille[i][j]==j1:
                            score+=10
                         if grille[i][j]==j2:
                            score+=-10
                   
                
    return score
    
            
def maxValue(grille,profondeur,α,β):
    g=gagner(grille,profondeur)
    if g!=0: 
        return [g]
    if place(grille)==144:
        return [0]
    if profondeur>2:
        return [deuxtrucalligner(grille)]
    meilleurscore=-math.inf
    coup=None
    for i in range(12):
             for j in range(12):
                 if grille[i][j]==" ":
                     grille[i][j]="X"
                     score=minValue(grille,profondeur+1,α,β)[0]
                     grille[i][j]=" "
                     if meilleurscore<score:
                         meilleurscore=score
                         coup=[i,j]
                     if meilleurscore>=β:
                         return meilleurscore,coup
                     α=max(α,meilleurscore)              
    return meilleurscore,coup
    
def minValue(grille,profondeur,α,β):  
    g=gagner(grille,profondeur)
    if g!=0: 
        return [g]
    if place(grille)==144:
        return [0]
    if profondeur>2:
        return [deuxtrucalligner(grille)]
    meilleurscore=math.inf #fonction de minimisation 
    coup=None
    for i in range(12):
        for j in range(12):
                if grille[i][j]==" ":
                  grille[i][j]=0
                  score=maxValue(grille,profondeur+1,α,β)[0]
                  grille[i][j]=" "
                  if meilleurscore>score:
                     meilleurscore=score
                     coup=[i,j]
                  if meilleurscore<=α:
                    return meilleurscore,coup
                  β=min(β,meilleurscore)
    return meilleurscore,coup







