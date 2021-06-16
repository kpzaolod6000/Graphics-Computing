import vtk

class clouds:
    
    def Setnform(self,resolution_1,resolution_2,scalX,scalY,scalZ):
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
    
    def SetActornform(self,mapperforma,r,g,b,posX,posY,posZ,rotate):
        
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapperforma)
        self.actor.GetProperty().SetColor(r,g,b)
        self.actor.SetPosition(posX,posY,posZ)
        self.actor.RotateZ(rotate)
        return self.actor