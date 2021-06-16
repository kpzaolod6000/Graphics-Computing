import vtk

class House:

    def SetSphere(self,radio):      
        self.chapa = vtk.vtkSphereSource()
        self.chapa.SetRadius(radio)
        self.chapa.Update()
        #mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.chapa.GetOutput())
        return mapper
        
    def SetCone(self,radio,height,resolution):
        self.cone = vtk.vtkConeSource()
        self.cone.SetRadius(radio)
        self.cone.SetHeight(height)
        self.cone.SetResolution(resolution)
        self.cone.SetDirection(0,1,0)
        self.cone.Update()
        #mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.cone.GetOutput())
        return mapper

    def SetCube(self,x,y,z):
        self.cube = vtk.vtkCubeSource()
        self.cube.SetXLength(x)
        self.cube.SetYLength(y)
        self.cube.SetZLength(z)
        self.cube.Update()
        #mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.cube.GetOutput())
        return mapper

    def SetActorCube(self,mapperCube,r,g,b,posX,posY,posZ):
        actor = vtk.vtkActor()
        actor.SetMapper(mapperCube)
        actor.GetProperty().SetColor( r,g,b,)
        actor.SetPosition(posX,posY,posZ)
        return actor
    
    def SetActorSphere(self,mapperSphere,r,g,b,posX,posY,posZ):
        actor = vtk.vtkActor()
        actor.SetMapper(mapperSphere)
        actor.GetProperty().SetColor(r,g,b)
        actor.SetPosition(posX,posY,posZ)
        return actor
    def SetActorCone(self,mapperCone,r,g,b,posX,posY,posZ):
        actor = vtk.vtkActor()
        actor.SetMapper(mapperCone)
        actor.GetProperty().SetColor(r,g,b)
        actor.SetPosition(posX,posY,posZ)
        return actor



