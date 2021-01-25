import ast
import astor

tree = ast.parse(open('parse-me').read())
# Printing the parsed tree object is a bit opaque
print(tree)

# astor (third-party) gives nice pretty-printing
print(astor.dump_tree(tree))

# You can navigate the tree like this (I learned about .body, .targets etc by
# looking at the pretty-printed output, not documentation
print(tree.body[0].targets[0].id)

# You can turn the tree back into source code like this
print(astor.to_source(tree))

# You can modify the tree and then turn it back into source code
tree.body[0].targets[0].id = 'newvarname'
print(astor.to_source(tree))  # Notice that this new program would now error. Be careful!
