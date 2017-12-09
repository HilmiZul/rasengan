w = 500
h = 500
x = w/2
y = h/2
radius_inti = 0
radius_angin = 0
rasengan = False

def setup():
    size(w, h)
    background(0, 0, 0)
    
def mousePressed():
    global rasengan
    rasengan = True
    
def draw():
    global x,y,radius_inti,radius_angin
    background(0)
    
    if rasengan:
        strokeWeight(1)
        stroke(100, 200, 255)
        #fill(100, 200, 255)
        noFill()
        
        if radius_angin < 100:
            radius_angin = radius_angin + 1
        for n in range(0, 100):
            ellipse(mouseX, mouseY, random(radius_angin+50), random(radius_angin+50))
            
        # inti rasengan
        if radius_inti < 50:
            radius_inti = radius_inti + 0.3
    
        fill(100, 255, 255)
        ellipse(mouseX, mouseY, radius_inti, radius_inti) 
