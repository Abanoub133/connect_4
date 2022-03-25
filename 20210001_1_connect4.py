##importing pygame module
import pygame

##making the game window size and color 
pygame.init()
width = 350
height = 350
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Connect 4")
yellow = (255,255,0)
hor = pygame.image.load(r'C:\Users\GERGES\Desktop\hor.png')
ver = pygame.image.load(r'C:\Users\GERGES\Desktop\ver.png')
xsign = pygame.image.load(r'C:\Users\GERGES\Desktop\x.png')
osign = pygame.image.load(r'C:\Users\GERGES\Desktop\o.png')


player1 = True


###all game positions marked as "e" (empty) till player puts x or o on it
A1 = "e"
A2 = "e"
A3 = "e"
A4 = "e"
A5 = "e"
A6 = "e"
B1 = "e"
B2 = "e"
B3 = "e"
B4 = "e"
B5 = "e"
B6 = "e"



C1 = "e"
C2 = "e"
C3 = "e"
C4 = "e"
C5 = "e"
C6 = "e"
D1 = "e"
D2 = "e"
D3 = "e"
D4 = "e"
D5 = "e"
D6 = "e"



E1 = "e"
E2 = "e"
E3 = "e"
E4 = "e"
E5 = "e"
E6 = "e"
F1 = "e"
F2 = "e"
F3 = "e"
F4 = "e"
F5 = "e"
F6 = "e"

G1 = "e"
G2 = "e"
G3 = "e"
G4 = "e"
G5 = "e"
G6 = "e"
WIN.fill(yellow)
WIN.blit(hor, (0, 50))
WIN.blit(hor, (0, 100))
WIN.blit(hor, (0, 150))
WIN.blit(hor, (0, 200))
WIN.blit(hor, (0, 250))
WIN.blit(hor, (0, 300))
WIN.blit(ver, (50, 50))
WIN.blit(ver, (100, 50))
WIN.blit(ver, (150, 50))
WIN.blit(ver, (200, 50))
WIN.blit(ver, (250, 50))
WIN.blit(ver, (300, 50))

pygame.display.update()

turn = False
## this function is called to change player turns
def player_turn():
    if turn ==False:
        font=pygame.font.SysFont("Times New Roman",30,True,False)
        surface = font.render("Player 1 Turn",True,(255,0,0))
        WIN.blit(surface,(90,5))
        pygame.display.update()
    else:
        font=pygame.font.SysFont("Times New Roman",30,True,False)
        surface = font.render("Player 2 Turn",True,(255,0,0))
        WIN.blit(surface,(90,5))
        pygame.display.update()

## this function is called to say that player 1 won
def result():
    WIN.fill(yellow)
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Player 1 Won !!", True, (255, 0, 0))
    WIN.blit(surface, (90, 90))
    pygame.display.update()

## this function is called to say that player 2 won

def result1():
    WIN.fill(yellow)
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Player 2 Won !!", True, (255, 0, 0))
    WIN.blit(surface, (90, 90))
    pygame.display.update()

## this function is called to say that no one won the game ended with a draw

def result2():
    WIN.fill(yellow)
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Draw!!", True, (255, 0, 0))
    WIN.blit(surface, (90, 90))
    pygame.display.update()

## this function is called to check if there is a winner

def win_check():
    if A1=='x' and A2 =="x" and A3=="x" and A4=="x":
        result()
    elif A1=='o' and A2 =="o" and A3=="o" and A4=="o":
        result1()
    elif A2=='x' and A3 =="x" and A4=="x" and A5=="x":
        result()
    elif A2=='o' and A3 =="o" and A4=="o" and A5=="o":
        result1()
    elif A3=='x' and A4 =="x" and A5=="x" and A6=="x":
        result()
    elif A4=='o' and A4 =="o" and A5=="o" and A6=="o":
        result1()
    elif B1=='x' and B2 =="x" and B3=="x" and B4=="x":
        result()
    elif B1=='o' and B2 =="o" and B3=="o" and B4=="o":
        result1()
    elif B2=='x' and B3 =="x" and B4=="x" and B5=="x":
        result()
    elif B2=='o' and B3 =="o" and B4=="o" and B5=="o":
        result1()
    elif B3=='x' and B4 =="x" and B5=="x" and B6=="x":
        result()
    elif B4=='o' and B4 =="o" and B5=="o" and B6=="o":
        result1()
    ##3
    elif C1=='x' and C2 =="x" and C3=="x" and C4=="x":
        result()
    elif C1=='o' and C2 =="o" and C3=="o" and C4=="o":
        result1()
    elif C2=='x' and C3 =="x" and C4=="x" and C5=="x":
        result()
    elif C2=='o' and C3 =="o" and C4=="o" and C5=="o":
        result1()
    elif C3=='x' and C4 =="x" and C5=="x" and C6=="x":
        result()
    elif C4=='o' and C4 =="o" and C5=="o" and C6=="o":
        result1()
    ##4
    elif D1=='x' and D2 =="x" and D3=="x" and D4=="x":
        result()
    elif D1=='o' and D2 =="o" and D3=="o" and D4=="o":
        result1()
    elif D2=='x' and D3 =="x" and D4=="x" and D5=="x":
        result()
    elif D2=='o' and D3 =="o" and D4=="o" and D5=="o":
        result1()
    elif D3=='x' and D4 =="x" and D5=="x" and D6=="x":
        result()
    elif D4=='o' and D4 =="o" and D5=="o" and D6=="o":
        result1()
    ###5
    elif E1=='x' and E2 =="x" and E3=="x" and E4=="x":
        result()
    elif E1=='o' and E2 =="o" and E3=="o" and E4=="o":
        result1()
    elif E2=='x' and E3 =="x" and E4=="x" and E5=="x":
        result()
    elif E2=='o' and E3 =="o" and E4=="o" and E5=="o":
        result1()
    elif E3=='x' and E4 =="x" and E5=="x" and E6=="x":
        result()
    elif E4=='o' and E4 =="o" and E5=="o" and E6=="o":
        result1()
    ###5
    elif F1=='x' and F2 =="x" and F3=="x" and F4=="x":
        result()
    elif F1=='o' and F2 =="o" and F3=="o" and F4=="o":
        result1()
    elif F2=='x' and F3 =="x" and F4=="x" and F5=="x":
        result()
    elif F2=='o' and F3 =="o" and F4=="o" and F5=="o":
        result1()
    elif F3=='x' and F4 =="x" and F5=="x" and F6=="x":
        result()
    elif F4=='o' and F4 =="o" and F5=="o" and F6=="o":
        result1()
    ###6
    elif G1=='x' and G2 =="x" and G3=="x" and G4=="x":
        result()
    elif G1=='o' and G2 =="o" and G3=="o" and G4=="o":
        result1()
    elif G2=='x' and G3 =="x" and G4=="x" and G5=="x":
        result()
    elif G2=='o' and G3 =="o" and G4=="o" and G5=="o":
        result1()
    elif G3=='x' and G4 =="x" and G5=="x" and G6=="x":
        result()
    elif G4=='o' and G4 =="o" and G5=="o" and G6=="o":
        result1()
    ###7
    elif A1=='x' and B1 =="x" and C1=="x" and D1=="x":
        result()
    elif A1=='o' and B1 =="o" and C1=="o" and D1=="o":
        result1()
    elif B1=='x' and C1 =="x" and D1=="x" and E1=="x":
        result()
    elif B1=='o' and C1 =="o" and D1=="o" and E1=="o":
        result1()
    elif C1=='x' and D1 =="x" and E1=="x" and F1=="x":
        result()
    elif C1=='o' and D1 =="o" and E1=="o" and F1=="o":
        result1()
    elif D1=='x' and E1 =="x" and F1=="x" and G1=="x":
        result()
    elif D1=='o' and E1 =="o" and F1=="o" and G1=="o":
        result1()
    ###
    elif A2=='x' and B2 =="x" and C2=="x" and D2=="x":
        result()
    elif A2=='o' and B2 =="o" and C2=="o" and D2=="o":
        result1()
    elif B2=='x' and C2 =="x" and D2=="x" and E2=="x":
        result()
    elif B2=='o' and C2 =="o" and D2=="o" and E2=="o":
        result1()
    elif C2=='x' and D2 =="x" and E2=="x" and F2=="x":
        result()
    elif C2=='o' and D2 =="o" and E2=="o" and F2=="o":
        result1()
    elif D2=='x' and E2 =="x" and F2=="x" and G2=="x":
        result()
    elif D2=='o' and E2 =="o" and F2=="o" and G2=="o":
        result1()

    ##
    elif A3=='x' and B3 =="x" and C3=="x" and D3=="x":
        result()
    elif A3=='o' and B3 =="o" and C3=="o" and D3=="o":
        result1()
    elif B3=='x' and C3 =="x" and D3=="x" and E3=="x":
        result()
    elif B3=='o' and C3 =="o" and D3=="o" and E3=="o":
        result1()
    elif C3=='x' and D3 =="x" and E3=="x" and F3=="x":
        result()
    elif C3=='o' and D3 =="o" and E3=="o" and F3=="o":
        result1()
    elif D3=='x' and E3 =="x" and F3=="x" and G3=="x":
        result()
    elif D3=='o' and E3 =="o" and F3=="o" and G3=="o":
        result1()

    ###7
    elif A4=='x' and B4 =="x" and C4=="x" and D4=="x":
        result()
    elif A4=='o' and B4 =="o" and C4=="o" and D4=="o":
        result1()
    elif B4=='x' and C4 =="x" and D4=="x" and E4=="x":
        result()
    elif B4=='o' and C4 =="o" and D4=="o" and E4=="o":
        result1()
    elif C4=='x' and D4 =="x" and E4=="x" and F4=="x":
        result()
    elif C4=='o' and D4 =="o" and E4=="o" and F4=="o":
        result1()
    elif D4=='x' and E4 =="x" and F4=="x" and G4=="x":
        result()
    elif D4=='o' and E4 =="o" and F4=="o" and G4=="o":
        result1()
    ###
    elif A5=='x' and B5 =="x" and C5=="x" and D5=="x":
        result()
    elif A5=='o' and B5 =="o" and C5=="o" and D5=="o":
        result1()
    elif B5=='x' and C5 =="x" and D5=="x" and E5=="x":
        result()
    elif B5=='o' and C5 =="o" and D5=="o" and E5=="o":
        result1()
    elif C5=='x' and D5 =="x" and E5=="x" and F5=="x":
        result()
    elif C5=='o' and D5 =="o" and E5=="o" and F5=="o":
        result1()
    elif D5=='x' and E5 =="x" and F5=="x" and G5=="x":
        result()
    elif D5=='o' and E5 =="o" and F5=="o" and G5=="o":
        result1()
    ###
    elif A6=='x' and B6 =="x" and C6=="x" and D6=="x":
        result()
    elif A6=='o' and B6 =="o" and C6=="o" and D6=="o":
        result1()
    elif B6=='x' and C6 =="x" and D6=="x" and E6=="x":
        result()
    elif B6=='o' and C6 =="o" and D6=="o" and E6=="o":
        result1()
    elif C6=='x' and D6 =="x" and E6=="x" and F6=="x":
        result()
    elif C6=='o' and D6 =="o" and E6=="o" and F6=="o":
        result1()
    elif D6=='x' and E6 =="x" and F6=="x" and G6=="x":
        result()
    elif D6=='o' and E6 =="o" and F6=="o" and G6=="o":
        result1()

    elif A1 == 'x' and B2 == "x" and C3 == "x" and D4 == "x":
        result()
    elif A1 == 'o' and B2 == "o" and C3 == "o" and D4 == "o":
        result1()
    elif A2 == 'x' and B3 == "x" and C4 == "x" and D5 == "x":
        result()
    elif A2 == 'o' and B3 == "o" and C4 == "o" and D5 == "o":
        result1()
    elif A3 == 'x' and B4 == "x" and C5 == "x" and D6 == "x":
        result()
    elif A3 == 'o' and B4 == "o" and C5 == "o" and D6 == "o":
        result1()
    elif A4 == 'x' and B3 == "x" and C2 == "x" and D1 == "x":
        result()
    elif A4 == 'o' and B3 == "o" and C2 == "o" and D1 == "o":
        result1()

    elif A5 == 'x' and B4 == "x" and C3 == "x" and D2 == "x":
        result()
    elif A5 == 'o' and B4 == "o" and C3 == "o" and D2 == "o":
        result1()
    elif A6 == 'x' and B5 == "x" and C4 == "x" and D3 == "x":
        result()
    elif A6 == 'o' and B5 == "o" and C4 == "o" and D3 == "o":
        result1()
    elif B1 == 'x' and C2 == "x" and D3 == "x" and E4 == "x":
        result()
    elif B1 == 'o' and C2 == "o" and D3 == "o" and E4 == "o":
        result1()
    elif B2 == 'x' and C3 == "x" and D4 == "x" and E5 == "x":
        result()
    elif B2 == 'o' and C3 == "o" and D4 == "o" and E5 == "o":
        result1()

    elif B3 == 'x' and C4 == "x" and D5 == "x" and E6 == "x":
        result()
    elif B3 == 'o' and C4 == "o" and D5 == "o" and E6 == "o":
        result1()
    elif B4 == 'x' and C3 == "x" and D2 == "x" and E1 == "x":
        result()
    elif B4 == 'o' and C3 == "o" and D2 == "o" and E1 == "o":
        result1()
    elif B5 == 'x' and C4 == "x" and D3 == "x" and E2 == "x":
        result()
    elif B5 == 'o' and C4 == "o" and D3 == "o" and E2 == "o":
        result1()
    elif B6 == 'x' and C5 == "x" and D4 == "x" and E3 == "x":
        result()
    elif B6 == 'o' and C5 == "o" and D4 == "o" and E3 == "o":
        result1()


    elif C1 == 'x' and D2 == "x" and E3 == "x" and F4 == "x":
        result()
    elif C1 == 'o' and D2 == "o" and E3 == "o" and F4 == "o":
        result1()
    elif C2 == 'x' and D3 == "x" and E4 == "x" and F5 == "x":
        result()
    elif C2 == 'o' and D3 == "o" and E4 == "o" and F5 == "o":
        result1()
    elif C3 == 'x' and D4 == "x" and E5 == "x" and F6 == "x":
        result()
    elif C3 == 'o' and D4 == "o" and E5 == "o" and F6 == "o":
        result1()
    elif C4 == 'x' and D3 == "x" and E2 == "x" and F1 == "x":
        result()
    elif C4 == 'o' and D3 == "o" and E2 == "o" and F1 == "o":
        result1()

    elif C5 == 'x' and D4 == "x" and E3 == "x" and F2 == "x":
        result()
    elif C5 == 'o' and D4 == "o" and E3 == "o" and F2 == "o":
        result1()
    elif C6 == 'x' and D5 == "x" and E4 == "x" and F3 == "x":
        result()
    elif C6 == 'o' and D5 == "o" and E4 == "o" and F3 == "o":
        result1()
    elif D1 == 'x' and E2 == "x" and F3 == "x" and G4 == "x":
        result()
    elif D1 == 'o' and E2 == "o" and F3 == "o" and G4 == "o":
        result1()
    elif D2 == 'x' and E3 == "x" and F4 == "x" and G5 == "x":
        result()
    elif D2 == 'o' and E3 == "o" and F4 == "o" and G5 == "o":
        result1()

    elif D3 == 'x' and E4 == "x" and F5 == "x" and G6 == "x":
        result()
    elif D3 == 'o' and E4 == "o" and F5 == "o" and G6 == "o":
        result1()
    elif D4 == 'x' and E3 == "x" and F2 == "x" and G1 == "x":
        result()
    elif D4 == 'o' and E3 == "o" and F2 == "o" and G1 == "o":
        result1()
    elif D5 == 'x' and E4 == "x" and F3 == "x" and G2 == "x":
        result()
    elif D5 == 'o' and E4 == "o" and F3 == "o" and G2 == "o":
        result1()
    elif D6 == 'x' and E5 == "x" and F4 == "x" and G3 == "x":
        result()
    elif D6 == 'o' and E5 == "o" and F4 == "o" and G3 == "o":
        result1()
    elif A1 !="e" and A2 !="e" and A3 !="e" and A4!="e" and A5!="e" and A6 !="e" and B1 !="e" and B2 !="e" and B3 !="e" and B4!="e" and B5!="e" and B6 !="e" and C1 !="e" and C2 !="e" and C3 !="e" and C4!="e" and C5!="e" and C6 !="e" and D1 !="e" and D2 !="e" and D3 !="e" and D4!="e" and D5!="e" and D6 !="e" and E1 !="e" and E2 !="e" and E3 !="e" and E4!="e" and E5!="e" and E6 !="e" and F1 !="e" and F2 !="e" and F3 !="e" and F4!="e" and F5!="e" and F6 !="e" and G1 !="e" and G2 !="e" and G3 !="e" and G4!="e" and G5!="e" and G6 !="e":
        result2()


##main function that handles and calls all other functions when needed
def main():
    global turn
    global player1
    player_turn()

    global A1
    global A2
    global A3
    global A4
    global A5
    global A6
    global B1
    global B2
    global B3
    global B4
    global B5
    global B6

    global C1
    global C2
    global C3
    global C4
    global C5
    global C6
    global D1
    global D2
    global D3
    global D4
    global D5
    global D6

    global E1
    global E2
    global E3
    global E4
    global E5
    global E6
    global F1
    global F2
    global F3
    global F4
    global F5
    global F6
    global G1
    global G2
    global G3
    global G4
    global G5
    global G6
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            (x, y) = pygame.mouse.get_pos()
            if x >= 1 and x <= 49 and y <= 100 and y>=56 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if A1=="e":
                        print("lk")
                        WIN.blit(xsign, (4, 305))
                        A1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif A2 =="e":
                        print("A2")
                        WIN.blit(xsign, (4, 255))
                        A2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif A3 =="e":
                        print("A2")
                        WIN.blit(xsign, (4, 205))
                        A3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif A4 =="e":
                        print("A2")
                        WIN.blit(xsign, (4, 155))
                        A4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif A5 =="e":
                        print("A2")
                        WIN.blit(xsign, (4, 105))
                        A5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif A6 =="e":
                        print("A2")
                        WIN.blit(xsign, (4, 55))
                        A6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if A1=="e":
                        print("lk")
                        WIN.blit(osign, (4, 305))
                        A1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif A2 =="e":
                        print("A2")
                        WIN.blit(osign, (4, 255))
                        A2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif A3 =="e":
                        print("A2")
                        WIN.blit(osign, (4, 205))
                        A3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif A4 =="e":
                        print("A2")
                        WIN.blit(osign, (4, 155))
                        A4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif A5 =="e":
                        print("A2")
                        WIN.blit(osign, (4, 105))
                        A5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif A6 =="e":
                        print("A2")
                        WIN.fill(yellow, (1, 5, 600, 40))
                        WIN.blit(osign, (4, 55))
                        A6="o"
                        pygame.display.update()
                        win_check()
            elif x >= 51 and x <= 100 and y <= 100 and y>=48 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if B1=="e":
                        print("lk")
                        WIN.blit(xsign, (55, 305))
                        B1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif B2 =="e":
                        print("A2")
                        WIN.blit(xsign, (55, 255))
                        B2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif B3 =="e":
                        print("A2")
                        WIN.blit(xsign, (55, 205))
                        B3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif B4 =="e":
                        print("A2")
                        WIN.blit(xsign, (55, 155))
                        B4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif B5 =="e":
                        print("A2")
                        WIN.blit(xsign, (55, 105))
                        B5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif B6 =="e":
                        print("A2")
                        WIN.blit(xsign, (55, 55))
                        B6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if B1=="e":
                        print("lk")
                        WIN.blit(osign, (55, 305))
                        B1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif B2 =="e":
                        print("A2")
                        WIN.blit(osign, (55, 255))
                        B2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif B3 =="e":
                        print("A2")
                        WIN.blit(osign, (55, 205))
                        B3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif B4 =="e":
                        print("A2")
                        WIN.blit(osign, (55, 155))
                        B4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif B5 =="e":
                        print("A2")
                        WIN.blit(osign, (55, 105))
                        B5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif B6 =="e":
                        print("A2")
                        WIN.blit(osign, (55, 55))
                        B6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()

            elif x >= 102 and x <= 150 and y <= 102 and y>=51 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if C1=="e":
                        print("lk")
                        WIN.blit(xsign, (105, 305))
                        C1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif C2 =="e":
                        print("A2")
                        WIN.blit(xsign, (105, 255))
                        C2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif C3 =="e":
                        print("A2")
                        WIN.blit(xsign, (105, 205))
                        C3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif C4 =="e":
                        print("A2")
                        WIN.blit(xsign, (105, 155))
                        C4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif C5 =="e":
                        print("A2")
                        WIN.blit(xsign, (105, 105))
                        C5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif C6 =="e":
                        print("A2")
                        WIN.blit(xsign, (105, 55))
                        C6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if C1=="e":
                        print("lk")
                        WIN.blit(osign, (105, 305))
                        C1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif C2 =="e":
                        print("A2")
                        WIN.blit(osign, (105, 255))
                        C2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif C3 =="e":
                        print("A2")
                        WIN.blit(osign, (105, 205))
                        C3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif C4 =="e":
                        print("A2")
                        WIN.blit(osign, (105, 155))
                        C4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif C5 =="e":
                        print("A2")
                        WIN.blit(osign, (105, 105))
                        C5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif C6 =="e":
                        print("A2")
                        WIN.blit(osign, (105, 55))
                        C6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()

            elif x >= 152 and x <= 200 and y <= 100 and y>=48 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if D1=="e":
                        print("lk")
                        WIN.blit(xsign, (155, 305))
                        D1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif D2 =="e":
                        print("A2")
                        WIN.blit(xsign, (155, 255))
                        D2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif D3 =="e":
                        print("A2")
                        WIN.blit(xsign, (155, 205))
                        D3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif D4 =="e":
                        print("A2")
                        WIN.blit(xsign, (155, 155))
                        D4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif D5 =="e":
                        print("A2")
                        WIN.blit(xsign, (155, 105))
                        D5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif D6 =="e":
                        print("A2")
                        WIN.blit(xsign, (155, 55))
                        D6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if D1=="e":
                        print("lk")
                        WIN.blit(osign, (155, 305))
                        D1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif D2 =="e":
                        print("A2")
                        WIN.blit(osign, (155, 255))
                        D2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif D3 =="e":
                        print("A2")
                        WIN.blit(osign, (155, 205))
                        D3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif D4 =="e":
                        print("A2")
                        WIN.blit(osign, (155, 155))
                        D4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif D5 =="e":
                        print("A2")
                        WIN.blit(osign, (155, 105))
                        D5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif D6 =="e":
                        print("A2")
                        WIN.blit(osign, (155, 55))
                        D6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()

            elif x >= 201 and x <= 249 and y <= 100 and y>=48 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if E1=="e":
                        print("lk")
                        WIN.blit(xsign, (205, 305))
                        E1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif E2 =="e":
                        print("A2")
                        WIN.blit(xsign, (205, 255))
                        E2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif E3 =="e":
                        print("A2")
                        WIN.blit(xsign, (205, 205))
                        E3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif E4 =="e":
                        print("A2")
                        WIN.blit(xsign, (205, 155))
                        E4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif E5 =="e":
                        print("A2")
                        WIN.blit(xsign, (205, 105))
                        E5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif E6 =="e":
                        print("A2")
                        WIN.blit(xsign, (205, 55))
                        E6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if E1=="e":
                        print("lk")
                        WIN.blit(osign, (205, 305))
                        E1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif E2 =="e":
                        print("A2")
                        WIN.blit(osign, (205, 255))
                        E2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif E3 =="e":
                        print("A2")
                        WIN.blit(osign, (205, 205))
                        E3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif E4 =="e":
                        print("A2")
                        WIN.blit(osign, (205, 155))
                        E4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif E5 =="e":
                        print("A2")
                        WIN.blit(osign, (205, 105))
                        E5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif E6 =="e":
                        print("A2")
                        WIN.blit(osign, (205, 55))
                        E6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()

            elif x >= 252 and x <= 299 and y <= 100 and y>=48 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if F1=="e":
                        print("lk")
                        WIN.blit(xsign, (255, 305))
                        F1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif F2 =="e":
                        print("A2")
                        WIN.blit(xsign, (255, 255))
                        F2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif F3 =="e":
                        print("A2")
                        WIN.blit(xsign, (255, 205))
                        F3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif F4 =="e":
                        print("A2")
                        WIN.blit(xsign, (255, 155))
                        F4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif F5 =="e":
                        print("A2")
                        WIN.blit(xsign, (255, 105))
                        F5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif F6 =="e":
                        print("A2")
                        WIN.blit(xsign, (255, 55))
                        F6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if F1=="e":
                        print("lk")
                        WIN.blit(osign, (255, 305))
                        F1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif F2 =="e":
                        print("A2")
                        WIN.blit(osign, (255, 255))
                        F2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif F3 =="e":
                        print("A2")
                        WIN.blit(osign, (255, 205))
                        F3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif F4 =="e":
                        print("A2")
                        WIN.blit(osign, (255, 155))
                        F4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif F5 =="e":
                        print("A2")
                        WIN.blit(osign, (255, 105))
                        F5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif F6 =="e":
                        print("A2")
                        WIN.blit(osign, (255, 55))
                        F6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()

            elif x >= 302 and x <= 348 and y <= 100 and y>=48 and event.type == pygame.MOUSEBUTTONDOWN:
                print("l")
                if player1 ==True:
                    if G1=="e":
                        print("lk")
                        WIN.blit(xsign, (305, 305))
                        G1 = "x"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=False
                        pygame.display.update()
                        win_check()
                    elif G2 =="e":
                        print("A2")
                        WIN.blit(xsign, (305, 255))
                        G2="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif G3 =="e":
                        print("A2")
                        WIN.blit(xsign, (305, 205))
                        G3="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif G4 =="e":
                        print("A2")
                        WIN.blit(xsign, (305, 155))
                        G4="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif G5 =="e":
                        print("A2")
                        WIN.blit(xsign, (305, 105))
                        G5="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                    elif G6 =="e":
                        print("A2")
                        WIN.blit(xsign, (305, 55))
                        G6="x"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = False
                        pygame.display.update()
                        win_check()
                else:
                    if G1=="e":
                        print("lk")
                        WIN.blit(osign, (305, 305))
                        G1 = "o"
                        WIN.fill(yellow, (1,5,600,40))
                        if turn ==False:
                            turn=True
                        else:
                            turn = False
                        player_turn()
                        player1=True
                        pygame.display.update()
                        win_check()
                    elif G2 =="e":
                        print("A2")
                        WIN.blit(osign, (305, 255))
                        G2="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif G3 =="e":
                        print("A2")
                        WIN.blit(osign, (305, 205))
                        G3="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif G4 =="e":
                        print("A2")
                        WIN.blit(osign, (305, 155))
                        G4="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif G5 =="e":
                        print("A2")
                        WIN.blit(osign, (305, 105))
                        G5="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        if turn == False:
                            turn = True
                        else:
                            turn = False
                        player_turn()
                        player1 = True
                        pygame.display.update()
                        win_check()
                    elif G6 =="e":
                        print("A2")
                        WIN.blit(osign, (305, 55))
                        G6="o"
                        WIN.fill(yellow, (1, 5, 600, 40))
                        pygame.display.update()
                        win_check()
        '''     
        WIN.blit(xsign, (4, 205))
        WIN.blit(xsign, (4, 155))
        WIN.blit(xsign, (4, 105))
        WIN.blit(xsign, (4, 55))
        '''
    pygame.quit()

if __name__ =="__main__":
    main()
