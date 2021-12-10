from  graphviz import Digraph
from graphviz import Graph

'''
'''
def graphviz_play():
    dot = Digraph()

    dot.node("A", "ka")

    dot.node("B", "BW")
    dot.node("C", "LC")

    dot.edges(['AB', 'AC'])
    # print (dot.source)
    # dot.render (dot.source)

    g = Graph(format='png')

    dot.format = 'svg'
    dot.render()


import git
git_dir = r"D:\work\GIT\main"
g = git.cmd.Git(git_dir)
st = g.status()
print (st)

'''
'''
def myd(sad):
    print (sad)