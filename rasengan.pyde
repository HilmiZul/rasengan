w = 500
h = 500
x = w/2
y = h/2
ri = 0
ra = 0
def setup():
    size(w, h)
    background(0, 0, 0)
    
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
    
    
    
    
    