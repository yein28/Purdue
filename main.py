from tree import *
import random

def A():
	rootA 		= Node( "A", 1, 1 )
	sports      = Node( "sports", 80, 1 )
	baseball    = Node( "baseball", 50, 1 )
	
	rootA.input_Node( sports )
	sports.input_Node( baseball )
	return rootA

def utilOfB():
	UoB			= Node( "UoB", 1, 1 )
	sports      = Node( "sports", 50, 1 ) 
	baseball    = Node( "baseball", 20,1 )
	UoB.input_Node( sports )
	sports.input_Node( baseball )
	return UoB


def B():
	rootB 		= Node( "B", 1, 1 )
	sports 		= Node( "sports", 70, 1 )
	baseball 	= Node( "baseball", 70, 1 )
	rootB.input_Node( sports )
	sports.input_Node( baseball )
	return rootB

# 시나리오 : A가 B에게 야구에 대해 질문
def main():
	printNode( A() )
#	print( list( wordDic.items() ) )
#	print( "random : " + str ( random.choice( list( wordDic.values() ) ) ) )
	printNode( utilOfB() )
	printNode( B() )
	# 질문 
	#while(1)
	#	send

if __name__ == '__main__':
	main()
