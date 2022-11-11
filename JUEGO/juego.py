import os
import random
import sys
import turtle
#Marcador
score = 0
high_score = 0
#Variables Iniciales
contador = 0

 #Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("Orange")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0", align = "center", font =("Courier", 24, "normal"))


#Funcion busca nuestro folder
def resource_path(relative_path):
    try:
       base_path = sys._MEIPASS
    except Exception:
       base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Configuracion de la ventana
wn=turtle.Screen()
wn.title("Juego de Halloween Santiago Carvajal y Santiago Galindo")
wn.setup(width = 600, height = 600)
wn.bgcolor('white')

#Imagenes del Juego
image = resource_path("player.gif")
imghamburguer =resource_path("hamburguer.gif")
imgh1 = resource_path("homen1.gif")
imgh2 = resource_path("homen2.gif")
imgh3 = resource_path("homen3.gif")
imgh4 = resource_path("homen4.gif")
imgZOM = resource_path("ZOM.gif")

#Cargar las imagenes
wn.addshape (image)
wn.addshape(imghamburguer)
wn.addshape(imgh1)
wn.addshape(imgh2)
wn.addshape(imgh3)
wn.addshape(imgh4)
wn.addshape(imgZOM)

#Cabeza del Jugador
cabeza = turtle.Turtle()
cabeza.speed (0)
cabeza.shape(image)
cabeza.penup()
cabeza.goto(120,-150)

#Cuerpo del Jugador
cuerpo =turtle.Turtle()
cuerpo.speed (0)
cuerpo.shape(imgh1)
cuerpo.penup()
cuerpo.goto(125,-220)
time=3


#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape(imghamburguer)
comida.penup()
comida.goto(-100,80)
score += 1


         
if score > high_score: 
           high_score = score

#zombie
Zombie = turtle.Turtle()
Zombie.speed(0)
Zombie.shape(imgZOM)
Zombie.penup()
Zombie.goto(100,-40)

#Funciones 
def arriba():
    cabeza.sety(cabeza.ycor()+20)
    cuerpo.sety(cuerpo.ycor()+20)

def abajo():
    cabeza.sety(cabeza.ycor()-20)
    cuerpo.sety(cuerpo.ycor()-20)

def izquierda():
    cabeza.setx(cabeza.xcor()-20)
    cuerpo.setx(cuerpo.xcor()-20)

def derecha():
    cabeza.setx(cabeza.xcor()+20)
    cuerpo.setx(cuerpo.xcor()+20)

#Escuchar Teclado
wn.listen()
wn.onkeypress (arriba, "Up")
wn.onkeypress (abajo, "Down")
wn.onkeypress (izquierda, "Left")
wn.onkeypress (derecha, "Right")

#Mantener mostrando la pantalla
while True:
    wn.update()

    #Interseccion con las comidas
    if cabeza.distance (comida) < 20:
        comida.distance (Zombie) < 10
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        contador=contador + 1
        Zombie = turtle.Turtle()
        Zombie.speed(0)
        Zombie.shape(imgZOM)
        Zombie.penup()
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        Zombie.goto(x,y)
        if cabeza.distance (Zombie) < 20:
            x = random.randint (-280,280)
            y = random.randint(-280,280)
            Zombie.goto(x,y)
            score = 0
            texto.clear()   
            texto.write("Score:  {}".format(score, high_score), 
                 align = "center", font =("Courier", 24, "normal"))
        
        

        

   #Aumentar marcador 
        score += 1
         
        if score > high_score: 
           high_score = score 

        texto.clear()   
        texto.write("Score:  {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
    
    if cabeza.distance (Zombie) < 20:
       x = random.randint (-280,280)
       y = random.randint(-280,280)
       contador=contador + 1
       Zombie.goto(x,y)
       score = 0
       texto.clear()   
       texto.write("Score: {}     High Score: {}".format(score, high_score), 
       align = "center", font =("Courier", 24, "normal"))
       break
        

    

    #Cambiar el cuerpo
    if 1 <= contador < 3: cuerpo.shape(imgh1)
    if 3 <= contador < 5: cuerpo.shape(imgh2)
    if 5 <= contador < 7: cuerpo.shape(imgh3)
    if 9 <= contador: cuerpo.shape (imgh4)


   
        
       
   

   

    