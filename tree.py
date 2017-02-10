#tree's max depth  = 10 
			
#path를 구분자 '-'를 기준으로 분류
def parse( path ):
	path = path.split( '-' )
#	print( "parsing path : " + str(path) )
	return path

class Node():
	def __init__( self, key, interest, ct ):
		self.key = key
		self.interest = interest
		self.ct = ct
		self.dic = {}

	def input_Node( self, Node ):
		self.dic[Node.key] = Node

"""
def is_exist( inputnode, path ):
	if path[0] == inputnode.key:
		if path[1] in inputnode.dic:
			if len( path ) is 1 :
				print( "into update" )
#				update( self.dic[path[0]] )
			else:
				print( "into recur " +  str(path[2:] ) )
				tmp = inputnode.dic[path[1]] 
				is_exist( tmp, path[2:] )
		else:
			print( "create new node : " + str(path[0] ))
			inputnode.dic[str(path[0])] = node(path[0], 50, 0 )
	else:
		print( "newnode : " + str(path[0]) )
		inputnode.dic[str(path[0])] = node(path[0], 50, 0 )
"""
def is_Exist( root, path ):
	pointer = root
	del path[0]
	while path[0] in pointer.dic :
		print( "into while" )
		pointer = pointer.dic[path[0]]
		del path[0]
	
	print( path[0] )
#	while !path.empty():
		

	


def printNode( node , indent = 0):
	print( '\t' * indent + str(node.key) + " " + str(list(node.dic.keys())) + " " + str(node.ct) )
	for key, value in node.dic.items():
		if isinstance( value.dic, dict):
			printNode( value, indent + 1 )
		else:
			return 

def main():
	root = Node( "root", 1, 1 )  	
	sports= Node( "sports", 80, 1 )
	baseball = Node( "baseball", 50, 1 )
	soccer = Node( "soccer", 70, 1 )
	running = Node( "running", 30, 1 )
	kia = Node( "kia", 90, 1 ) 
	hw = Node( "hanhwa", 50, 1 )

	root.input_Node(sports) 
	sports.input_Node( baseball )
	sports.input_Node( soccer )
	sports.input_Node( running )
	soccer.input_Node( kia )
	baseball.input_Node( kia )
	baseball.input_Node( hw )
	printNode( root )

	tmp = parse( "root-sports-baseball-hanhwa" )
	is_Exist( root, tmp ) 
#	printNode( root )
	
if __name__ == '__main__':
	main()
