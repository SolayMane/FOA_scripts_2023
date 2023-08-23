import ete3
from ete3 import TextFace, Tree,faces, AttrFace, TreeStyle, NodeStyle
import sys
import glob

treefile = sys.argv[1]
outName = sys.argv[2]
outgroup = sys.argv[3]
#read the file
#inputdire = sys.argv[1]
#outputName = 'example' # we can get that from user input
# read the tree files
t = Tree(treefile)

# set the outgroup, we can take that from user input, Dickeya_dadantii_3937 is an example

def layout(node):
    if node.is_leaf():
        N = AttrFace("name", fsize=10)
        faces.add_face_to_node(N, node, 0)
#        F = AttrFace("support", fsize=30)
#        faces.add_face_to_node(F, node, 0, position="branch-top")




t.set_outgroup(outgroup)

ts = TreeStyle()
ts.layout_fn = layout
ts.show_leaf_name = False
ts.show_branch_support = True
ts.mode = "r"
#ts.root_opening_factor = 1


# save the results as png  or pdf
t.render(outName + ".pdf", w=1800, units="px",tree_style=ts)

