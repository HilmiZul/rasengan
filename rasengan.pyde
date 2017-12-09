w = 500
h = 500
x = w/2
y = h/2
<<<<<<< HEAD
radius_inti = 0
radius_angin = 0
rasengan = False

=======
ri = 0
ra = 0
>>>>>>> e2a3c3d49397dec9a70099285f051844ba940230
def setup():
    size(w, h)
    background(0, 0, 0)
    
<<<<<<< HEAD
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
=======
def draw():
    global x,y,ri,ra
    background(0)
    
    strokeWeight(1)
    stroke(100, 200, 255)
    #fill(100, 200, 255)
    noFill()
    
    if ri < 50:
        ri = ri + 0.3

    if ra < 100:
        ra = ra + 1
    for n in range(0, 100):
        ellipse(x, y, random(ra+50), random(ra+50))
        
    # inti rasengan
    fill(100, 255, 255)
    ellipse(x, y, ri, ri)
    
    
    
    
    
>>>>>>> e2a3c3d49397dec9a70099285f051844ba940230
