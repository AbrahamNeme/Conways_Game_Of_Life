import pygame
import sys
import random
import copy

# ----------------------------KLASSE-------------------------------- #

class Secondwindow:                                                                         #Klasse für die Erzeugung eines Rasters.
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = 1440, 640
        self.surface = pygame.Surface((self.width, self.height))                            #Erzeugt eine Oberfläche
        self.grid = [[Cell(self.surface, x, y) for x in range(45)] for y in range(20)]      #Ein zweidimensionales Array wird erstellt 
        for row in self.grid:
            for element in row:
                element.identifyneighbours(self.grid)                                       #Alle Nachbarzellen jeder Zelle werden identifiziert / Zeile 72
      
    def draw(self):
        self.surface.fill((51, 183, 255))                                                   #die Oberfläche wird hellblau gefärbt
        for row in self.grid:
            for element in row:
                element.draw()                                                              #Methode der Klasse "Cells" / Zeile 63
        self.screen.blit(self.surface, (self.x, self.y))                                    #Zeichnet eine Oberfläche auf das Fenster
    
    def rules(self):                                                                        #Methode, die die Spielregeln anwendet
        updatedgrid = copy.copy(self.grid)                                                  #Eine Kopie des Rasters wird erstellt
        for row in self.grid:
            for element in row:
                element.aliveneighbours()                                                   #Die lebenden Nachbarn jerder Zelle werden gezählt / Zeile 88
        
        for y, row in enumerate(self.grid):                                                 #"enumerate" funktioniert wie ein Zähler
            for x, element in enumerate(row):
                if element.status:                                                          #Wenn die Zelle lebendig ist
                    if element.livingneighbours < 2:
                        updatedgrid[y][x].status = False
                    if element.livingneighbours == 2 or element.livingneighbours == 3:
                        updatedgrid[y][x].status = True
                    if element.livingneighbours > 3:
                        updatedgrid[y][x].status = False                                    #der Zellstatus wird über einen Index geändert
                else:
                    if element.livingneighbours == 3:
                        updatedgrid[y][x].status = True
        self.grid = updatedgrid
    
    def reset(self):                                                                        #Methode, die den Status aller Zellen auf tot ändert
        for row in self.grid:
            for element in row:
                element.status = False

# ----------------------------KLASSE-------------------------------- #

class Cell:                                                                                 #Klasse zur Erzeugung von Zellen
    def __init__(self, surftoplace, xpos, ypos):
        self.surftoplace = surftoplace
        self.xpos = xpos
        self.ypos = ypos
        self.status = False
        self.livingcell = pygame.image.load('cell{}.png'.format(random.randint(1,3)))       #Lädt ein zufälliges Bild für die Zelle
        self.size = 32
        self.cellsurface = pygame.Surface((self.size, self.size))                           #Erzeugt eine Oberfläche
        self.neighbourslist = []
        self.livingneighbours = 0
    
    def draw(self):
        if self.status:                                                                     #Wenn die Zelle lebendig ist
            self.cellsurface.fill((255, 255, 255))                                          #die Oberfläche ist weiß gefärbt
            self.cellsurface.blit(self.livingcell, (0, 0))                                  #Zeichnet das Bild auf die Zelloberfläche
        else:
            self.cellsurface.fill((0, 0, 0))                                                #die Oberfläche wird schwarz gefärbt
            pygame.draw.rect(self.cellsurface, (51, 183, 255), (2, 2, 28, 28))              #Zeichnet ein kleineres Rechteck für die Ränder
        self.surftoplace.blit(self.cellsurface, (self.xpos*self.size, self.ypos*self.size)) #Zeichnet die Zelleoberfläche auf den Spielbereich
    
    def identifyneighbours(self, grid):                                         # Methode, die alle Nachbarzellen einer Zelle identifiziert
        neighbours = [[self.xpos+1, self.ypos], [self.xpos-1, self.ypos],       
                     [self.xpos, self.ypos+1], [self.xpos, self.ypos-1],        #(-1,-1)(0,-1)(+1,-1)
                     [self.xpos+1, self.ypos+1], [self.xpos+1, self.ypos-1],    #(-1,0) (0,0) (+1,0)
                     [self.xpos-1, self.ypos+1], [self.xpos-1, self.ypos-1]]    #(-1,+1)(0,+1)(+1,+1)
        for element in neighbours:
            if element[0] < 0:                                                  #element[0] = -1
                element[0] += 45                                                #element[0] = (-1 + 45) = 44
            if element[0] > 44:           
                element[0] -= 45                                                #element[1] = 20
            if element[1] < 0:                                                  #element[1] = (20 - 20) = 0
                element[1] += 20
            if element[1] > 19:                                                 #.append(grid[44][0])
                element[1] -= 20
            self.neighbourslist.append(grid[element[1]][element[0]])            #Hängt ein Element an die Nachbarliste an

    def aliveneighbours(self):                                                  #Zählt die lebenden Nachbarn einer Zelle
        alive = 0
        for element in self.neighbourslist:
            if element.status:                                                  #Wenn die Zelle lebendig ist
                alive += 1                                                      #Addiert 1 zu der Variable "alive"
        self.livingneighbours = alive

# ----------------------------KLASSE-------------------------------- #

class Button():                                                                 #Klasse zur Erstellung von Schaltflächen
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('comicsans', 30)                        #Funktion zur Auswahl der Schriftart
    
    def mouseoverB(self, pos):
        if pos[0] > self.x and pos[0] < self.x+self.width:                      #Gibt "Wahr" zurück, wenn der Zeiger sich innerhalb der Schaltfläche befindet,
            if pos[1] > self.y and pos[1] < self.y+self.height:                 #und "Falsch", wenn nicht
                return True
        else:
            return False
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))              #Funktion zum Zeichnen eines Rechtecks
        pygame.draw.rect(screen, self.color, (self.x+2, self.y+2, self.width-4, self.height-4))     #Zeichnet ein kleineres Rechteck für die Ränder
        text = self.font.render(self.text, 1, (0, 0, 0))                                            #Funktion zum Anwenden der Schriftart und -größe auf den Text
        screen.blit(text, (self.x+(self.width//2-text.get_width()//2), self.y+(self.height//2-text.get_height()//2)))   #Zeichnet den Text auf die Schaltfläche
        
# ---------------------SEKUNDÄRE FUNKTIONEN------------------------- #

def mouseongamearea(position):                                                  # Tuple --> [x, y]
    if position[0] > 40 and position[0] < 1480:                                 #Gibt "Wahr" zurück, wenn der Zeiger sich innerhalb des Raster-Bereichs befindet,
        if position[1] > 160 and position[1] < 800:                             #und "Falsch", wenn nicht
            return True
    else:
        return False

def clickcell(position):
    pos = [((position[0]-40)//32), ((position[1]-160)//32)]
    secondwin.grid[pos[1]][pos[0]].status = True                                #Ändert den Zellstatus auf lebendig

def unclickcell(position):                                                      #pos = [((55-40)//32), ((180-160)//32)]
    pos = [((position[0]-40)//32), ((position[1]-160)//32)]                     #pos =[0, 0]
    secondwin.grid[pos[1]][pos[0]].status = False                               #secondwin.grid[0][0].status = False 

def checkstatus(position):
    pos = [((position[0]-40)//32), ((position[1]-160)//32)]
    check = secondwin.grid[pos[1]][pos[0]].status                               #Speichert den aktuellen Status der Zelle in einer Variablen
    return check                                                                # Gibt den Wert der Variable "Check" zurück

def rungame():
    global Gamestatus
    Gamestatus = 'start'

def pausegame():
    global Gamestatus                                                           #Bezieht sich auf die Variable "Gamestatus" auf Zeile 223
    Gamestatus = 'pause'                                                        #Ändert den Wert der Variable

def resetgame():
    global Gamestatus
    Gamestatus = 'reset'
    secondwin.reset()                                                           #Ändert den Status aller Zellen auf tot / Methode der Klasse "Secondwindow" / Zeile 44
                                                                     
# ------------------------HAUPT FUNKTIONEN-------------------------- #

def events():
    for event in pygame.event.get():
        mousepos = pygame.mouse.get_pos()                                       #Funktion, die die Position des Zeigers erhält / Gibt eine Tuple zurück [x,y]
        global Run                                                              #Bezieht sich auf die Variable "Run" auf Zeile 224
        if event.type == pygame.KEYDOWN:                                        #Wenn das Ereignis das Drücken einer Taste entspricht
            if event.key == pygame.K_ESCAPE:                                    #Wenn das Ereignis das Drücken der Escape-taste entspricht
                Run = False
        if event.type == pygame.QUIT:                                           #Wenn man auf das rote Viereck mit dem X klickt
            Run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:          #Wenn das Ereignis das Drücken der linken Maustaste entspricht
            if mouseongamearea(mousepos):                                       #Wenn der Zeiger sich über dem Raster befindet / Zeile 122
                clickcell(mousepos)                                             #Ändert den Zellstatus auf lebendig / Zeile 129
            
            if startB.mouseoverB(mousepos):                                     #if mousepos[0] > 280 and mousepos[0] < 432 :
                rungame()                                                       #if mousepos[1] > 109 and mousepos[1] < 151:
               
            if pauseB.mouseoverB(mousepos):                                     #rungame() Zeile 142
                pausegame()                                                     #pausegame() Zeile 146
                                                                    
            if resetB.mouseoverB(mousepos):                                     #resetgame() Zeile 150
                resetgame()                                                     
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:          #Wenn das Ereignis das Drücken der rechten Maustaste entspricht
            if checkstatus(mousepos) and mouseongamearea(mousepos):             #Wenn die Zelle lebendig ist und der Zeiger sich über dem Raster befindet
                unclickcell(mousepos)                                           #Ändert den Zellstatus auf tot / Zeile 133
        
        if event.type == pygame.MOUSEMOTION:                                    #Wenn das Ereignis einer Mausbewegung entspricht
            if startB.mouseoverB(mousepos):
                startB.color = (0, 190, 50)
            else:
                startB.color = (0, 255, 0)
            if pauseB.mouseoverB(mousepos):                                     #Wenn der Zeiger sich über der Schaltfläche befindet / Zeile 107
                pauseB.color = (50, 0, 190)                                     #Die Farbe der Schaltfläche wechselt zu einer helleren Farbe
            else:
                pauseB.color = (0, 0, 255)                                      #Ist die Bedingung nicht erfüllt, kehrt die Schaltfläche zu ihrer ursprünglichen Farbe zurück
            if resetB.mouseoverB(mousepos):
                resetB.color = (190, 50, 0)
            else:
                resetB.color = (255, 0, 0)

def draw():                                                             
    window.blit(background, (0, 0))                                             #Zeichnet das zuvor geladene Bild
    secondwin.draw()                                                            #Draw-Methode der Klasse "Secondwindow" / Zeile 17
    startB.draw(window)                                                         #Zeichnet der Start-Schaltfläche
    pauseB.draw(window)                                                         #Zeichnet der Pause-Schaltfläche / Draw Methode der Klasse "Button" / Zeile 114
    resetB.draw(window)                                                         #Zeichnet der Reset-Schaltfläche
    keys.draw(window)                                                           #Zeichnet die Anweisungstabelle
                                                                     
# -----------------------OBJEKTE + SCHLEIFE------------------------- #

pygame.init()                                                                   #Pygame wird initializiert
Width, Height = 1520, 800
window = pygame.display.set_mode((Width, Height))                               #Spielfenster wird erzeugt
pygame.display.set_caption("CONWAY'S GAME OF LIFE")                             #Fügt die Fensterunterschrift hinzu
winicon = pygame.image.load('icon.png')                                         #Lädt und speichert ein Bild in eine Variable
pygame.display.set_icon(winicon)                                                #Fügt dem Fenster ein Symbol hinzu
background = pygame.image.load('background.jpg')                                #Lädt und speichert ein Bild in eine Variable
clock = pygame.time.Clock()
secondwin = Secondwindow(window, 40, 160)                                       #Erzeugt ein Objekt der Klasse "Secondwindow" / Zeile6
startB = Button(281, 110, 150, 40, (0, 255, 0), 'Start')                        #Erzeugt ein Objekt der Klasse "Button" / Zeile 97
pauseB = Button(687, 110, 150, 40, (0, 0, 255), 'Pause')                        #" "
resetB = Button(1093, 110, 150, 40, (255, 0, 0), 'Reset')                       #" "
keys = Button(281, 50, 963, 40, (190, 190, 190), 'Leftclick: Select cell  /  Rightclick: Deselect cell  /  Esc: Exit game')

Fps = 15
Gamestatus = 'reset'                                                            #Variable zur Differenzierung des aktuellen Spielzustands
Run = True
while Run:
    if Gamestatus == 'reset':
        events()                                                                #Überprüft alle Ereignisse / Zeile 157
        draw()                                                                  #Zeichnet alle Elemente im Fenster / Zeile 198
    if Gamestatus == 'start':
        events()
        secondwin.rules()                                                       #Wendet die Spielregeln an / Methode der Klasse "Secondwindow" /Zeile 24
        draw()
    if Gamestatus == 'pause':
        events()
        draw()
    
    pygame.display.update()                                                     #Funktion zur Aktualisierung der Bildschirmanzeige
    clock.tick(Fps)                                                             #Reguliert die Geschwindigkeit des Spiels / Bilder pro Sekunde

pygame.quit()                                                                   #Pygame wird beendet
sys.exit()                                                                      #Erlaubt das Verlassen von Python
