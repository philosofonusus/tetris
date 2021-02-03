f='Calibri'
e='gameover'
U=None
T='start'
S=len
I=False
H=True
C=range
import pygame as B,random as O
L=[(0,0,0),(120,37,179),(100,179,179),(80,34,22),(80,134,22),(12,0,255),(255,25,0)]
class V:
	x=0;y=0;figures=[[[1,5,9,13],[4,5,6,7]],[[4,5,9,10],[2,6,5,9]],[[6,7,9,10],[1,5,6,10]],[[1,2,5,9],[0,4,5,6],[1,5,9,8],[4,5,6,10]],[[1,2,6,10],[5,6,7,9],[2,6,10,11],[3,5,6,7]],[[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,9]],[[1,2,5,6]]]
	def __init__(A,x,y):A.x=x;A.y=y;A.type=O.randint(0,S(A.figures)-1);A.color=O.randint(1,S(L)-1);A.rotation=0
	def image(A):return A.figures[A.type][A.rotation]
	def rotate(A):A.rotation=(A.rotation+1)%S(A.figures[A.type])
class W:
	level=2;score=0;state=T;field=[];height=0;width=0;x=100;y=60;zoom=20;figure=U
	def __init__(A,height,width):
		D=width;B=height;A.height=B;A.width=D;A.field=[];A.score=0;A.state=T
		for F in C(B):
			E=[]
			for G in C(D):E.append(0)
			A.field.append(E)
	def new_figure(A):A.figure=V(3,0)
	def intersects(A):
		E=I
		for D in C(4):
			for B in C(4):
				if D*4+B in A.figure.image():
					if D+A.figure.y>A.height-1 or B+A.figure.x>A.width-1 or B+A.figure.x<0 or A.field[D+A.figure.y][B+A.figure.x]>0:E=H
		return E
	def break_lines(A):
		G=0
		for E in C(1,A.height):
			B=0
			for D in C(A.width):
				if A.field[E][D]==0:B+=1
			if B==0:
				B+=1
				for F in C(E,1,-1):
					for D in C(A.width):A.field[F][D]=A.field[F-1][D];A.score+=B**2
	def go_down(A):
		A.figure.y+=1
		if A.intersects():A.figure.y-=1;A.freeze()
	def freeze(A):
		for B in C(4):
			for D in C(4):
				if B*4+D in A.figure.image():A.field[B+A.figure.y][D+A.figure.x]=A.figure.color
		A.break_lines();A.new_figure()
		if A.intersects():A.state=e
	def go_side(A,dx):
		B=A.figure.x;A.figure.x+=dx
		if A.intersects():A.figure.x=B
	def rotate(A):
		B=A.figure.rotation;A.figure.rotate()
		if A.intersects():A.figure.rotation=B
B.init()
X=0,0,0
Y=255,255,255
Z=128,128,128
J=400,500
G=B.display.set_mode(J)
B.display.set_caption('Tetris')
P=I
a=B.time.Clock()
Q=60
A=W(20,10)
K=0
M=I
while not P:
	if A.figure is U:A.new_figure()
	K+=1
	if K>100000:K=0
	if K%(Q//A.level//2)==0 or M:
		if A.state==T:A.go_down()
	for D in B.event.get():
		if D.type==B.QUIT:P=H
		if D.type==B.KEYDOWN:
			if D.key==B.K_UP:A.rotate()
			if D.key==B.K_DOWN:M=H
			if D.key==B.K_LEFT:A.go_side(-1)
			if D.key==B.K_RIGHT:A.go_side(1)
			if D.key==B.K_ESCAPE:A.__init__(20,10);A.figure=U
	if D.type==B.KEYUP:
		if D.key==B.K_DOWN:M=I
	G.fill(Y)
	for E in C(A.height):
		for F in C(A.width):
			B.draw.rect(G,Z,[A.x+A.zoom*F,A.y+A.zoom*E,A.zoom,A.zoom],1)
			if A.field[E][F]>0:B.draw.rect(G,L[A.field[E][F]],[A.x+A.zoom*F+1,A.y+A.zoom*E+1,A.zoom-2,A.zoom-1])
	if A.figure:
		for E in C(4):
			for F in C(4):
				b=E*4+F
				if b in A.figure.image():B.draw.rect(G,L[A.figure.color],[A.x+A.zoom*(F+A.figure.x)+1,A.y+A.zoom*(E+A.figure.y)+1,A.zoom-2,A.zoom-2])
	R=B.font.SysFont(f,25,H,I);g=B.font.SysFont(f,65,H,I);N=R.render(str(A.score),H,X);c=N.get_rect(center=(J[0]/2,20))
	if A.state==e:d=R.render('Game Over',H,(255,0,0));G.blit(d,N.get_rect(center=(J[0]/2-50,J[1])))
	G.blit(N,c);B.display.flip();a.tick(Q)
B.quit()
