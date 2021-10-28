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
showTriangle = 0

def mousePressed():
    global clickX
    global clickY
    global showTriangle

    clickX = mouseX
    clickY = mouseY
    showTriangle = 1
    
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
    global showTriangle
 
    showTriangle = 0   
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
    global img
    
    size(1500, 700)
    background(255,255,255)
    frameRate(25)
    img = loadImage("Archer.png")

def draw():
    global gravity, showTriangle, start,  img
    global clickX, clickY, speedX, speedY, projX, projY
    
    print speedX, speedY, start
    
    image(img, 10, 600, 150, 150/1.6375)
    if showTriangle == 1:
        background(255,255,255)
        triangle(clickX, clickY, speedX*10 + clickX, speedY*10 + clickY, speedX*10 + clickX + 10, speedY*10 + clickY - (10*speedX/speedY))

        
    if projY > 650:
            start = 0
    if start == 1:
        circle(projX, projY, 10)
        projX = projX + speedX
        projY = projY + speedY
        speedY += gravity
    
