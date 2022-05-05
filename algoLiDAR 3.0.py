import turtle
from math import *
################################################
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sqrt((self.x *self.x) + (self.y *self.y))
    def affiche(self):
        print("(",self.x,",",self.y,")")
    
################################################
def produit_scalaire(v,w):
    return((v.x*w.x)+(v.y*w.y))
################################################
def dessiner_piste(longext,largext,longint,largint,r):
    turtle.up()  #Lève le crayon
    turtle.goto(-longext/2, -150)
    turtle.down()
    for i in range(2):
        turtle.forward(longext)  #Côté
        turtle.circle(r, 90)
        turtle.forward(largext)
        turtle.circle(r, 90)
        
    turtle.up()  #Lève le crayon
    turtle.goto(-225, -100)
    turtle.down()

    for i in range(2):
        turtle.forward(longint)  #Côté
        turtle.circle(r, 90)
        turtle.forward(largint)
        turtle.circle(r, 90)
    turtle.up()  #Lève le crayon
    turtle.goto(x_voiture,y_voiture)
    turtle.down()
################################################
def dessiner_voiture(xv,yv,av,longv,largv):
    turtle.up()  #Lève le crayon
    turtle.goto(xv+cos(radians(av))*longv/2,yv+sin(radians(av))*longv/2)
    turtle.circle(0,90+av)
    turtle.down()
    turtle.color("blue")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(largv/2)
        turtle.circle(0, 90)
        turtle.forward(longv)  #Côté
        turtle.circle(0, 90)
        turtle.forward(largv/2)

    turtle.end_fill()
    turtle.color("black")
    turtle.up()  #Lève le crayon
    turtle.goto(xv,yv)
    turtle.setheading(radians(av))
    turtle.down()
################################################
def segment(x,y):#dessine le segment limited by la position de la voiture et (x,y) 
    turtle.up() #Lève le cray
    turtle.goto(x_voiture,y_voiture)
    #turtle.circle(0,atan(angle_voiture+(y-y_voiture)/(x-x_voiture)))
    turtle.down()
    turtle.goto(x,y)
    turtle.dot(5, "red") #colorer le pt d'intersection
################################################
def verif_solve(A,B,C):
    delta=B*B-4*A*C # On calcule delta, le discriminant, en fonction de A,B et C
    return(delta>=0)
################################################
def solve(A,B,C):
    delta=B*B-4*A*C
    if verif_solve(A,B,C):
        racine_carre_delta=sqrt(delta) # On calcul la racine carré de delta
        k=-B-racine_carre_delta # Variable qui va intervenir dans le calcul de X1
        l=-B+racine_carre_delta # Variable qui va intervenir dans le calcul de x2
        m=2*A # Variable qui va intervenir dans le calcul de X1 et X2
        x1=k/m # Calcul de X1
        x2=l/m # Calcul de X2
    return((x1,x2))
################################################################################


def vert_intersect_d1(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d1
    return (not((abs(c)<=250) and (d>=75))and (abs(c)<275))
##########################################################
def vert_intersect_d4(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d4
    return (not((abs(c)<=250)and(d<=-75))and (abs(c)<275))
##########################################################
def vert_intersect_d3(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d3
    return ((abs(c)<225) and (d>100))
##########################################################
def vert_intersect_d2(c,d):#verifie s'il y a une intersection entre la droite verticale passant par la voiture et d2
    return (((abs(c)<225)and(d<-100)))
##########################################################
def intersect_d1(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d1
    y=-150
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<275))
##########################################################
def intersect_d4(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d4
    y=150
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<275))
##########################################################
def intersect_d2(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d2
    y=-100
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<225))
##########################################################
def intersect_d3(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d3
    y=100
    if (a==0):
        return (False)
    return ((abs((y-b)/a)<225))
##########################################################
def intersect_d5(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d5
    return(abs(-300*a+b)<125)
##########################################################
def intersect_d8(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d8
    return(abs(300*a+b)<125)
##########################################################
def intersect_d6(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d6
    return(abs(-250*a+b)<75)
##########################################################
def intersect_d7(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et d7
    return(abs(250*a+b)<75)
################################################
def verif_intersect_c5(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et c5
    x0=-225
    y0=-75
    if not(verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)):
        return(False)
    else:
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)    
        return(((solu[0]<=-225) and ((a*solu[0]+b)<=-75)) or ((solu[1]<=-225) and ((a*solu[1]+b)<=-75)))
################################################
def verif_intersect_c6(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et c6
    x0=225
    y0=-75
    if not(verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)):
        return(False)
    else:
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)    
        return(((-solu[0]<=-225) and ((a*solu[0]+b)<=-75)) or ((-solu[1]<=-225) and ((a*solu[1]+b)<=-75)))
################################################
def intersect_c1(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c1
    x0=-275
    y0=-125
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((solu[0]>=-300)and (solu[0]<=-275) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((solu[0]>=-300)and (solu[0]<=-275) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)) and (solu[1]>=-300)and (solu[1]<=-275) and ((a*solu[1]+b)<=-125) and ((a*solu[1]+b)>=-150):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((solu[0]>=-300)and (solu[0]<=-275) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif ((solu[1]>=-300)and (solu[1]<=-275) and ((a*solu[1]+b)<=-125) and ((a*solu[1]+b)>=-150)):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))            
################################################
def intersect_c2(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c2
    x0=275
    y0=-125
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((solu[0]>=275)and (solu[0]<=300) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((solu[0]>=275)and (solu[0]<=300) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)) and (solu[1]>=275)and (solu[1]<=300) and ((a*solu[1]+b)<=-125) and ((a*solu[1]+b)>=-150):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((solu[0]>=275)and (solu[0]<=300) and ((a*solu[0]+b)<=-125) and ((a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif (solu[1]>=275)and (solu[1]<=300) and ((a*solu[1]+b)<=-125) and ((a*solu[1]+b)>=-150):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))     
################################################
def intersect_c3(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c3
    x0=275
    y0=125
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((solu[0]>=275)and (solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((solu[0]>=275)and (solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)) and (solu[1]>=275)and (solu[1]<=300) and (-(a*solu[1]+b)<=-125) and (-(a*solu[1]+b)>=-150):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((solu[0]>=275)and (solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif (solu[1]>=275)and (solu[1]<=300) and (-(a*solu[1]+b)<=-125) and (-(a*solu[1]+b)>=-150):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def intersect_c4(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c4
    x0=-275
    y0=125
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if(-(solu[0]>=275)and (-solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((-solu[0]>=275)and (-solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)) and (-solu[1]>=275)and (-solu[1]<=300) and (-(a*solu[1]+b)<=-125) and (-(a*solu[1]+b)>=-150):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((-solu[0]>=275)and (-solu[0]<=300) and (-(a*solu[0]+b)<=-125) and (-(a*solu[0]+b)>=-150)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif (-solu[1]>=275)and (-solu[1]<=300) and (-(a*solu[1]+b)<=-125) and (-(a*solu[1]+b)>=-150):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def intersect_c5(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c5
    x0=-225
    y0=-75
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((solu[0]<=-225) and ((a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((solu[0]<=-225) and ((a*solu[0]+b)<=-75)) and ((solu[1]<=-225) and ((a*solu[1]+b)<=-75)):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((solu[0]<=-225) and ((a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif ((solu[1]<=-225) and ((a*solu[1]+b)<=-75)):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def intersect_c6(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c6
    x0=225
    y0=-75
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((-solu[0]<=-225) and ((a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((-solu[0]<=-225) and ((a*solu[0]+b)<=-75)) and ((-solu[1]<=-225) and ((a*solu[1]+b)<=-75)):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((-solu[0]<=-225) and ((a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif ((-solu[1]<=-225) and ((a*solu[1]+b)<=-75)):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def verif_intersect_c7(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et c7
    x0=225
    y0=75
    if not(verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)):
        return(False)
    else:
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)    
        return(((-solu[0]<=-225) and (-(a*solu[0]+b)<=-75)) or ((-solu[1]<=-225) and (-(a*solu[1]+b)<=-75)))
################################################
def intersect_c7(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c7
    x0=225
    y0=75
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((-solu[0]<=-225) and (-(a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((-solu[0]<=-225) and (-(a*solu[0]+b)<=-75)) and ((-solu[1]<=-225) and (-(a*solu[1]+b)<=-75)):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((-solu[0]<=-225) and (-(a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif ((-solu[1]<=-225) and (-(a*solu[1]+b)<=-75)):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def verif_intersect_c8(a,b):#verifie s'il y a une intersection entre la droite d'eq y=ax+b passant par la voiture et c8
    x0=-225
    y0=75
    if not(verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)):
        return(False)
    else:
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)    
        return(((solu[0]<=-225) and (-(a*solu[0]+b)<=-75)) or ((solu[1]<=-225) and (-(a*solu[1]+b)<=-75)))
################################################
def intersect_c8(a,b):#calcule l'intersection entre la droite d'eq y=ax+b passant par la voiture et c8
    x0=-225
    y0=75
    if verif_solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25):
        solu=solve(a*a+1,2*a*b-2*x0-2*a*y0,x0*x0+b*b+y0*y0-2*b*y0-25*25)
        if solu[0]==solu[1]:
            if((solu[0]<=-225) and (-(a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))
        else:
            if((solu[0]<=-225) and (-(a*solu[0]+b)<=-75)) and ((solu[1]<=-225) and (-(a*solu[1]+b)<=-75)):
                v1=vector(solu[0]-x_voiture,a*solu[0]+b-y_voiture)
                v2=vector(solu[1]-x_voiture,a*solu[1]+b-y_voiture)
                if v1.norm()<v2.norm():
                    l.append((solu[0],(a*solu[0]+b)))
                    segment(solu[0],(a*solu[0]+b))                    
                else:
                    l.append((solu[1],(a*solu[1]+b)))
                    segment(solu[1],(a*solu[1]+b))
            elif ((solu[0]<=-225) and (-(a*solu[0]+b)<=-75)):
                l.append((solu[0],(a*solu[0]+b)))
                segment(solu[0],(a*solu[0]+b))             
            elif ((solu[1]<=-225) and (-(a*solu[1]+b)<=-75)):
                l.append((solu[1],(a*solu[1]+b)))
                segment(solu[1],(a*solu[1]+b))  
################################################
def intersect_vert_c1(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c1
    x0=-275
    y0=-125
    if x<=-275:
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()<v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c4(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c4
    x0=-275
    y0=125
    if x<=-275:
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()<v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c3(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c3
    x0=275
    y0=125
    if x>=275:
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()<v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c2(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c2
    x0=275
    y0=-125
    if x>=275:
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()<v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c5(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c5
    x0=-225
    y0=-75
    if (x>=-250)and (x<=-225) and (y<=-75):
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()>v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c6(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c6
    x0=225
    y0=-75
    if (x<=250)and (-x<=-225) and (y<=-75):
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()>v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c7(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c7
    x0=225
    y0=75
    if (-x>=-250)and (-x<=-225) and (-y<=-75):
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()>v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def intersect_vert_c8(x,y):#calcule l'intersection entre la droite veticale passant par la (x,y) et c8
    x0=-225
    y0=75
    if (x>=-250)and (x<=-225) and (-y<=-75):
        solu=solve(1,-2*y0,(x-x0)**2+y0*y0-25*25)
        v1=vector(0,solu[0]-y)
        v2=vector(0,solu[1]-y)
        if v1.norm()>v2.norm():
            l.append((x,solu[1]))
            segment(x,solu[1])
        else:
            l.append((x,solu[0]))
            segment(x,solu[0])
################################################
def calcul_intersect_vert_d1(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d1
    if vert_intersect_d1(c,d):
        l.append((c,-150.0))
        segment(c,-150.0)
##########################################################
def calcul_intersect_vert_d4(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d4
    if vert_intersect_d4(c,d):
        l.append((c,150))
        segment(c,150)
##########################################################
def calcul_intersect_vert_d2(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d2
    if vert_intersect_d2(c,d):
        l.append((c,-100))
        segment(c,-100)
##########################################################
def calcul_intersect_vert_d3(c,d):#calcule le pt d'intersection entre la droite d'eq x=c passant par la voiture et d3
    if vert_intersect_d3(c,d):
        l.append((c,100))
        segment(c,100)
##########################################################
def calcul_intersect_d2(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d2
    if intersect_d2(a,b):
        yy=-100
        l.append(((yy-b)/a,yy))
        segment((yy-b)/a,yy)
##########################################################
def calcul_intersect_d3(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d3
    if intersect_d3(a,b):
        yy=100
        l.append(((yy-b)/a,yy))
        segment((yy-b)/a,yy)
##########################################################
def calcul_intersect_d1(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d1
    if intersect_d1(a,b):
        l.append(((-150-b)/a,-150))
        segment((-150-b)/a,-150)
##########################################################
def calcul_intersect_d4(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d4
    if intersect_d4(a,b):
        l.append(((150-b)/a,150))
        segment((150-b)/a,150)
##########################################################
def calcul_intersect_d5(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d5
    if intersect_d5(a,b):
        xx=-300
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)
##########################################################
def calcul_intersect_d6(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d6
    if intersect_d6(a,b):
        xx=-250
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)
##########################################################
def calcul_intersect_d7(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d7
    if intersect_d7(a,b):
        xx=250
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)
##########################################################
def calcul_intersect_d8(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et d8
    if intersect_d8(a,b):
        xx=300
        l.append((xx,a*xx+b))
        segment(xx,a*xx+b)
################################################
def intersect_piste(a,b):#calcule le pt d'intersection entre la droite d'eq y=ax+b passant par la voiture et la piste
    if (abs(x_voiture)<=225):
        if (y_voiture<-100):
            calcul_intersect_d1(a,b)
            calcul_intersect_d2(a,b)
            intersect_c1(a,b)
            intersect_c2(a,b)
            if not(intersect_d2(a,b)):
                intersect_c5(a,b)
                intersect_c6(a,b) 
                if not(verif_intersect_c5(a,b)):	               
                    calcul_intersect_d5(a,b)
                if not(verif_intersect_c6(a,b)):                
                    calcul_intersect_d8(a,b)
        else:
            calcul_intersect_d3(a,b)
            calcul_intersect_d4(a,b)
            intersect_c3(a,b)
            intersect_c4(a,b)            
            if not(intersect_d3(a,b)):
                intersect_c7(a,b)
                intersect_c8(a,b) 
                if not(verif_intersect_c8(a,b)):	               
                    calcul_intersect_d5(a,b)
                if not(verif_intersect_c7(a,b)):                
                    calcul_intersect_d8(a,b)                
    elif (abs(y_voiture)<=75):
        if (x_voiture<=0):
            calcul_intersect_d5(a,b)
            calcul_intersect_d6(a,b)
            intersect_c1(a,b)
            intersect_c4(a,b)                 
            if not(intersect_d6(a,b)):
                intersect_c5(a,b)
                intersect_c8(a,b)  
                if not(verif_intersect_c8(a,b)):	               
                    calcul_intersect_d4(a,b)
                if not(verif_intersect_c5(a,b)):                
                    calcul_intersect_d1(a,b) 
        else:
            calcul_intersect_d7(a,b)
            calcul_intersect_d8(a,b)
            intersect_c2(a,b)
            intersect_c3(a,b)    
            if not(intersect_d7(a,b)):
                intersect_c6(a,b)
                intersect_c7(a,b)  
                if not(verif_intersect_c7(a,b)):	               
                    calcul_intersect_d4(a,b)
                if not(verif_intersect_c6(a,b)):                
                    calcul_intersect_d1(a,b) 
                   
    elif (x_voiture<=-225) and (y_voiture<=-75):
        calcul_intersect_d1(a,b)
        calcul_intersect_d5(a,b)
        intersect_c1(a,b)
        intersect_c5(a,b)
        if not(verif_intersect_c5(a,b)):
            calcul_intersect_d2(a,b)
            calcul_intersect_d6(a,b)
            if (not(intersect_d2(a,b))):
                calcul_intersect_d8(a,b)
                intersect_c2(a,b)            
            if (not(intersect_d6(a,b)) and (not(intersect_d2(a,b)))):
                calcul_intersect_d4(a,b)
                intersect_c4(a,b) 

    elif (x_voiture>=225) and (y_voiture<=-75):
        calcul_intersect_d1(a,b)
        calcul_intersect_d8(a,b)
        intersect_c2(a,b)
        intersect_c6(a,b)
        if not(verif_intersect_c6(a,b)):
            calcul_intersect_d2(a,b)
            calcul_intersect_d7(a,b)
            if (not(intersect_d2(a,b))):
                calcul_intersect_d5(a,b)
                intersect_c1(a,b)            
            if (not(intersect_d7(a,b)) and (not(intersect_d2(a,b)))):
                calcul_intersect_d4(a,b)
                intersect_c3(a,b) 

        
    elif (x_voiture>=225) and (y_voiture>=75):
        calcul_intersect_d4(a,b)
        calcul_intersect_d8(a,b)
        intersect_c3(a,b)
        intersect_c7(a,b)
        if not(verif_intersect_c7(a,b)):
            calcul_intersect_d3(a,b)
            calcul_intersect_d7(a,b)
            if (not(intersect_d3(a,b))):
                calcul_intersect_d5(a,b)
                intersect_c4(a,b)            
            if (not(intersect_d7(a,b)) and (not(intersect_d3(a,b)))):
                calcul_intersect_d1(a,b)
                intersect_c2(a,b) 

   
    else:
        calcul_intersect_d4(a,b)
        calcul_intersect_d5(a,b)
        intersect_c4(a,b)
        intersect_c8(a,b)
        if not(verif_intersect_c8(a,b)):
            calcul_intersect_d3(a,b)
            calcul_intersect_d6(a,b)
            if (not(intersect_d3(a,b))):
                calcul_intersect_d8(a,b)
                intersect_c3(a,b)            
            if (not(intersect_d6(a,b)) and (not(intersect_d3(a,b)))):
                calcul_intersect_d1(a,b)
                intersect_c1(a,b) 
##########################################################
def dans_grand_rectangle(x,y):#verifie si (x,y) est dans le grand rectangle de la piste
    return (((abs(x)<300) and (abs(y)<=125)) or ((abs(x)<=275)and(abs(y)<150)) or ((abs(x)-275)*(abs(x)-275)+(abs(y)-125)*(abs(y)-125)<25*25))
##########################################################
def dans_petit_rectangle(x,y):#verifie si (x,y) est dans le petit rectangle de la piste
    return (((abs(x)<=250) and (abs(y)<=75)) or ((abs(x)<=225)and(abs(y)<=100)) or ((abs(x)-225)*(abs(x)-225)+(abs(y)-75)*(abs(y)-75)<25*25))
##########################################################
def saisie():#retourne x_voiture,y_voiture,angle_voiture apres validation de la saisie
    x=int(input("Donnez x_voiture : "))
    y=int(input("Donnez y_voiture : "))
    c=int(input("Donnez angle_voiture (en degree) : "))
    while(True):
        if (dans_grand_rectangle(x,y) and not(dans_petit_rectangle(x,y))):
            break
        print("Il faut que la voiture soit sur la piste ")
        x=int(input("Donnez x_voiture : "))
        y=int(input("Donnez y_voiture : "))
    c=c%360
    return(x,y,c)
    

 #############################################################  
 #############################################################
 #########################  MAIN  ############################  
 #############################################################        
 ############################################################# 
 
drawing_area=turtle.Screen() 
drawing_area.title("Piste")
turtle.speed(0)# si vous voulez dessiner avec la vitesse la plus rapide
turtle.tracer(False)# pour ne pas attendre le dessin 
#dimensions de la piste
longueur_ext=550#11m
longueur_int=450#9m
largeur_ext=250 #5m
largeur_int=150#3m
#dimensions de la voiture
longueur_voiture=25#0.5m
largeur_voiture=10#0.2m

######les positions de references de tests qui sont les corners et les milieux des droites de la piste#####
# p1=[0,-125,0]
# p2=[275,p1[1],45]
# p3=[p2[0],0,90]
# p4=[p2[0],125,135]
# p5=[0,p4[1],180]
# p6=[-275,p5[1],225]
# p7=[p6[0],p3[1],270]
# p8=[p6[0],p1[1],315]
# liste_positions=[p1,p2,p3,p4,p5,p6,p7,p8]


#nombre de droites a construire
nbr=180
while(True):
   nbr=int(input("Donnez le nombre de droites a construire (strictement positif) : "))
   if (nbr>0):
       break


#tableau ou on met les points d'intersections de la droite de pente tan(theta) passant par les coordonnees de la voiture  avec la piste
#theta=indice du tableau*360/nbr 
tableau_intersect=[]

#tableau de LiDAR: ce tableau stocke [angle par rapport vecteur de direction de la voiture , distance entre la voiture et le mur]
tab_lidar=[]

position=saisie()
x_voiture=position[0]
y_voiture=position[1]
angle_voiture=position[2]
vect_direction=vector(cos(radians(angle_voiture)),sin(radians(angle_voiture)))#vecteur de direction de la voiture

turtle.reset() #effacer pour creer une autre frame
turtle.tracer(False)
dessiner_piste(longueur_ext,largeur_ext,longueur_int,largeur_int,25)
turtle.up()  #Lève le crayon
turtle.goto(x_voiture,y_voiture)
turtle.down()

for i in range(nbr):
    theta=((180/nbr)*i+angle_voiture)%180
    l=[]
    if ((theta!=90)and(theta!=270)):     
        intersect_piste(tan(radians(theta)),y_voiture-tan(radians(theta))*x_voiture)
        tableau_intersect.append(l)
    else:
        calcul_intersect_vert_d2(x_voiture,y_voiture)
        calcul_intersect_vert_d4(x_voiture,y_voiture)
        calcul_intersect_vert_d1(x_voiture,y_voiture)
        calcul_intersect_vert_d3(x_voiture,y_voiture)
        intersect_vert_c1(x_voiture,y_voiture)
        intersect_vert_c2(x_voiture,y_voiture)
        intersect_vert_c3(x_voiture,y_voiture)
        intersect_vert_c4(x_voiture,y_voiture)
        intersect_vert_c5(x_voiture,y_voiture)
        intersect_vert_c6(x_voiture,y_voiture)
        intersect_vert_c7(x_voiture,y_voiture)
        intersect_vert_c8(x_voiture,y_voiture)
        tableau_intersect.append(l)

    v1=vector(l[0][0]-x_voiture,l[0][1]-y_voiture)
    v2=vector(l[1][0]-x_voiture,l[1][1]-y_voiture)

    angle=(theta-angle_voiture)%180
    if angle>90:
        angle=angle-180
    if (angle==90):
        vect_test=vector(cos(radians(angle_voiture+10)),sin(radians(angle_voiture+10)))#vecteur pour tester pour l'angle =90 ou -90
        if (produit_scalaire(v1,vect_test)>0):
            tab=[angle,v1.norm()/50]
            tab_lidar.append(tab)
            tab=[-angle,v2.norm()/50]
            tab_lidar.append(tab)
        else:
            tab=[angle,v2.norm()/50]
            tab_lidar.append(tab)
            tab=[-angle,v1.norm()/50]
            tab_lidar.append(tab)             
    else:
        if (produit_scalaire(v1,vect_direction)>0):
            tab=[angle,v1.norm()/50]
            tab_lidar.append(tab)
        else:
            tab=[angle,v2.norm()/50]
            tab_lidar.append(tab)

    

dessiner_voiture(x_voiture,y_voiture,angle_voiture,25,10)
turtle.tracer(True)
turtle.up()  #Lève le crayon
turtle.goto(x_voiture,y_voiture)
turtle.circle(0,angle_voiture)
turtle.down()


print("x_voiture: ",x_voiture,"        y_voiture: ",y_voiture,"        angle_voiture :",angle_voiture)

#affichage de tableau ou on met les points d'intersections de la droite de pente tan(theta) passant par les coordonnees de la voiture  avec la piste
# for k in range(nbr):
#     print("theta=",(180/nbr)*k," : ")
#     print(tableau_intersect[k])

print("Affichage du tableau de LiDAR: ce tableau donne [angle par rapport vecteur de direction de la voiture(en degre) , distance entre la voiture et le mur(en metre)]")    
for k in range(len(tab_lidar)):
    print(tab_lidar[k])


turtle.exitonclick()


