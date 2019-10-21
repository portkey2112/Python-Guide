class Trie:
    def __init__(self, character, level):
        self.character = character
        self.children = {}
        for it in range(0, 26):
            self.children[chr(97 + it)] = None
        self.level = level
        self.word_or_not = False
        return


def insert_into_trie(current_node, given_string, it):
    # given_string is in lower case, already
    # it : the index of character currently being processed
    current_char = given_string[it]
    if current_node.children[current_char] is None:
        current_node.children[current_char] = Trie(current_char, current_node.level + 1)
    it += 1
    current_node = current_node.children[current_char]
    if it == len(given_string):
        current_node.word_or_not = True
        return
    insert_into_trie(current_node, given_string, it)


def level_order_traversal(start_node):
    queue = [start_node]
    current_level = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        for it in range(0, 26):
            if current_node.children[chr(97 + it)] is None:
                continue
            queue.append(current_node.children[chr(97 + it)])
        text = "{0}{1}".format(current_node.character, "T" if current_node.word_or_not else "")
        if not current_node.level == current_level:
            current_level = current_node.level
            text = "\n{0}".format(text)
        print(text, end="\t")
    print()


def search_word(start_node, val):
    current_node = start_node
    for it in val:
        if current_node.children[it] is None:
            return False
        current_node = current_node.children[it]
    return current_node.word_or_not


if __name__ == '__main__':
    root_of_trie = Trie(None, 0)
    while True:
        string = input("String : ").lower()
        if string.__eq__("exit999"):
            break
        if not string.isalpha():
            print("{0} SKIPPED".format(string))
            continue
        insert_into_trie(root_of_trie, string, 0)
    level_order_traversal(root_of_trie)
    while True:
        string = input("String : ").lower()
        if string.__eq__("exit999"):
            break
        if not string.isalpha():
            print("{0} SKIPPED".format(string))
            continue
        print("Is it in TRIE : {0}".format(search_word(root_of_trie, string)))


# as you insert words into the TRIE,
# the node where a complete word forms will have a TRUE marked on it.
