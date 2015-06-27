# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import time

cells=[[0 for i in range(8)]for j in range(8)]
turn =True


def drawingReversi():
	raw=[" " for i in xrange(9)]
	raw[8]=" --------"
	for j in xrange(8):
		for i in xrange(8):
			if cells[j][i]==0:
				raw[j]+="0"
			elif cells[j][i]==1:
				raw[j]+="1"
			else:
				raw[j]+="2"
		print raw[j].decode("utf-8")
	print raw[8]

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

	if _posX<0 or _posX>7 or _posY<0 or _posY>7:
		return False

	if cells[_posX][_posY]==putStone:
		return False
	if cells[_posX][_posY]==0:
		return False

	_posX+=_vecX
	_posY+=_vecY

	while (_posX>=0 and _posX< 8 and _posY>=0 and _posY<8):
		 if cells[_posX][_posY]==0:
		 	return False

		 if cells[_posX][_posY]==putStone:
		 	return True

		 _posX+=_vecX
		 _posY+=_vecY






def canPut(_posX,_posY):
	if _posX>=8 or _posY>=8:
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


	while True:
		input=raw_input()
		time.sleep(1)
	
		if input!= None:
			data=input.split(" ")
			if len(data)==2:
				if canPut(int(data[1]),int(data[0])):
					put(int(data[1]),int(data[0]))
					reverseStone(int(data[1]),int(data[0]))
					if turn:
						print"next Player 2"
					else:
						print"next Player 1"
					drawingReversi()

					turn= not turn

				else:
					print "not putable"
			else:
				print "Syntax Error(posX(0<=posX<8) posY(0<=posY<8))"
