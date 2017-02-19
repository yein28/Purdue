# parse the path string by '-' Input : String / Ouput : Array
wordDic = {}

def parse( path ):
	path = path.split( '-' )
	print( "parsing path : " + str(path) )
	return path

#class Dictionary():
#	def __init__ 
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
	tmp = list(path)
	del path[0]

	while len( path ) > 0 and path[0] in pointer.dic :
		pointer = pointer.dic[path[0]]
		del path[0]
	
	if len( path ) is 0:
#!!! make the update algorithm
		pointer.interest = pointer.interest + 100000
	else:
		while len(path) is not 0 :
			idx = tmp.index( path[0] ) + 1
#			print(str(path[0]) + " tmp : " + str(tmp[:idx] ) )i
			newPath =  makePath( tmp[:idx] ) 
			wordDic[path[0]] = newPath
			nextNode = pointer.input_newNode( path[0] )
			pointer = nextNode
			del path[0]

def makePath( pathList ):
	path = ""
	while len(pathList) != 1 :
		path = path + str(pathList.pop(0)) + "-"
	path = path + str(pathList.pop(0))
	return path

def printNode( node , indent = 0):
	print( '\t' * indent + str(node.key) + " " + str(list(node.dic.keys())) + " " + str(node.interest) )
	for key, value in node.dic.items():
		if isinstance( value.dic, dict):
			printNode( value, indent + 1 )
		else:
			return 
"""
def main():
	root = Node( "root", 1, 1 )  	
	sports= Node( "sports", 80, 1 )
	baseball = Node( "baseball", 50, 1 )
	soccer = Node( "soccer", 70, 1 )
	running = Node( "running", 30, 1 )
	kia = Node( "kia", 90, 1 ) 
	hw = Node( "hanhwa", 50, 1 )
	program = Node( "program", "50", 1 )
	
	root.input_Node( sports) 
	root.input_Node( program )
	sports.input_Node( baseball )
	sports.input_Node( soccer )
	sports.input_Node( running )
	soccer.input_Node( kia )
	baseball.input_Node( kia )
#	baseball.input_Node( hw )
	printNode( root )
	path = parse( "root-sports-baseball-hanhwa" )
	is_Exist( root, path ) 
	printNode( root )
	
if __name__ == '__main__':
	main()
"""
