import maya.cmds as cmds
import random

selectionList = cmds.ls(orderedSelection=True)

if len( selectionList ) >= 2:
    
    targetName = selectionList[0]
    selectionList.remove(targetName)
    
    for objectName in selectionList:
        
        print '%s aim at %s' % (objectName, targetName)
        cmds.aimConstraint(targetName, objectName, aimVector=[0,1,0] )
else:
    print "select atleast two object"