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
            'diagonal-ur': pygame.K_w and pygame.K_d,
            'diagonal-ul': pygame.K_w and pygame.K_a,
        }
        self.entity = entity
        self.lastKeyStroke = self.bindings['move-down'] #by default, idle down
    

    def checkInput(self):
        events = pygame.event.get() 
        self.keysInput()
        self.quitEvents(events)

    def keysInput(self):
        pressedKeys = pygame.key.get_pressed()
   
        #works but feels super clunky -----------------------------
        #idea: update the move trait of entity in input
        #(instead of updating all the traits at once??)
        #downs
        if pressedKeys[self.bindings['move-down']]:
            self.entity.traits["walk-down"].move = True
            self.entity.traits["walk-down"].update()
        else: 
            self.entity.traits["walk-down"].move = False
        #up
        if pressedKeys[self.bindings['move-up']]:
            self.entity.traits["walk-up"].move = True
            self.entity.traits["walk-up"].update()
        else: 
            self.entity.traits["walk-up"].move = False
        #left
        if pressedKeys[self.bindings['move-left']]: #and not pressedKeys[self.bindings['move-right']]:
            self.entity.traits["walk-left"].move = True
            self.entity.traits["walk-left"].update()
        else:
            self.entity.traits["walk-left"].move = False

        #right
        if pressedKeys[self.bindings['move-right']]: #and not pressedKeys[self.bindings['move-left']]:
            self.entity.traits["walk-right"].move = True
            self.entity.traits["walk-right"].update()
        else:
            self.entity.traits["walk-right"].move = False


    def quitEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            
            
