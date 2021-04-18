import vtk
import math

#Equation
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class BuildTree:
    def __init__(self,quantity,topbyNivel,center):#center = radio
        self.leaf = False
        self.quantity = quantity
        self.tope = 4
        self.topbyNivel = topbyNivel
        self.point
        self.center  = center
    def insert(self,pointNew):
        #new_point = Point(x,y,z)
        self.point = pointNew

        for item in range(item,topbyNivel+1):
            cont = 0;
            if(self.quantity >= 4**item):
                self.quantity = self.quantity - 4


        self.quantity  -= 1
        #self.point.append(new_point)
        #if(self.topbyNivel >= 4):
        if(self.quantity >= 4):
            #updateP = Point(pointNew.x,pointNew.y,pointNew.z)
            #for i in range(self.leaf):
                
            
            self.leafXPos = BuildTree(self.quantity,self.topbyNivel,self.center)
            self.leafXNeg = BuildTree(self.quantity,self.topbyNivel,self.center)
            self.leafZPos = BuildTree(self.quantity,self.topbyNivel,self.center)
            self.leafZNeg = BuildTree(self.quantity,self.topbyNivel,self.center)
            self.leafXPos.leaf = True
            self.leafXNeg.leaf = True
            self.leafZPos.leaf = True
            self.leafZNeg.leaf = True
            
            self.leafXPos.insert(Point(self.point.x + self.center,self.point.y - self.center*2,self.point.z))
            self.leafXNeg.insert(Point(self.point.x - self.center,self.point.y-self.center*2,self.point.z))
            self.leafZPos.insert(Point(self.point.x,self.point.y-self.center*2,self.point.z + self.center))
            self.leafZNeg.insert(Point(self.point.x,self.point.y-self.center*2,self.point.z - self.center))


# source
## Tronco
cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(0.2)
cylinder.SetHeight(1.3)
cylinder.SetResolution(50)
cylinder.Update()

## Hojas
sphere = vtk.vtkSphereSource()
sphere.SetRadius(0.3)

 # Make the surface smooth.
sphere.SetPhiResolution(500)
sphere.SetThetaResolution(500)
sphere.Update()
# mapper
## Tronco
mapperTrunk = vtk.vtkPolyDataMapper()
mapperTrunk.SetInputData(cylinder.GetOutput())

## Hojas
mapperLeaf = vtk.vtkPolyDataMapper()
mapperLeaf.SetInputData(sphere.GetOutput())

#actor
## Tronco
actorTrunk = vtk.vtkActor()
actorTrunk.SetMapper(mapperTrunk)
actorTrunk.GetProperty().SetColor(86/255, 47/255, 47/255)
#actorTrunk.RotateX(20.0)
actorTrunk.SetPosition(0.0,0.0,0.0)#(x,y,z)

##Hojas
#establecer el numero de esferas
quantitySphere = 341
topbyNivel = int(math.log(quantitySphere,4)) #altura del arbol 4^n
dia = 0.6
point = Point(0.0,0.8+(dia * topbyNivel),0.0) #maxima altura

actorLeaf = vtk.vtkActor()
actorLeaf.SetMapper(mapperLeaf)
actorLeaf.GetProperty().SetColor(0.0, 1.0, 0.0)
actorLeaf.SetPosition(point.x,point.y,point.z)

arraySphere = []
quantitySphere -=1
#for quantitySphere in range(quantitySphere-1):
indexArray = 0
for quantityNivel in range(1,topbyNivel+1):
    qSphereSave = 4**quantityNivel
    if (quantitySphere >= qSphereSave):
        quantitySphere -= qSphereSave
        if (len(arraySphere) == 0):
            pointXPos = Point(0.3,(0.8+(dia * topbyNivel)-dia),0.0)
            pointXNeg = Point(-0.3,(0.8+(dia * topbyNivel)-dia),0.0) 
            pointZPos = Point(0.0,(0.8+(dia * topbyNivel)-dia),0.3) 
            pointZNeg = Point(0.0,(0.8+(dia * topbyNivel)-dia),-0.3) 
            arraySphere.append(pointXPos)
            arraySphere.append(pointXNeg)
            arraySphere.append(pointZPos)
            arraySphere.append(pointZNeg)
        
        else:
            for i in range(indexArray,len(arraySphere)):
                pointXPos = Point(arraySphere[i].x+0.3,arraySphere[i].y-dia,arraySphere[i].z)
                pointXNeg = Point(arraySphere[i].x-0.3,arraySphere[i].y-dia,arraySphere[i].z)
                pointZPos = Point(arraySphere[i].x,arraySphere[i].y-dia,arraySphere[i].z+0.3)
                pointZNeg = Point(arraySphere[i].x,arraySphere[i].y-dia,arraySphere[i].z-0.3)
                arraySphere.append(pointXPos)
                arraySphere.append(pointXNeg)
                arraySphere.append(pointZPos)
                arraySphere.append(pointZNeg)
            indexArray = 4**(quantityNivel-1)
        
     #   else:
            
    #else:

    

#tree = BuildTree(quantitySphere-1,topbyNivel,0.3)#radio
#tree.insert(point)





#axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actorTrunk)
renderer.AddActor(actorLeaf)
for pointLeaf in arraySphere:
    actorLeaf_aux = vtk.vtkActor()
    actorLeaf_aux.SetMapper(mapperLeaf)
    actorLeaf_aux.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorLeaf_aux.SetPosition(pointLeaf.x,pointLeaf.y,pointLeaf.z)

    renderer.AddActor(actorLeaf_aux)
renderer.AddActor(axes)

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
