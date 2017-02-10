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


def is_Exist( inputNode, path ):
	if path[0] == inputNode.key:
		if path[1] in inputNode.dic:
			if len( path ) is 1 :
				print( "into update" )
#				update( self.dic[path[0]] )
			else:
				print( "into recur " +  str(path[2:] ) )
				tmp = inputNode.dic[path[1]] 
				is_Exist( tmp, path[2:] )
		else:
			print( "create new Node : " + str(path[0] ))
			inputNode.dic[str(path[0])] = Node(path[0], 50, 0 )
	else:
		print( "newNode : " + str(path[0]) )
		inputNode.dic[str(path[0])] = Node(path[0], 50, 0 )

def printNode( Node , indent = 0):
	print( '\t' * indent + str(Node.key) + " " + str(list(Node.dic.keys())) + " " + str(Node.ct) )
	for key, value in Node.dic.items():
		if isinstance( value.dic, dict):
			printNode( value, indent + 1 )
		else:
			return 

def main():
	root = Node( "sports", 80, 1 )
	baseball = Node( "baseball", 50, 1 )
	soccer = Node( "soccer", 70, 1 )
	running = Node( "running", 30, 1 )
	kia = Node( "kia", 90, 1 ) 
	hw = Node( "hanhwa", 50, 1 )

	root.input_Node( baseball )
	root.input_Node( soccer )
	root.input_Node( running )
	soccer.input_Node( kia )
	baseball.input_Node( kia )
	baseball.input_Node( hw )
#	printNode( root )

	tmp = parse( "sports-baseball-kt" )
	is_Exist( root, tmp ) 
	printNode( root )
	
if __name__ == '__main__':
	main()
