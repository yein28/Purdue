from tree import *
import random

def getRandPath( root, key ):

	return path

def main():
	root = Node( "root", 1, 1 )    
	sports= Node( "sports", 80, 1 ) 
	baseball = Node( "baseball", 50, 1 ) 
	soccer = Node( "soccer", 70, 1 ) 
	running = Node( "running", 30, 1 ) 
	kia = Node( "kia", 90, 1 ) 
	hw = Node( "hanhwa", 50, 1 ) 
	program = Node( "program", "50", 1 ) 

#	root.input_Node( sports )
#	root.input_Node( program )
#	sports.input_Node( baseball )
#	sports.input_Node( soccer )
#	sports.input_Node( running )
#	soccer.input_Node( kia )
#	baseball.input_Node( kia )
#   baseball.input_Node( hw )
#	printNode(root)
	path = parse( "root-sports-baseball-hanhwa" )
	is_Exist( root, path )
	path = parse( "root-sports-soccer" )
	is_Exist( root, path )
	path = parse( "root-program" )
	is_Exist( root, path )
	printNode( root )
	print( list( wordDic.items() ) )
#	while( 1 ):
	print( "random : " + str ( random.choice( list( wordDic.values() ) ) ) )

if __name__ == '__main__':
	main()
