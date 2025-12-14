class Plateau:

    def __init__(self):
        self.board = [['br1','bh1','bb1','bq0','bk0','bb2','bh2','br2'],
                        ['bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8'],
                        [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * '],
                        [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * '],
                        [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * '],
                        [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * '],
                        ['wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8'],
                        ['wr1','wh1','wb1','wq0','wk0','wb2','wh2','wr2']]
        self.bpos = {'br1':[0,0],'bh1':[0,1],'bb1':[0,2],'bq0':[0,3],'bk0':[0,4],'bb2':[0,5],'bh2':[0,6],'br2':[0,7],
                        'bp1':[1,0],'bp2':[1,1],'bp3':[1,2],'bp4':[1,3],'bp5':[1,4],'bp6':[1,5],'bp7':[1,6],'bp8':[1,7]}
        self.wpos = {'wr1':[7,0],'wh1':[7,1],'wb1':[7,2],'wq0':[7,3],'wk0':[7,4],'wb2':[7,5],'wh2':[7,6],'wr2':[7,7],
                        'wp1':[6,0],'wp2':[6,1],'wp3':[6,2],'wp4':[6,3],'wp5':[6,4],'wp6':[6,5],'wp7':[6,6],'wp8':[6,7]}
        self.wval = self.wpos.values()
        self.bval = self.bpos.values()
        self.wdoublejumpers = {}
        self.bdoublejumpers = {}
        self.wcheck = self.bcheck = False
    
    def print_board(self):
        print('   ',end='')
        [print(f' {x}    ',end='') for x in range(8)]
        print()
        for num,x in enumerate(self.board):
            print(num,' ',end='')
            print(' | '.join(x),'-'*50,sep='\n')
    
