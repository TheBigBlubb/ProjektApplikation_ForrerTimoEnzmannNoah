def werteAnzeige(score,speed,speedXold, speedYold):
    fill(255,255,255)
    rect(0, 0, 300, 150) 
    textSize(20)
    fill(0,0,0)
    text("Treffer: " + str(score) + "\n" + "GeschwindigkeitX: " + str(speedXold) + " m/s" + "\n" + "GeschwindigkeitY: " + str(speedYold*-1) + " m/s" + "\n" + "Geschwindigkeit:   " + str(int(speed)) + " m/s" ,20,30)

    
