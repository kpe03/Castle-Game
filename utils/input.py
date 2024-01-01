import pygame

class Input:
    def __init__(self, entity):
        #get current keys/events
        self.x_move = 0
        self.y_move = 0
        #dictionary for key bindings
        self.bindings = {
            'move-up': pygame.K_w,
            'move-down': pygame.K_s,
            'move-left': pygame.K_a,
            'move-right': pygame.K_d,
            'diagonal-ur': pygame.K_w or pygame.K_d
        }
        self.entity = entity

    def checkInput(self):
        events = pygame.event.get() 
        self.keysInput()
        self.quitEvents(events)

    def keysInput(self):
        pressedKeys = pygame.key.get_pressed()

        #player movement input
        #up
        if pressedKeys[self.bindings['move-up']] and not pressedKeys[self.bindings['move-down']]:
            self.entity.traits["walk-up"].move = True
        else: 
            self.entity.traits["walk-up"].move = False
        #down 
        if pressedKeys[self.bindings['move-down']] and not pressedKeys[self.bindings['move-up']]:
            self.entity.traits["walk-down"].move = True
        else: 
            self.entity.traits["walk-down"].move = False
        #left
        if pressedKeys[self.bindings['move-left']] and not pressedKeys[self.bindings['move-right']]:
            self.entity.traits["walk-left"].move = True
        else:
            self.entity.traits["walk-left"].move = False
        #right
        if pressedKeys[self.bindings['move-right']] and not pressedKeys[self.bindings['move-left']]:
            self.entity.traits["walk-right"].move = True
        else:
            self.entity.traits["walk-right"].move = False

    
            
        

    def quitEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            
            
