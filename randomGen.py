import maya.cmds as cmds
import random

random.seed( 1234 )

result = cmds.ls(orderedSelection = True)

transformName = result[0]
instanceGroupName = cmds.group(empty=True, name=transformName + '_instance_group#')

for i in range(0, 50):
	
	instanceResult = cmds.instance(transformName, name=transformName + '_instance#')
	cmds.parent(instanceResult, instanceGroupName)

	x = random.uniform(-50, 50)
	y = random.uniform(0, 100)
	z = random.uniform(-100, 80)

	cmds.move(x, y, z, instanceResult)

	rotx = random.uniform(0, 360)
	roty = random.uniform(0, 180)
	rotz = random.uniform(90, 270)

	cmds.rotate(rotx, roty, rotz, instanceResult)
 	
	scalefactor = random.uniform(0.5, 1.5)

	cmds.scale(scalefactor, instanceResult)

cmds.hide(transformName)