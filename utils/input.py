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
        #player movement input, change animation of walking/direction
        #when no keys pressed, all else statements will execute... I need an easier
        #way to handle idle animations.
        #up
        if pressedKeys[self.bindings['move-up']]:
            # self.entity.traits["walk-up"].move = True
            # self.entity.traits["walk-up"].direction_y = -1
            self.entity.begin_moving("walk-up")
            
        # else:
        #     self.entity.traits["walk-up"].move = False
        #     self.entity.traits["walk-up"].direction_y = 0
        #down 
        if pressedKeys[self.bindings['move-down']]:
            self.entity.traits["walk-down"].move = True
            self.entity.traits["walk-down"].direction_y = 1
        else: 
            self.entity.traits["walk-down"].move = False
            self.entity.traits["walk-down"].direction_y = 0
            print("Idling")

        #left
        if pressedKeys[self.bindings['move-left']] and not pressedKeys[self.bindings['move-right']]:
            self.entity.traits["walk-left"].move = True
            self.entity.traits["walk-left"].direction_x = -1
        else:
            self.entity.traits["walk-left"].move = False
            self.entity.traits["walk-left"].direction_x = 0

        #right
        if pressedKeys[self.bindings['move-right']] and not pressedKeys[self.bindings['move-left']]:
            self.entity.traits["walk-right"].move = True
            self.entity.traits["walk-right"].direction_x = 1
        else:
            self.entity.traits["walk-right"].move = False
            self.entity.traits["walk-right"].direction_x = 0
            

        

    def quitEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            
            
