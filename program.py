"""
YOU ARE ON A PERFECT GRID OF N X N NODE
EVEN ROWS GO EAST
ODD ROWS GO WEST
EVEN COLOMNS GO NORTH
ODD COLOMNS GO SOUTH
EVERY NODE HAS A LIGHT
ALL LIGHTS ARE SYNCED 
L:= TIME THAT THE STOP LIGHTS STAY IN A STATE
T:= SIMPLE INT REPRESENTING CURRENT TIME
D:= TIME IT TAKES TO MOVE FROM ONE NODE TO THE NEXT
T//L%2==0 YOU CAN ONLY LEAVE NODES GOING HORIZONTALLY OR WAIT
T//L%2==1 YOU CAN ONLY LEAVE NODES GOING VERTICALLY OR WAIT

"""
D=5
L=3

#SHOULD SQRT BUT NOT NEEDED FOR COMPARES
def dist(a,b):
	return (a[0]-b[0])**2+(a[1]-b[1])**2

#MANHATTAN DISTANCE
def mandist(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])


#IDEALLY THIS WILL USE (X,Y,T) INSTEAD OF JUST (X,Y) FOR EXPLORED NODE DATA STORAGE
def time3Dijkstra(start,end):
	pass
	
#BREADTH FIRST SEARCH
def timeBFS(start,end):
	startx,starty=start
	x1,y1,T=startx,starty,0
	explored=set()
	nodes=[(x1,y1,T)]
	for node in nodes:
		# ~ print(len(explored))
		
		x,y,T=node
		if T+5*mandist((x,y),end) >150:
			continue
			
		waitnode = (x,y,T+1)
		
		dx=1-y%2*2
		dy=1-x%2*2
		hNode=(x+dx,y,T+5)
		vNode=(x,y+dy,T+5)
		if T//L%2==0 and hNode not in explored:
			nodes.append(hNode)
			explored.add(hNode)
		elif T//L%2==1 and hNode not in explored:
			nodes.append(vNode)
			explored.add(vNode)
		if waitnode not in explored:
			nodes.append(waitnode)
			explored.add(waitnode)

	# ~ print(start)
	# ~ print(end)
	t=min([t for i,j,t in explored if (i,j)==end])
	return t

#MOVES THROUGH INTERSECTION AS LONG AS NEXT INTERESTION IS CLOSER
#IF NIETHER ARE CLOSER...MOVE TO THE NEXT CLOSEST
def timeOpportunistic(start,end,getpath=False):
	x1,y1=start
	x2,y2=end
	T=0
	path=[(x1,y1)]
	while (x1,y1)!=(x2,y2):
		dx=1-y1%2*2
		dy=1-x1%2*2
		hNode=(x1+dx,y1)
		vNode=(x1,y1+dy)
		closest=min([hNode,vNode],key=lambda p:dist(p,end))
		if T//L%2==0 and mandist(hNode,end)<mandist((x1,y1),end):
			T+=D
			path+=[(x1,y1,T)]
			x1+=dx
			
			# ~ print("go "+("east" if dx==1 else "west"))
		elif T//L%2==1 and mandist(vNode,end)<mandist((x1,y1),end):
			T+=D
			y1+=dy
			path+=[(x1,y1,T)]
			# ~ print("go "+("north" if dy==1 else "south"))
		elif T//L%2==0 and closest==hNode:
			T+=D
			x1+=dx
			path+=[(x1,y1,T)]
			# ~ print("go "+("east" if dx==1 else "west"))
		elif T//L%2==1 and closest==vNode:
			T+=D
			y1+=dy
			path+=[(x1,y1,T)]
			# ~ print("go "+("north" if dy==1 else "south"))
		else:
			T+=1
			path+=[(x1,y1,T)]
			# ~ print("wait")
		# ~ input(str((x1,y1)))
	if getpath:
		return T,path
	else:
		return T

#ONLY MOVES TO THE NEXT CLOSEST INTERSECTION (AS THE CROW FLIES)
def timeDirect(start,end):
	x1,y1=start
	x2,y2=end
	T=0
	while (x1,y1)!=(x2,y2):
		dx=1-y1%2*2
		dy=1-x1%2*2
		hNode=(x1+dx,y1)
		vNode=(x1,y1+dy)
		closest=min([hNode,vNode],key=lambda p:dist(p,end))
		if T//L%2==0 and closest==hNode:
			T+=D
			x1+=dx
			# ~ print("go "+("east" if dx==1 else "west"))
		elif T//L%2==1 and closest==vNode:
			T+=D
			y1+=dy
			# ~ print("go "+("north" if dy==1 else "south"))
		else:
			T+=1
			# ~ print("wait")
		# ~ input(str((x1,y1)))
	return T
	
	
t=timeDirect((0,0),(10,10))
print(t)

t=timeOpportunistic((0,0),(10,10))
print(t)

t=timeBFS((0,0),(10,10))
print(t)

data=[]
hist_direct=[]
hist_op=[]
hist_bfs=[]
worst=[0]
for x1 in range(5):
	for y1 in range(5):
		for x2 in range(5):
			for y2 in range(5):	
				td=timeDirect((x1,y1),(x2,y2))
				to=timeOpportunistic((x1,y1),(x2,y2))
				tb=timeBFS((x1,y1),(x2,y2))
				md=mandist((x1,y1),(x2,y2))
				if to>worst[0]:
					worst=[to,(x1,y1),(x2,y2)]
				if md==0:
					continue
				data.append((md,td,to,tb))
				hist_direct.append(td/md)
				hist_op.append(to/md)
				hist_bfs.append(tb/md)
print(worst)

import matplotlib.pyplot as plt

# Get the x and y values from the data
x,y1,y2,y3=list(zip(*data))

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the scatter plot
p1=ax.scatter(x, y1,label="direct")
p2=ax.scatter(x, y2,label="opportunistic")
p3=ax.scatter(x ,y3,label="breadth")

p1.set_sizes([3])
p2.set_sizes([3])
p3.set_sizes([3])
# Add a legend
ax.legend()

# Show the plot
plt.show()

print(max(hist_direct),min(hist_direct))

fig2, ax2 = plt.subplots()

# Create the first histogram
ax2.hist(hist_direct, label='direct',bins=30)

# Create the second histogram
ax2.hist(hist_op, label='opportunistic', alpha=0.5,bins=30)

#Create the third histogram
ax2.hist(hist_bfs, label='breadth', alpha=0.5, bins=30)

# Add a legend
ax2.legend()

# Show the plot
plt.show()

_,path=timeOpportunistic((1, 19), (2, 0),True)
print(path)
