import turtle

def tree(t,length,order):
    if length < (length/order):
           return       
    t.forward(length)      
    t.left(45)         
    tree(t,length * 0.5,length/order)      
    t.right(90)         
    tree(t,length * 0.5,length/order)      
    t.left(45)          
    t.backward(length)       
    return

screen = turtle.Screen ( ) 
tip = turtle.Turtle() 
tip.shape ("turtle") 
tip.speed (0)   
  
tip.left(90)  # vertical start
tree (tip, 200, 5)
tip.exitonclick()