def setup():
    size(1000,1000)

    
def draw():
    line(mouseX,mouseY,500,500)
    print(mouseX,mouseY,mousePressed)
    if mousePressed:
        rect(width/2,height/2,250,250)
        
        
    

    
    
    
