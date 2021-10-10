'''
ref : https://colab.research.google.com/drive/1nhVvTij1LuF-nB1okf9MHtyTdpmARzdG#scrollTo=lKwEjgkdONYV
'''
import time
N = int(input("Enter N : ")) # N x N Board

for j in range(4,N+1) :
    start = time.perf_counter()
    numSol = 0  			# number of solutions
    for i in range(4,j+1) :
        b = i*[-1]  			# indices = rows, b[index] = coloumn, first init to -1
        colFree = i*[1] 			# all N col are free at first
        upFree = (2*i - 1)*[1] 		# all up diagonals are free at first
        downFree = (2*i - 1)*[1]    		# all down diagonals are free at first

    def printBoard(b):
        print(b)

    def putQueen(r, b, colFree, upFree, downFree):
        global i
        global numSol
        for c in range(i): # ใล่ใส่ไปทีละ column ทุก col.
            if colFree[c] and upFree[r+c] and downFree[r-c+i-1]: #ใส่ได้?
                b[r] = c    # ใส่ ที่ r, c

                colFree[c] = upFree[r+c] = downFree[r-c+i-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

                if r == i-1:       # ถ้าใส่ควีนครบแล้ว
                    #printBoard(b)  #print(b)
                    numSol += 1
                else:
                    putQueen(r+1, b, colFree, upFree, downFree)  # ใส่ควีนแถวถัดไป
                colFree[c] = upFree[r+c] = downFree[r-c+i-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                               # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution
    putQueen(0, b, colFree, upFree, downFree)   #  first add at 1st  (ie. row 0)
    stop = time.perf_counter()
    print("Board : {}".format(i))
    print('number of solutions = ', numSol)
    print("Time : {}".format(stop-start))
