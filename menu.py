def Revealexplr():
     import os
     a=nuke.selectedNode()
     b=a['file'].value()
     u=os.path.split(b)[0]
     u = os.path.normpath(u)
     print u
     cmd = "caja %s" % (u)
     print cmd
     os.system(cmd)
nuke.menu( 'Nodes' ).addCommand( 'Other/FileOpen', "Revealexplr()", 'shift+q')