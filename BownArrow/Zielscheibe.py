#an der eingegeben Position, wird eine Zielscheibe mit Durchmesser 30px generiert
def zielScheibe(xPos,yPos):
    stroke(0,0,0)
    fill(255,0,0)
    circle(xPos,yPos,30)
    fill(255,255,255)
    circle(xPos,yPos,20)
    fill(255,0,0)
    circle(xPos,yPos,10)
