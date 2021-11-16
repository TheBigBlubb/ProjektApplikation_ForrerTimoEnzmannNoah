def werteAnzeige(score,speed,speedXold, speedYold):
    fill(255,255,255)
    rect(0, 0, 200, 150) 
    textSize(20)
    fill(0,0,0)
    text(str(score) + "\n" + str(speedXold) + "\n" + str(speedYold) + "\n" + str(int(speed)),20,30)

    
