class Triehugger(object):
    def __init__(self, val="", parent=None, store=True):
        self.val = val
        self.children = {}
        self.parent = parent
        self.store = store

    def add(self, val):
        self.add_help(val, 0)

    def add_help(self, val, idx):
        if idx == len(val):
            return
        cur = val[:idx+1]
        if cur not in self.children:
            # Only store final leaf node
            new_node = Triehugger(val=cur, parent=self, store=True if idx == len(val)-1 else False)
            self.children[cur] = new_node
        # Node already exists! In that case, if we are at the final word in our recursion,
        # store the existing node
        elif idx == len(val)-1:
            self.children[cur].store = True
        child = self.children[cur]
        child.add_help(val, idx+1)

    def delete(self, val):
        self.delete_help(val, 0)

    def delete_help(self, val, idx):
        if val in self.children:
            del self.children[val]
            # Incrementally do GC work after each delete
            self.garbage_collect()
        else:
            cur = val[:idx+1]
            if cur in self.children:
                child = self.children[cur]
                child.delete_help(val, idx+1)

    def garbage_collect(self):
        if not self:
            return
        parent = self.parent
        # If current self has no siblings and marked no-store, delete it
        if len(parent.children) == 1 and not self.store:
            del parent.children[self.val]
            parent.garbage_collect()

    def __repr__(self):
        return self.display(0)

    def display(self, indent):
        lines = [" " * indent + "- " + self.val]
        for child in self.children.values():
            lines.append(child.display(indent + 1))
        return "\n".join(lines) if lines else ""

if __name__ == "__main__":
    # Example usage
    triehugger = Triehugger()
    triehugger.add("beets")
    triehugger.add("beetle")
    triehugger.add("beetlejuice")
    print(triehugger)
    triehugger.delete("beetlejuice")
    print(triehugger)

