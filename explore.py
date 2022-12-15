def mandist(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def bfs(a,b):
	startx,starty=a
	L=3
	x1,y1,t=startx,starty,0
	best={}
	explored=set()
	nodes=[(x1,y1,t)]
	for node in nodes:
		# ~ print(len(explored))
		
		x,y,t=node
		if t+5*mandist((x,y),b) >150:
			continue
			
		waitnode = (x,y,t+1)
		
		dx=1-y%2*2
		dy=1-x%2*2
		hNode=(x+dx,y,t+5)
		vNode=(x,y+dy,t+5)
		if t//L%2==0 and hNode not in explored:
			nodes.append(hNode)
			explored.add(hNode)
		elif t//L%2==1 and hNode not in explored:
			nodes.append(vNode)
			explored.add(vNode)
		if waitnode not in explored:
			nodes.append(waitnode)
			explored.add(waitnode)

	print(explored)
	t=min([t for i,j,t in explored if (i,j)==b])
	return t
	
print(bfs((0,0),(10,10)))
	# ~ loop through explored and find min t value where x and y are your target
