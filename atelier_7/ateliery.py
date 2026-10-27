import maya.cmds as cmds 


#on a besoin de selectionner lobjet avant de lancer le script
objet = cmds.ls(selection = True)

#erase previous keyframes
cmds.cutKey(objet, clear=True)

min = 1
max = 50
valueend = 50

#set keyframes
cmds.setKeyframe(objet, attribute="translateY", time=min, value=1)
cmds.setKeyframe(objet, attribute="translateY", time=(max/2), value=valueend)
cmds.setKeyframe(objet, attribute="translateY", time=max, value=1)

#control how long the animation will be played
cmds.playbackOptions(edit=True, min=min, max=max)
cmds.playbackOptions(edit=True, animationEndTime=max)


