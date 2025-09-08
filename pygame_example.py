import pygame

pygame.init()

gravity = 0.5
velocity_y = 0
speed = 1
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((100, 100, 50, 50))
fullscreen = True
run = True
player_y = float(player.y)

while run:
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, ((255, 255, 255)), player)
    key = pygame.key.get_pressed()
    player_y = float(player.y)
    
    
    if player.bottom < screen_height:
        velocity_y += gravity 
        player.y += velocity_y
    
    if player_y + player.height >= screen_height:
        player_y = screen_height - player.height
        velocity_y = 0
        

    
    if key[pygame.K_w] == True:
        if player.top > 0:
            player.move_ip(0, -velocity_y)
 
    if key[pygame.K_a] == True:
        if player.left > 0:
            player.move_ip(-speed, 0)

    if key[pygame.K_d] == True:
        if player.right < screen_width:
            player.move_ip(speed, 0)
            
    if key[pygame.K_UP] == True:
        if player.top > 0:
            player.move_ip(0, -velocity_y)
    
    if key[pygame.K_LEFT] == True:
        if player.left > 0:
            player.move_ip(-speed, 0)

    if key[pygame.K_RIGHT] == True:
        if player.right < screen_height*2:
            player.move_ip(speed, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if key[pygame.K_ESCAPE] == True or key[pygame.K_q] == True:
        run = False  
        
    if key[pygame.K_f] == True:
       if fullscreen:
           screen = pygame.display.set_mode((screen_width, screen_height))
           fullscreen = False
           pygame.time.delay(200)

       else:
           screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
           fullscreen = True

    pygame.display.update()

pygame.quit()