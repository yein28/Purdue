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

	# path = array / ex)[sports, baseball, kia]
	def is_Exist( self, path ):
		if path[0] in self.dic:
			is_Exist( self.dic[path[0]], path[1:] )
		else:
			inputNode = ( path[0], 50, 0 )
			self.dic[path[0]] = inputNode
		

	# update the value
	#def update( self, Node ):	

	def del_Node( self, Node ):
		del self.dic[Node.key]

def printNode( Node, indent ):
	print Node
	for key, value in Node.dic.items():
		print( str(key) )
		if type(value) is Node:
			printNode( value , 0 ) 

def main():
	root = Node( "sports", 80, 1 )
	baseball = Node( "baseball", 50, 1 )

	root.input_Node( baseball )
	printNode( root, 0 )

	tmp = parse( "sports-baseball-kia" )
	root.is_Exist( tmp ) 
	
if __name__ == '__main__':
	main()
