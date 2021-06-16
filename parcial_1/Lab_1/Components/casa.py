import vtk

chapa = vtk.vtkSphereSource()
chapa.SetRadius(0.7)
chapa.Update()

cone = vtk.vtkConeSource()
cone.SetRadius(14)
cone.SetHeight(15)
cone.SetResolution(50)
cone.Update()

monte1 = vtk.vtkConeSource()
monte1.SetRadius(50)
monte1.SetHeight(80)
monte1.SetResolution(50)
monte1.Update()

monte2 = vtk.vtkConeSource()
monte2.SetRadius(50)
monte2.SetHeight(80)
monte2.SetResolution(50)
monte2.Update()

cube1 = vtk.vtkCubeSource()
cube1.SetXLength(20)
cube1.SetYLength(20)
cube1.SetZLength(20)
cube1.Update()

cube2 = vtk.vtkCubeSource()
cube2.SetXLength(8)
cube2.SetYLength(1)
cube2.SetZLength(15.5)
cube2.Update()

cube3 = vtk.vtkCubeSource()
cube3.SetXLength(1)
cube3.SetYLength(7)
cube3.SetZLength(5)
cube3.Update()

#mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cube1.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube2.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(cube3.GetOutput())

mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputData(cone.GetOutput())

mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputData(chapa.GetOutput())


mapper6 = vtk.vtkPolyDataMapper()
mapper6.SetInputData(monte1.GetOutput())

mapper7 = vtk.vtkPolyDataMapper()
mapper7.SetInputData(monte2.GetOutput())
#actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor( 235/255, 161/255, 52/255)
actor1.SetPosition(0,0,0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(235/255, 116/255, 52/255)
actor2.SetPosition(0,11,-2.2)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(130/255, 185/255, 189/255)
actor3.SetPosition(11,0,0)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.GetProperty().SetColor(142/255, 156/255, 151/255)
actor4.RotateY(-90)
actor4.SetPosition(0,0,17.5)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.GetProperty().SetColor(99/255, 87/255, 22/255)
actor5.SetPosition(3.5,12,-1)

actor6 = vtk.vtkActor()
actor6.SetMapper(mapper6)
actor6.RotateY(-90)
actor6.GetProperty().SetColor(92/255, 60/255, 35/255)
actor6.SetPosition(0,-70,30)


actor7 = vtk.vtkActor()
actor7.SetMapper(mapper7)
actor7.RotateY(-90)
actor7.GetProperty().SetColor(92/255, 60/255, 35/255)
actor7.SetPosition(-30,-70,30)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor1)
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