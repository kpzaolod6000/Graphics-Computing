import vtk
import random
import house as h
import arbol as abl
import nube as nube
import sol

# source
## Arbol
### Tronco y Hojas
tree = abl.Tree()

## Casa
house = h.House()

## Sol
sun = sol.Sun()

##nube
nube = nube.clouds()

# mapper
## Arbol
### Tronco
mapperTrunk = tree.SetTrunk(0.3,2.6,50)#radio,height,resolution

### Hojas
mapperLeaf = tree.SetLeaf(0.3,500)#radio,resolution

## Casa
mapperChapa = house.SetSphere(0.1)#radio
mapperCone = house.SetCone(1.9,1.6,20)#radio,height,resolution
mapperCube1 = house.SetCube(2.5,2.5,2.5)#cuerpo
mapperCube2 = house.SetCube(1.2,1.8,0.2)#puerta
mapperCube3 = house.SetCube(0.1,1.1,1.4)#ventana

## Cerros
mapperCerro1 = house.SetCone(10.0,15.0,60)#radio,height,resolution

## Sol
mapperSol = sun.SetSphere(2,50)#radio
###Lineas del sol
mapperLineas = sun.SetLineas(22,20,1.5,0.5,0.5)#resolution_1,resolution_2,scalX,scalY,scalZ


# actor
## Sol
actorSol = sun.SetActorSphere(mapperSol,1,1,0,0,10,-40)#mapperSphere,r,g,b,posX,posY,posZ
###Lineas del sol

actorLinea1 = sun.SetActorLineas(mapperLineas,1,1,0,3,10,-40,0.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate
actorLinea2 = sun.SetActorLineas(mapperLineas,1,1,0,-3,10,-40,0.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate
actorLinea3 = sun.SetActorLineas(mapperLineas,1,1,0,2,13,-40,45.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate
actorLinea4 = sun.SetActorLineas(mapperLineas,1,1,0,-2,13,-40,135.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate
actorLinea5 = sun.SetActorLineas(mapperLineas,1,1,0,2,7,-40,315.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate
actorLinea6 = sun.SetActorLineas(mapperLineas,1,1,0,-2,7,-40,225.0)#mapperSphere,r,g,b,posX,posY,posZ,rotate

######################nubes


mappernubes=nube.Setnform(20,20,6,2,2)

actornube1 = nube.SetActornform(mappernubes,0,0,1,15,15,-30,0.1)
actornube2 = nube.SetActornform(mappernubes,0,0,1,8,14,30,1.3)
actornube3 = nube.SetActornform(mappernubes,0,0,1,-1,14,-18,-1.-2)
actornube4 = nube.SetActornform(mappernubes,0,0,1,-8.5,11,15,0.0)
actornube5 = nube.SetActornform(mappernubes,0,0,1,-15.2,14,6,0.0)
######################


## Cerros
actorCerro1 = house.SetActorCube(mapperCerro1,11/255, 83/255, 69/255 ,7.0,5.0,-30.0)#color and pos
actorCerro2 = house.SetActorCube(mapperCerro1,11/255, 83/255, 69/255 ,-7.0,5.0,-30.0)#color and pos

## Casa
### Cube
actorCube1 = house.SetActorCube(mapperCube1,235/255, 161/255, 52/255,0,0,0)#color and pos
actorCube2 = house.SetActorCube(mapperCube2,235/255, 116/255, 52/255,0.0,-0.3,1.5)#color and pos
actorCube3 = house.SetActorCube(mapperCube3,130/255, 185/255, 189/255,-1.5,0,0)#color and pos

### Cone
actorCone = house.SetActorCube(mapperCone,142/255, 156/255, 151/255,0,2.0,0)#color and pos

### Chapa
actorChapa = house.SetActorCube(mapperChapa,99/255, 87/255, 22/255,-0.4,-0.3,1.6)#color and pos

## Arbol
### Tronco
actorTrunk = tree.SetActorTrunk(mapperTrunk,2,0.0,1.5)#mapperTrunk,posx,posy,posz
actorTrunk2 = tree.SetActorTrunk(mapperTrunk,-2,0.0,1.5)#mapperTrunk,posx,posy,posz

###Hojas
#establecer las esferas
arraySphere = tree.SetTree(50,2,1.6,1.5)#cantidad,posx,posy,posz raiz
arraySphere2 = tree.SetTree(25,-2,1.6,1.5)#cantidad,posx,posy,posz raiz

#axes
transform = vtk.vtkTransform()
transform.Translate(1.5, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)

renderer.AddActor(actorSol)
renderer.AddActor(actorTrunk)
renderer.AddActor(actorTrunk2)
for pointLeaf in arraySphere:
    actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
    renderer.AddActor(actorLeaf_aux)
for pointLeaf in arraySphere2:
    actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
    renderer.AddActor(actorLeaf_aux)
#renderer.AddActor(axes)
## Casa
renderer.AddActor(actorCube1)
renderer.AddActor(actorCube2)
renderer.AddActor(actorCube3)
renderer.AddActor(actorCone)
renderer.AddActor(actorChapa)
renderer.AddActor(actorCerro1)
renderer.AddActor(actorCerro2)
## sol
renderer.AddActor(actorLinea1)
renderer.AddActor(actorLinea2)
renderer.AddActor(actorLinea3)
renderer.AddActor(actorLinea4)
renderer.AddActor(actorLinea5)
renderer.AddActor(actorLinea6)
###########nube 
renderer.AddActor(actornube1)
renderer.AddActor(actornube2)
renderer.AddActor(actornube3)
renderer.AddActor(actornube4)
renderer.AddActor(actornube5)


###### Estableciendo mas arboles
quantityTree = 1
for i in range(quantityTree):
    positionX=random.uniform(-30,30)
    positionZ=random.uniform(-30,30)
    while(positionX >= -2.5 and positionX <=2.5):
        positionX=random.uniform(-30,30)
    while(positionZ >= -2.5 and positionZ <=2.5):
        positionZ=random.uniform(-30,30)

    actorTrunk_aux = tree.SetActorTrunk(mapperTrunk,positionX,0.0,positionZ)
    quantityLeaf=random.randint(5,30)
    arraySphere_aux = tree.SetTree(quantityLeaf,positionX,1.6,positionZ)
    renderer.AddActor(actorTrunk_aux)
    for pointLeaf in arraySphere_aux:
        actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
        renderer.AddActor(actorLeaf_aux)



 


#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
