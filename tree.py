# parse the path string by '-' Input : String / Ouput : Array
def parse( path ):
	path = path.split( '-' )
	print( "parsing path : " + str(path) )
	return path

class Node():
	def __init__( self, key, interest, ct ):
		self.key = key
		self.interest = interest
		self.ct = ct
		self.dic = {}

	def input_Node( self, Node ):
		self.dic[Node.key] = Node

	def input_newNode( self, key ):
		newNode = Node( key, "50", "1" )
		self.dic[key] = newNode
		return newNode


def is_Exist( root, path ):
	pointer = root
	del path[0]

	while len(path) > 0 and path[0] in pointer.dic :
		print( "into while " + str(path[0]) )
		print( len(path) )
		pointer = pointer.dic[path[0]]
		del path[0]
	
	if len(path) is 0:
		print( "length is 0 something update " + str(pointer.key))
		pointer.interest = pointer.interest + 100000
	else:
		while len(path) is not 0 :
			nextNode = pointer.input_newNode( path[0] )
			pointer = nextNode
			del path[0]


def printNode( node , indent = 0):
	print( '\t' * indent + str(node.key) + " " + str(list(node.dic.keys())) + " " + str(node.interest) )
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

	path = parse( "root-sports-baseball-hanhwa" )
	is_Exist( root, path ) 
	printNode( root )
	
if __name__ == '__main__':
	main()
