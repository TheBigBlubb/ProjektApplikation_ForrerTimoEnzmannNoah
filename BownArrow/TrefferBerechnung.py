def trefferBerechnung(xstart,xziel,ystart,yziel,gravity,speedx, speedystart,toleranz):
    frames = 0.001
    y=0.001
    treffer = 0
    if speedx == 0:
        speedx=1
    frames = (xziel-xstart)/speedx
    y = ystart+(speedystart+speedystart+frames*gravity)/2*frames
    if y <= (yziel+toleranz+15) and y >= (yziel-toleranz-15):
        treffer = 1
    else:
        treffer = 0
    return treffer, frames
        
