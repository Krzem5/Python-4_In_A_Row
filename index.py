from math import floor



class Engine:
	def __init__(self,st="player"):
		self.st=st
		self.tiles={"player":"O","computer":"X"}
		self.ctile=self.tiles[self.st]
		self.board=self.new_board()

	def new_board(self,w=7,h=6):
		b=[]
		for y in range(h):b+=[[" "]*w]
		return b

	def board_to_string(self,b,s=[False,[]]):
		for sp in s[1]:b[sp[0]][sp[1]]="#"
		s=f"\n\n {str(list(range(1,len(b[0])+1))).replace('[','').replace(']','').replace(',','')}\n{'+-'*(len(b[0]))}+\n"
		for x in range(len(b)):
			for y in range(len(b[0])):
				s+=f"|{b[x][y]}"
			s+=f"|\n{'+-'*(len(b[0]))}+\n"
		return s

	def get_player_move(self,b):
		while True:
			n=input(f"\nWhat's your move? (1-{len(b[0])})\t")
			if self.valid(n,b):
				break
		return int(n)-1

	def valid(self,m,b):
		try:
			m=int(m)-1
		except:
			return False
		if not (-1<m<len(b[0])) or b[0][m]!=" ":
			return False
		return True

	def get_computer_move(self,b):
		return 0

	def make_move(self,m,b,t):
		for yi in range(len(b)-1,-1,-1):
			if b[yi][m]==" ":break
		b[yi][m]=t
		return b,self.check_win(b,t,[yi,m])

	def check_win(self,b,t,p):
		ds=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
		for d in ds:
			ws=[]
			x=int(p[1])
			y=int(p[0])
			ws+=[[y,x]]
			while True:
				x+=d[0]
				y+=d[1]
				if x<0 or y<0 or x>len(b[0])-1 or y>len(b)-1 or len(ws)==4 or b[y][x]!=t:
					break
				ws+=[[y,x]]
			if len(ws)==4:break
		ld={"X":"Computer","O":"You"}
		return [len(ws)==4,ws,f"\n{ld[t]} won.\n\n"]

	def swap_tile(self,t):
		return {"X":"O","O":"X"}[t]

	def ask_play_again(self):
		while True:
			p=input("Do you want to play again? (y/n)\t")
			if p in list("yn"):
				break
		return p=="y"

	def reset(self):
		self.ctile=self.tiles[self.st]
		self.board=self.new_board()

	def run(self):
		while True:
			if self.ctile==self.tiles["player"]:
				print(self.board_to_string(self.board))
				m=self.get_player_move(self.board)
			else:
				m=self.get_computer_move(self.board)
			self.board,s=self.make_move(m,self.board,self.ctile)
			if s[0]:
				print(self.board_to_string(self.board,s))
				print(s[2])
				if self.ask_play_again():
					self.reset()
				else:
					break
			else:
				self.ctile=self.swap_tile(self.ctile)

if __name__=="__main__":
	e=Engine()
	e.run()
