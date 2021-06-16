import vtk

class Sun:

    def SetSphere(self,radio,resolution):      
        self.sol = vtk.vtkSphereSource()
        self.sol.SetRadius(radio)
        self.sol.SetPhiResolution(resolution)
        self.sol.SetThetaResolution(resolution)
        self.sol.Update()

        #mapper
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputData(self.sol.GetOutput())
       
        return self.mapper
        
    def SetLineas(self,resolution_1,resolution_2,scalX,scalY,scalZ):
        self.linea = vtk.vtkSphereSource()
        self.linea.SetThetaResolution(resolution_1)
        self.linea.SetPhiResolution(resolution_2)
        self.linea.Update()

        #transformacion
        self.trans = vtk.vtkTransform()
        self.trans.Scale(scalX,scalY,scalZ)

        self.transfilter = vtk.vtkTransformFilter()
        self.transfilter.SetInputConnection(self.linea.GetOutputPort())
        self.transfilter.SetTransform(self.trans)

        #mapper
        self.mapper = vtk.vtkDataSetMapper()
        self.mapper.SetInputConnection(self.transfilter.GetOutputPort())
        return self.mapper
 
    def SetActorSphere(self,mapperSphere,r,g,b,posX,posY,posZ):

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapperSphere)
        self.actor.GetProperty().SetColor(r,g,b)
        self.actor.SetPosition(posX,posY,posZ)
        return self.actor
    
    def SetActorLineas(self,mapperLineas,r,g,b,posX,posY,posZ,rotate):
        
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapperLineas)
        self.actor.GetProperty().SetColor(r,g,b)
        self.actor.SetPosition(posX,posY,posZ)
        self.actor.RotateZ(rotate)
        return self.actor
 
