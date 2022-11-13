x=100

def setup():
   size(500,500)
def draw():
   global x
   fill(0,x)
   triangle(250,100,200,260,300,260)
   x=x+10
