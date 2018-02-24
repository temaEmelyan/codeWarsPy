class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next is None:
            return str(self.data)
        return '{} -> {}'.format(str(self.data), self.next)


def front_back_split(source, front, back):
    list_len = get_list_len(source)
    if list_len < 2:
        raise Exception

    if list_len == 2:
        front.next = source.next
        front.data = source.data
        back.next = front.next.next
        back.data = front.next.data
        front.next = None
        return

    f = source
    b = source

    temp = None

    for i in range(int(list_len / 2 + 0.6)):
        temp = b
        b = b.next
    temp.next = None

    front.next = f.next
    front.data = f.data
    back.next = b.next
    back.data = b.data


def get_list_len(source):
    if source is None:
        return 0
    if source.next is None:
        return 1
    return get_list_len(source.next) + 1


def build_list(lis):
    start = Node(0)
    node = start

    for l in lis:
        node.next = Node(l)
        node = node.next

    return start.next


node = Node()
n = Node()
source = build_list([1, 3])
front_back_split(source, node, n)
print('{} ; {}'.format(node, n))

node = Node()
n = Node()
source = build_list([1, 2, 3])
front_back_split(source, node, n)
print('{} ; {}'.format(node, n))

node = Node()
n = Node()
source = build_list([1, 2, 3, 4, 5, 6])
front_back_split(source, node, n)
print('{} ; {}'.format(node, n))

node = Node()
n = Node()
source = build_list([1, 2, 3, 4, 5, 6, 7])
front_back_split(source, node, n)
print('{} ; {}'.format(node, n))
