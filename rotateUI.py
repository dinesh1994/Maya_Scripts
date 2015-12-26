import maya.cmds as cmds
import functools

def createUI( wName, applyCallBack ):

	windowId = 'myWindowID'

	if cmds.window( windowId, exists=True ):
		cmds.deleteUI( windowId )

	cmds.window( windowId, title=wName, sizeable=False, resizeToFitChildren=True )
	cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[ (1,75), (2,60), (3,60) ], columnOffset=[ (1,'right',3) ] )
	cmds.text( label='Time Range:' )
	
	startTimeField = cmds.intField( value=cmds.playbackOptions( q=True, minTime=True ) )
	endTimeField = cmds.intField( value=cmds.playbackOptions( q=True, maxTime=True ) )
	
	cmds.text( label='Attribute:' )
	rotAxisField = cmds.textField( text='rotateY' )
	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )
	
	#functools.partial delay the execution of applyCallBsck till apply button is placed
	cmds.button( label='Apply', command=functools.partial( applyCallBack, 
	                                                       startTimeField,
	                                                       endTimeField, 
	                                                       rotAxisField) )
	
	def cancelCallBack( *args ):
	    if cmds.window( windowId, exists=True ):
	        cmds.deleteUI( windowId )
	        
	cmds.button( label='cancel', command=cancelCallBack )
	cmds.showWindow()
	
def applyCallBack( startTimeField, endTimeField, rotAxisField, *args ):
    
    startTime = cmds.intField( startTimeField, query=True, value=True )
    endTime = cmds.intField( endTimeField, query=True, value=True )
    rotAxis = cmds.textField( rotAxisField, query=True, text=True )
    
    print 'startTime = ' + str(startTime)
    print 'endTime = ' + str(endTime)
    print 'rotAxis = %s' % (rotAxis)

createUI( 'testWindow', applyCallBack )