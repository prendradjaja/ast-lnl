import ast
import astor

def myeval(s):
    """
    >>> myeval('1 + 2 * 3')
    9
    """

    # step 1. string replacement
    s = (s.replace('+',    'temp')
       .replace('*',    '+')
       .replace('temp', '*'))

    # step 2. parse
    tree = ast.parse(s)

    # step 3. node replacement
    # print(astor.dump_tree(tree))
    traverse(tree)

    # step 4. dump / eval
    code = astor.to_source(tree)
    return eval(code)
    # Be careful with eval in real life -- don't give it user-provided data, or you'll get
    # code injection vulnerabilities. Usually best to avoid it entirely...

def traverse(tree):
    # In real life, you'd probably use ast.NodeTransformer instead of implementing a
    # traversal yourself

    # print(tree)
    if isinstance(tree, ast.Module):
        for node in tree.body:
            traverse(node)
    elif isinstance(tree, ast.Expr):
        traverse(tree.value)
    elif isinstance(tree, ast.BinOp):
        # swap the op
        if isinstance(tree.op, ast.Add):
            tree.op = ast.Mult()
        elif isinstance(tree.op, ast.Mult):
            tree.op = ast.Add()
        else:
            print('invalid op', tree.op)
            exit()

        # traverse
        traverse(tree.left)
        traverse(tree.right)

print(myeval('1 + 2 * 3'))
