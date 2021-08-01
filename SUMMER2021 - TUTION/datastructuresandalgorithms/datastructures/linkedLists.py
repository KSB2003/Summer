#linked list is a collection of nodes that point to each other.
#cannot come back to previous node - singly linked list - only one path.




class Node():
    def __init__(self, value):
        self.__value = value
        self.__next = None


    def nextsetter(self, node):
        self.__next = node

    def getternext(self):
        return self.__next

    def valgetter(self):
        return self.__value

def remover(head, node):
    if isinstance(head, Node):
        if head==node:
            head.nextsetter(None)
        else:
            while head is not None:
                if head.getternext()==node:
                    h1 = head.getternext()
                    h2 = h1.getternext()
                    head.nextsetter(h2)
                    h1.nextsetter(None)
                    break

                head = head.getternext()


def insertatend(head, node):
    """

    :param head: head of the linked list
    :param node: the node that you want to insert in the linked list at the end - similiar to an append function
    :return: nothing

    """
    pass


def inserter(head, node, position):
    """

    :param head: head of the linked list
    :param node: the node that you want to insert at the given position
    :param position: the position at which the node is to be inserted into - create condition to make the position valid
    :return: nothing
    """


def reverse(head):
    """

    the function would change the order of the linked list and not create a copy

    :param head: head of the linked list
    :return: the new head
    """


def circularize(head):
    """
    connect the tail to the head, make sure that there is no infinite loop
    :param head: the head of the linked list
    :return:
    """







def removerkeepboth(head, node):
    if isinstance(head, Node):
        if head==node:
            h1 = head.getternext()
            head.nextsetter(None)
            return h1

        else:
            temp = head
            while head is not None:
                if head.getternext()==node:
                    h1 = head.getternext()
                    h2 = h1.getternext()
                    head.nextsetter(h2)
                    h1.nextsetter(None)
                    break
                head = head.getternext()

            return temp


class MyLinkedList():
    def __init__(self):
        self.__nodes = []

    def appender(self, node):
        if isinstance(node, Node):
            self.__nodes.append(node)

    def listgetter(self):
        return self.__nodes





def printlist(head):
    if isinstance(head, Node):
        while head is not None:
            print(head.valgetter())
            head = head.getternext()







def runner():

    linkedList = MyLinkedList()

    ll1 = Node("a")
    #linkedList.appender(ll1)
    ll2 = Node("b")
    #linkedList.appender(ll2)
    ll3 = Node("c")
    #linkedList.appender(ll3)
    ll4 = Node("d")
    #linkedList.appender(ll4)
    ll5 = Node("e")
    #linkedList.appender(ll5)


    ll1.nextsetter(ll2)
    ll2.nextsetter(ll3)
    ll3.nextsetter(ll4)
    ll4.nextsetter(ll5)


    printlist(removerkeepboth(head=ll1, node=ll1))




runner()

"""
HW:
 - make an insert function
 - its parameters are head and node




"""
