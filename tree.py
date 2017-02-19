# key : word, value : path to word
wordDic = {}

# parse the path string by '-' Input : String / Ouput : Array
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

	def input_newNode( self, key ):
		newNode = Node( key, 0, 1 )
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
			idx = tmp.index( path[0] ) + 1				# get idx 
			newPath =  makePath( tmp[:idx] ) 			# slice the list to make path
			wordDic[path[0]] = newPath					# input new word to dictionary 
			nextNode = pointer.input_newNode( path[0] )
			pointer = nextNode
			del path[0]

def makePath( pathList ):	
	path = ""
	while len(pathList) != 1 :
		path = path + str(pathList.pop(0)) + "-"
	path = path + str(pathList.pop(0))
	return pathwordDic[path[0]] = newPath

def printNode( node , indent = 0):
	print( '\t' * indent + str(node.key) + " " + str(list(node.dic.keys())) + " " + str(node.interest) )
	for key, value in node.dic.items():
		if isinstance( value.dic, dict):
			printNode( value, indent + 1 )
		else:
			return 
