import maya.cmds as cmds

selectionList = cmds.ls( selection=True, type='transform' )

if len( selectionList ) >=2:
    
    targetName = selectionList[0]
    selectionList.remove( targetName )
    
    locatorGroupName = cmds.group( empty=True, name='expansion_loc_group#' )
    maxExpansion=100
    newAttrName='expansion'
    
    if not cmds.objExists( '%s.%s' % (targetName, newAttrName) ):
        cmds.select( targetName )
        cmds.addAttr( longName='expansion', shortName='exp',
                      attributeType='double', min=0, max=maxExpansion,
                      defaultValue=maxExpansion, keyable=True )
    
    for obj in selectionList:
        
        coords = cmds.getAttr( '%s.translate' % (obj) )[0]
        locatorName = cmds.spaceLocator( position=coords, name='%s_loc#' % (obj) )[0]
        cmds.xform( locatorName, centerPivots=True )
        cmds.parent( locatorName, locatorGroupName )
        
        pointConstraintName = cmds.pointConstraint( [ targetName, locatorName ], obj, name='%s_pointConstraint#' % (obj) )[0]

        cmds.expression( alwaysEvaluate=True,
                         name='%s_exp#' % (obj),
                         object=pointConstraintName,
                         string='%sW0 = %s - %s.%s' % (targetName, maxExpansion, targetName, newAttrName) )

        cmds.connectAttr( '%s.%s' % (targetName, newAttrName),
                          '%s.%sW1' % (pointConstraintName, locatorName) )
        
    cmds.xform( locatorGroupName, centerPivots=True )
    
    
else:
    print 'Please select atleast two items'       