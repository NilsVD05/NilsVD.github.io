import pygame
pygame.init() 
 
win = pygame.display.set_mode((1300,650))  
pygame.display.set_caption("First Game") 

x = 100
y = 100
width = 80
height = 80
vel = 5
isJump = False 
jumpCount = 10 
run = True 

 
while run:   
    pygame.time.delay(1)  

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:          
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1300 - vel - width: 
        x += vel 

    if not(isJump):
        if keys[pygame.K_UP]    and y > vel: 
            y -= vel
        if keys[pygame.K_DOWN]  and y < 650 - height - vel: 
            y += vel
        if keys[pygame.K_SPACE]:    
          isJump = True 
        if keys[pygame.K_q]:    
           win.fill((0,0,0)) 

    if isJump:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
             jumpCount = 10  
             isJump = False   
    

    
    pygame.draw.rect(win, (250,130,0), (x, y, width, height))  
    
    pygame.display.update()


pygame.quit()