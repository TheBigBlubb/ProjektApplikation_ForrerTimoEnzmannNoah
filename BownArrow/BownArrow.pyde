from Zielscheibe import zielScheibe
from TrefferBerechnung import trefferBerechnung

start = 0
#Position des Projektils
projX = 50
projY = 450
#Tempo des Projektils
speedX = 1
speedY = -10
#Deltaberechnung
clickX = 0
clickY = 0
releaseX = 0
releaseY = 0
#Gravitation
gravity = 1
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
    global clickX, clickY, speedX, speedY, projX, projY
 
    showTriangle = 0   
    projY = 650
    projX = 50
    
    start = 1
    #background(255,255,255)
    releaseX = mouseX
    releaseY = mouseY
    speedX = (releaseX - clickX) / 10
    speedY = (releaseY - clickY) / 10
    #limitiert geschwindigkeit in Xrichtung. Yrichtung bleibt frei, ist aber schwieriger zu zielen
    if speedX > 25:
        speedX = 25
    treffer, fth = trefferBerechnung(50,zielX,650,zielY,gravity,speedX,speedY, 15)
    fth = fth + frameCount +1

def setup():
    global img
    
    size(1500, 700)
    background(255,255,255)
    frameRate(25)
    img = loadImage("Archer.png")

def draw():
    global gravity, showTriangle, start,  img, treffer, fth, zielX, zielY
    global clickX, clickY, speedX, speedY, projX, projY

    print speedX, speedY, start

    
    if showTriangle == 1:
        background(255,255,255)
        tx2 = 50+ mouseX - clickX
        ty2 = 650 + mouseY - clickY
        if tx2 > 200:
            tx2 = 200
        fill(0,0,0)
        triangle(50, 650, tx2, ty2, tx2 + 5, ty2 + 5)

        
    image(img, 10, 600, 150, 150/1.6375)
    zielScheibe(zielX,zielY)
        
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
        
