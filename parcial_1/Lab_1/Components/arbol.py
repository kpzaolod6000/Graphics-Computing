import vtk

# source
cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(12)
cylinder.SetHeight(70)
cylinder.SetResolution(50)
cylinder.Update()

#hojas
valcen = 21
centro = vtk.vtkSphereSource()
centro.SetRadius(valcen)
centro.Update()

#

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(cylinder.GetOutput())

#hojas
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(centro.GetOutput())

#

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(.3,.2,.1)
actor.RotateX(20.0)
actor.SetPosition(10,-30,0)

#esferas

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(0.0, 1.0, 0.0)
actor2.SetPosition(30,10,10)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper2)
actor3.GetProperty().SetColor(0.0, 1.0, 0.0)
actor3.SetPosition(-10,10,10)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper2)
actor4.GetProperty().SetColor(0.0, 1.0, 0.0)
actor4.SetPosition(10,7,25)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper2)
actor5.GetProperty().SetColor(0.0, 1.0, 0.0)
actor5.SetPosition(10,15,-7)

actor6 = vtk.vtkActor()
actor6.SetMapper(mapper2)
actor6.GetProperty().SetColor(0.0, 1.0, 0.0)
actor6.SetPosition(10,30,10)

#
#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(actor6)
#


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
