class SinglyLLNode():
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

node1=SinglyLLNode("5")
node2=SinglyLLNode("7")
node3=SinglyLLNode("9")
node4=SinglyLLNode("11")

node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4

Currentnode=node1
while True:
    Currentnode=Currentnode.nextNode
    print(Currentnode.value,"->")
    if Currentnode.nextNode is None:
        print("None")
        break
    
