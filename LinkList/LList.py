# -*- coding: utf8 -*-


class Node(object):
    def __init__(self, date):
        self._date = date
        self._next = None

    @property
    def payload(self):
        return self._date

    @payload.setter
    def payload(self, date):
        self._date = date

    @property
    def link(self):
        return self._next

    @link.setter
    def link(self, new_link):
        self._next = new_link

    def __str__(self):
        return str(self._date)

    def __repr__(self):
        return str(self._date)


class LinkingList(object):
    def __init__(self):
        self._size = 0
        self._root = None

    def add(self, date):
        if not self._root:
            self._root = Node(date)
        else:
            temp = Node(date)
            temp.link = self._root
            self._root = temp
        self._size += 1

    def __len__(self):
        return self._size

    def __iter__(self):
        curr = self._root
        while curr:
            yield curr.payload
            curr = curr.link

    def is_list(self, find):
        return find in self


if __name__ == '__main__':
    LL = LinkingList()
    LL.add(123)

