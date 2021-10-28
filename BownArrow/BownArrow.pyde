start = 0
#Position des Projektils
projX = 50
projY = 450
#Tempo des Projektils
speedX = 1
speedY = -10
#deltaberechnung
clickX = 0
clickY = 0
releaseX = 0
releaseY = 0
#gravitation
gravity = 1

def mousePressed():
    global clickX
    global clickY

    clickX = mouseX
    clickY = mouseY
    
def mouseReleased():
    global releaseX
    global releaseY
    global clickX
    global clickY
    global speedX
    global speedY
    global start
    global projX
    global projY

    projY = 650
    projX = 50
    
    start = 1
    background(255,255,255)
    releaseX = mouseX
    releaseY = mouseY
    speedX = (releaseX - clickX) / 10
    speedY = (releaseY - clickY) / 10
    #limitier geschwindigkeit in Xrichtung. Yrichtung bleibt frei, ist aber schwieriger zu zielen
    if speedX > 20:
        speedX = 20
    

def setup():
    size(1500, 700)
    background(255,255,255)
    frameRate(25)

def draw():
    global gravity
    global start
    global speedX
    global speedY
    global projX
    global projY
    
    print speedX, speedY, start
    
    circle(50, 650, 30)
    if projY > 650:
            start = 0
    if start == 1:
        circle(projX, projY, 10)
        projX = projX + speedX
        projY = projY + speedY
        speedY += gravity
        
