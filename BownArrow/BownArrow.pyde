from Zielscheibe import zielScheibe
from TrefferBerechnung import trefferBerechnung
from AnzeigeWerte import werteAnzeige
from Lineal import lineal

start = 0
#Position des Projektils
projX = 50
projY = 450
#Tempo des Projektils
speedX = 0.0
speedY = 0.0
speedXold = 0.0
speedYold = 0.0
#Deltaberechnung
clickX = 0.0
clickY = 0.0
releaseX = 0.0
releaseY = 0.0
#Gravitation
gravity = 0.981
showTriangle = 0
treffer = 0
fth = 0 #frame bis treffer (frames to hit)
zielX = random(500,1400)
zielY = random(50,650)


def mousePressed():
    global showTriangle
    global clickX, clickY

    clickX = mouseX
    clickY = mouseY
    showTriangle = 1
    
def mouseReleased():
    global start, showTriangle, fth, treffer, zielX, zielY
    global clickX, clickY, speedX, speedY, projX, projY, speedXold, speedYold
 
    showTriangle = 0   
    projY = 650
    projX = 50
    
    start = 1
    releaseX = mouseX
    releaseY = mouseY
    speedX = (releaseX - clickX) / 10
    speedY = (releaseY - clickY) / 10
    #limitiert geschwindigkeit in Xrichtung. Yrichtung bleibt frei, ist aber schwieriger zu zielen
    if speedX > 25:
        speedX = 25.0
    speedXold = speedX
    speedYold = speedY
    treffer, fth = trefferBerechnung(50.0,zielX,650.0,zielY,gravity,speedX,speedY, 15)
    fth = fth + frameCount +1

def setup():
    global img, bimg
    
    size(1500, 700)
    background(255,255,255)
    frameRate(25)
    img = loadImage("Archer.png")
    bimg = loadImage("Background.png")

def draw():
    global gravity, showTriangle, start,  img, bimg, treffer, fth, zielX, zielY
    global clickX, clickY, speedX, speedY, projX, projY, speedXold, speedYold

    print speedX, speedY, start

    image(bimg,0,0)
    if showTriangle == 1:
        tx2 = 50+ mouseX - clickX
        ty2 = 650 + mouseY - clickY
        if tx2 > 200:
            tx2 = 200
        fill(0,0,0)
        triangle(50, 650, tx2, ty2, tx2 + 5, ty2 + 5)

        
    image(img, 10, 600, 150, 150/1.6375)
    zielScheibe(zielX,zielY)
    werteAnzeige(0, sqrt(sq(speedXold)+sq(speedYold)), speedXold, speedYold)
    lineal()
                    
    if projY > 650:
            start = 0
    if (start == 1 and treffer==0) or (start==1 and treffer==1 and frameCount<fth):
        fill(255,255,255)
#Debug Linien zur Anzeige der y Werte des Trefferbereichs (zu einem Zeitpunkt in de das Ziel statisch generiert wurde
#        line(600,315,650,315)
#        line(600,285,650,285)
        circle(projX, projY, 10)
        projX = projX + speedX
        projY = projY + speedY
        speedY += gravity
    if treffer==1 and frameCount-80>=fth:
        zielX = random(500,1400)
        zielY = random(50,650)
        treffer = 2
        
