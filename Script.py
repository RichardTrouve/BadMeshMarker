import maya.cmds as cmds

if cmds.window("marker", exists = True):
    cmds.deleteUI("marker")

myWindow = cmds.window("marker",t="Bad Mesh Marker",w =300,h= 300)
cmds.columnLayout(adj = True)
cmds.separator( height=10, style='double')
cmds.button( l='N-Gons', c= "marker()")
cmds.button( l='Clear Outliner Colors', c= "clearOutlineColor()" )
cmds.showWindow(myWindow)

#---------------------------------------------

def marker():
    objects = cmds.ls( typ='mesh',)
    geo = cmds.listRelatives(objects, parent=True, fullPath=True)
    marked = 0
    
    for item in geo :
        cmds.select (item)
        cmds.selectMode(q=True, co=True)
        cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=3)
        cmds.polySelectConstraint(dis=True)
        badPolys = cmds.polyEvaluate(fc=True)
        if not badPolys == 0:
            cmds.setAttr ( item + ".useOutlinerColor" , True)
            cmds.setAttr ( item + ".outlinerColor" , 1,0,0)
    
    cmds.select(clear=True)

#---------------------------------------------

def clearOutlineColor():
    objects = cmds.ls( typ='mesh',)
    geo = cmds.listRelatives(objects, parent=True, fullPath=True)
    print 
    
    for item in geo:
        cmds.select (item)
        cmds.setAttr ( item + ".useOutlinerColor" , False)
        cmds.setAttr ( item + ".outlinerColor" , 0,0,0)
        cmds.select (clear= True)    

