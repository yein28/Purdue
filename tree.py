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

	# path = array / ex)[sports, baseball, kt]
	def is_Exist( self, path ):
		if path[0] in self.dic:
			if path.len == 1:
				update( self.dic[path[0]] )
			else:
				is_Exist( self.dic[path[0]], path[1:] )
		else:
			inputNode = Node( path[0], 50, 0 )
			self.dic[path[0]] = inputNode

	# update the value
	#def update( self, Node ):	

	def del_Node( self, Node ):
		del self.dic[Node.key]

def printNode( Node , indent = 0):
	print( '\t' * indent + str(Node.key) )
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
	root.is_Exist( tmp ) 
	printNode( root )
	
if __name__ == '__main__':
	main()
