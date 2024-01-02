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
        self.idleDirection = "walk-down"
        self.keysHeld = None #last key pressed

    def setUpInput(self):
        self.keysHeld = pygame.key.get_pressed()

    def checkInput(self):
        events = pygame.event.get() 
        self.keysInput()
        self.quitEvents(events)

    def keysInput(self):
        pressedKeys = pygame.key.get_pressed()
        
        
        if True in pressedKeys:
            #downs
            if pressedKeys[self.bindings['move-down']]:
                self.entity.traits["walk-down"].move = True
                self.entity.traits["walk-down"].update()
            #up
            if pressedKeys[self.bindings['move-up']]:
                self.entity.traits["walk-up"].move = True
                self.entity.traits["walk-up"].update()
            #left
            if pressedKeys[self.bindings['move-left']]: 
                self.entity.traits["walk-left"].move = True
                self.entity.traits["walk-left"].update()
            #right
            if pressedKeys[self.bindings['move-right']]: 
                self.entity.traits["walk-right"].move = True
                self.entity.traits["walk-right"].update()

        #todo: diagonal key strokes (using keysPressed and keysHeld)
                
        #find last keystroke and do idle aniamtion
        else:
            self.entity.traits["walk-down"].move = False
            self.entity.traits["walk-up"].move = False
            self.entity.traits["walk-left"].move = False
            self.entity.traits["walk-right"].move = False
            #set all move of traits to false. then, set the idle animation
            if self.keysHeld[self.bindings['move-down']]:
                self.idleDirection = "walk-down"
            elif self.keysHeld[self.bindings['move-up']]:
                self.idleDirection = "walk-up"
            elif self.keysHeld[self.bindings['move-left']]:
                self.idleDirection = "walk-left"
            elif self.keysHeld[self.bindings['move-right']]:
                self.idleDirection = "walk-right"
            self.entity.traits[self.idleDirection].update()
            print("Idle direction:", self.idleDirection)

        self.keysHeld = pressedKeys #update the keysHeld list


    def quitEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            
            
