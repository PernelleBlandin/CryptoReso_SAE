from .Piece import Piece


class Pion(Piece):

    def pawn(self,nam,to):##
        sign,getter,op_get,remember,opp_rem = (1,self.bpos,self.wpos,self.bdoublejumpers,self.wdoublejumpers) if nam[0] == 'b' else (-1,self.wpos,self.bpos,self.wdoublejumpers,self.bdoublejumpers)
        tx,ty = to
        fx,fy = getter.get(nam,[-1,-1])
        if fx==fy==-1 or tx==ty==-1: return False
        if nam[1] == 'p':
            # to move 2 steps forward
            if ty == fy and (tx == fx + 2*sign and self.board[tx-1*sign][ty] ==  self.board[tx][ty] == ' * '):
                getter[(nam:=nam[0]+'P'+nam[2])] = getter.pop(nam)
                if nam[0] == 'b':
                    self.bval = getter.values()
                else:
                    self.wval = getter.values()
                
                # remembers the pawn/attack_box for en_passant
                if self.mover(nam,to):
                    remember[nam] = [tx - sign,ty]
                    return True
                        
        pawn_present = to in op_get.values()
        cross_cond = (ty  in (fy-1,fy+1) and tx == fx + 1*sign )
        single_cond = (ty==fy and tx == fx + 1*sign and self.board[tx][ty] == ' * ')
        en_cond = [tx,ty] in opp_rem.values()
        
        # move single step
        if en_cond or (cross_cond and pawn_present) or  single_cond :
            # beginning single step
            if nam[1] == 'p':
                getter[(nam:=nam[0]+'P'+nam[2])] = getter.pop(nam)
                if nam[0] == 'b':
                    self.bval = getter.values()
                else:
                    self.wval = getter.values()
            
            if self.mover(nam,to):
                # if the remembered pawn moves out
                if single_cond and nam in remember:
                    remember.pop(nam)
                
                # if en_passant comes to action
                elif en_cond and cross_cond:
                    to_rem = self.board[tx-sign][ty]
                    self.board[tx-sign][ty] = ' * '
                    op_get.pop(to_rem)
                    self.bval = self.bpos.values()
                    self.wval = self.wpos.values()
                return True
        return False


    # nom: str
    # deplacements: list[int]
    # position: tuple
    # est_noir: bool
    # mouvements_effectues: int
    # stringRep: str

    # def __init__(
    #     self, est_noir: bool, position: tuple, mouvements_effectues: int
    # ) -> None:

    #     super().__init__(
    #         "Pion",
    #         est_noir,
    #         position,
    #         [(0, 1), (0, 2)] if mouvements_effectues == 0 else [(0, 1)],
    #         mouvements_effectues,
    #     )
    #     self.stringRep = "♙" if not self.est_noir else "♟"

    # def __str__(self) -> str:
    #     cote = "Noir" if self.est_noir else "Blanc"
    #     return (
    #         "Type : Pion"
    #         f" - Position : {self.position}"
    #         f" - Côte : {cote}"
    #         f" -- Mouvements effectués : {self.mouvements_effectues}"
    #     )
