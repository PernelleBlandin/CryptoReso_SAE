from classes.Plateau import Plateau
import os
from os import system

class Jeu():
    def __init__(self) -> None:
        self.plateau = Plateau()

    def lancer(self):
        print("\n")
        print("Bienvenue dans le jeu d'échecs !\n")
        print(self.plateau)



    def mover(self,pawn,to):
        if pawn[0] in ('b','w'):
            pos,op_pos,val,op_val,word,op_word,num = (self.bpos,self.wpos,self.bval,self.wval,'b','w',1) if pawn[0] == 'b' else (self.wpos,self.bpos,self.wval,self.bval,'w','b',6)
            opp_pawn = (' * ',-1)
            
            # checks for opp pawn! if there remove it from db..
            if to in op_val:
                [opp_pawn:=(x,op_pos[x]) for x,y in op_pos.items() if y == to]
                op_pos.pop(opp_pawn[0])
            
            ## checks for same pawn! if there illegal move(false)
            elif to in val:
                return False
            
            ## does all the shifting stuff db and board.
            fr = pos[pawn]
            pos[pawn] = to
            self.board[to[0]][to[1]] = pawn   
            self.board[fr[0]][fr[1]] = ' * '
            if pawn[0]=='b':
                self.bcheck = False
            else:
                self.wcheck = False
            ## if same color was able to move --> then its outa check
            
            ## checks after the weather king of same still in check --> if yes backtracks previous move..
            if self.checker(word):
                ## reverses the P-->p if its in check and not moved
                if pawn[1] == 'P' and fr[0] == num:
                    pos[(pawn := pawn[0] + 'p' + pawn[2])] = pos.pop(pawn)
                    
                self.board[fr[0]][fr[1]] = pawn
                self.board[to[0]][to[1]] = opp_pawn[0]
                pos[pawn] = fr
                if opp_pawn[1] != -1:
                    op_pos[opp_pawn[0]] = to
                if pawn[0]=='b':
                    self.bcheck = True
                else:
                    self.wcheck = True
                return False
            
            #  if previous cond is wrong --> checks for opp color check..
            else:
                if self.checker(op_word):
                    print(f'\n\t\tDUDE {op_word} ON CHECK\n') # word
                    if pawn[0]=='b':
                        self.wcheck = True
                    else:
                        self.bcheck = True
                    
        self.wval = self.wpos.values()
        self.bval = self.bpos.values()
        return True




if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancer()
    mov = 0
    turns = ['w','b']
    while (inp:=(input('name: '))) != 'xxx':
        if len(inp) == 3 and inp[0]==turns[mov%2]:
            if inp[2] != 'c':
                raw = input("pos: ").strip()

                # Allow formats: "5 1", "5,1", "(5,1)", "51"
                clean = ''.join(ch for ch in raw if ch.isdigit())

                if len(clean) != 2:
                    print("give correct position bro")
                    continue
                pos = [int(clean[0]), int(clean[1])]
            else:
                pos = [0,0]
            system('cls' if os.name == 'nt' else 'clear')

            if jeu.sorter(inp,pos):
                jeu.print_board()
                mov += 1
            else:
                print('\t\tillegal move brothor')
                if jeu.wcheck:
                    print('\t\tDUDE w STILL IS ON CHECK')
                elif jeu.bcheck:
                    print('\t\tDUDE b STILL IS ON CHECK')
                jeu.print_board()
        else:
            print(f"its {turns[mov%2]} turn now")
    print(f"\t\t{turns[mov%2]} forfited\n\t\thence {turns[(mov+1)%2]} wins")
