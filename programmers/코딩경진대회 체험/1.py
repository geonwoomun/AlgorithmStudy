# 코딩경진대회 체험 1번

#첫 번째 점 p의 좌표 
px, py = list(map(int, input().split()))
#두 번째 점 q의 좌표 
qx, qy = list(map(int ,input().split()))
	
if(px == qx and py == qy):
	print("DOT")
elif((px == qx and py != qy) or (px != qx and py == qy)):
	print("SEGMENT")
elif(abs(px-qx) == abs(py-qy)):
	print("SQUARE")
else:
	print("RECTANGLE")