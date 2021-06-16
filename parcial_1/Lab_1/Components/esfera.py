import vtk

# source
valcen = 21
sol = vtk.vtkSphereSource()
sol.SetRadius(valcen)
sol.Update()

#lineas sol
linea1 = vtk.vtkSphereSource()
linea1.SetThetaResolution(22)
linea1.SetPhiResolution(20)


#transformacion
trans = vtk.vtkTransform()
trans.Scale(23, 10, 15)

transfilter = vtk.vtkTransformFilter()
transfilter.SetInputConnection(linea1.GetOutputPort())
transfilter.SetTransform(trans)

trans2 = vtk.vtkTransform()
trans2.Scale(23,10,15)

transfilter2 = vtk.vtkTransformFilter()
transfilter2.SetInputConnection(linea1.GetOutputPort())
transfilter2.SetTransform(trans2)


# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(sol.GetOutput())

mapper2 = vtk.vtkDataSetMapper()
mapper2.SetInputConnection(transfilter.GetOutputPort())

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1,1,0)
actor.SetPosition(1,1,1)


actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(1,1,0)
actor2.SetPosition(30,10,10)
actor2.RotateZ(20.0)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper2)
actor3.GetProperty().SetColor(1,1,0)
actor3.SetPosition(1,32,10)
actor3.RotateZ(90.0)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper2)
actor4.GetProperty().SetColor(1,1,0)
actor4.SetPosition(1,-32,5)
actor4.RotateZ(90.0)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper2)
actor5.GetProperty().SetColor(1,1,0)
actor5.SetPosition(-30,-10,5)
actor5.RotateZ(20.0)

actor6 = vtk.vtkActor()
actor6.SetMapper(mapper2)
actor6.GetProperty().SetColor(1,1,0)
actor6.SetPosition(-30,15,5)
actor6.RotateZ(-20.0)

actor7 = vtk.vtkActor()
actor7.SetMapper(mapper2)
actor7.GetProperty().SetColor(1,1,0)
actor7.SetPosition(30,-17,5)
actor7.RotateZ(-20.0)
#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(actor6)
renderer.AddActor(actor7)
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

