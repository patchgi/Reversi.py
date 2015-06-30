# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import random
import time

FIELD=8
cells=[[0 for i in range(FIELD)]for j in range(FIELD)]
turn =True


def drawingReversi():
	raw=[" " for i in xrange(9)]
	raw[8]=" --------"
	for j in xrange(FIELD):
		for i in xrange(FIELD):
			if cells[j][i]==0:
				raw[j]+="0"
			elif cells[j][i]==1:
				raw[j]+="1"
			else:
				raw[j]+="2"
		print raw[j].decode("utf-8")
	print raw[FIELD]

def put(_posX,_posY):
	global turn
	putStone=0
	if turn:
		putStone=1
	else:
		putStone=2

	cells[_posX][_posY]=putStone


def canPutStone(_posX,_posY,_vecX,_vecY):
	putStone=0
	global turn
	if turn:
		putStone=1
	else:
		putStone=2
	_posX+=_vecX
	_posY+=_vecY

	if _posX<0 or _posX>FIELD-1 or _posY<0 or _posY>FIELD-1:
		return False

	if cells[_posX][_posY]==putStone:
		return False
	if cells[_posX][_posY]==0:
		return False

	_posX+=_vecX
	_posY+=_vecY

	while (_posX>=0 and _posX< FIELD and _posY>=0 and _posY<FIELD):
		 if cells[_posX][_posY]==0:
		 	return False

		 if cells[_posX][_posY]==putStone:
		 	return True

		 _posX+=_vecX
		 _posY+=_vecY



def canPut(_posX,_posY):
	if _posX>=FIELD or _posY>=FIELD:
		return False
	if cells[_posX][_posY]!=0:
		return False

	if canPutStone(_posX, _posY, -1, -1):
		return True
	if canPutStone(_posX, _posY, 0, -1):
		return True
	if canPutStone(_posX, _posY, 1, -1):
		return True
	if canPutStone(_posX, _posY, -1, 0):
		return True
	if canPutStone(_posX, _posY, 1, 0):
		return True
	if canPutStone(_posX, _posY, -1, 1):
		return True
	if canPutStone(_posX, _posY, 0, 1):
		return True
	if canPutStone(_posX, _posY, 1, 1):
		return True

def reverse(_posX, _posY, _vecX, _vecY):
    global turn
    putStone = 0

    if turn:
        putStone = 1
    else:
        putStone = 2

    _posX += _vecX
    _posY += _vecY

    while(cells[_posX][_posY] != putStone):

        cells[_posX][_posY] = putStone
        _posX += _vecX
        _posY += _vecY

def reverseStone(_posX, _posY):

    if canPutStone(_posX, _posY, -1, -1):
        reverse(_posX, _posY, -1, -1)
    if canPutStone(_posX, _posY, 0, -1):
        reverse(_posX, _posY, 0, -1)
    if canPutStone(_posX, _posY, 1, -1):
        reverse(_posX, _posY, 1, -1)
    if canPutStone(_posX, _posY, -1, 0):
        reverse(_posX, _posY, -1, 0)
    if canPutStone(_posX, _posY, 1, 0):
        reverse(_posX, _posY, 1, 0)
    if canPutStone(_posX, _posY, -1, 1):
        reverse(_posX, _posY, -1, 1)
    if canPutStone(_posX, _posY, 0, 1):
        reverse(_posX, _posY, 0, 1)
    if canPutStone(_posX, _posY, 1, 1):
        reverse(_posX, _posY, 1, 1)

if __name__=="__main__":
	data=0
	cells [3][3]=1
	cells [3][4]=2
	cells [4][3]=2
	cells [4][4]=1

	playCount=0
	blackStone=0
	whiteStone=0

	drawingReversi()

	while True:
		#judgeGame
		if playCount==60:
			for i in xrange(FIELD):
				for j in xrange(FIELD):
					if cells[i][j]==1:
						blackStone+=1
					if cells[i][j]==2:
						whiteStone+=1

			if blackStone>whiteStone:
				print "black WIN"
				break
			elif blackStone<whiteStone:
				print "white WIN"
				break

			else:
				print "DRAW"
		canCount=0
		if turn:
			for i in xrange(8):
				for j in xrange(8):
					if canPut(i,j):
						canCount+=1
			if canCount==0:
				print "pass"
				print "next Player 1"
				turn=not turn
				break
			time.sleep(.1)
			x=0
			y=0
			while(True):
				x=random.randint(0,7)
				y=random.randint(0,7)
				if canPut(x,y):
					break

			put(x,y)
			playCount+=1
			reverseStone(x,y)

			print str(y)+" "+str(x)

			drawingReversi()

			print"next Player 2"

			turn= not turn
			"""
			for i in xrange(8):
				for j in xrange(8):
					if canPut(i,j):
						canCount+=1;
			if canCount==0:
				print "pass"
				print "next Player 1"
				turn=not turn
				break
			input=raw_input()
			time.sleep(.1)
	
			if input!= None:
				data=input.split(" ")

				if len(data)==2:
					if canPut(int(data[1]),int(data[0])):
						put(int(data[1]),int(data[0]))
						playCount+=1
						reverseStone(int(data[1]),int(data[0]))

						drawingReversi()

						print"next Player 2"

						turn= not turn

					else:
						print "not putable"
				else:
					print "Syntax Error(posX(0<=posX<FIELD) posY(0<=posY<FIELD))"
					"""
		else:

			for i in xrange(8):
				for j in xrange(8):
					if canPut(i,j):
						canCount+=1
			if canCount==0:
				print "pass"
				print "next Player 1"
				turn=not turn
				break
			time.sleep(.1)
			x=0
			y=0
			while(True):
				x=random.randint(0,7)
				y=random.randint(0,7)
				if canPut(x,y):
					break

			put(x,y)
			playCount+=1
			reverseStone(x,y)

			print str(y)+" "+str(x)

			drawingReversi()

			print"next Player 1"

			turn= not turn