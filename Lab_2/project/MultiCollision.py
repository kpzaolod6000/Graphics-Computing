import vtk
import math

class MySphere:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius    
        self.velocity = [0,-10,0] # la esfera cae, por eso tiene una velocida hacia abajo
        self.last_velocity = [0,-10,0]
        self.actor = None

class MyFloor:
    def __init__(self, pos, height,posWalls):
        self.pos = pos
        self.height = height    
        self.actor = None
        self.posWalls = posWalls

sphere = MySphere([0,2.5,0], 2)
floor = MyFloor([0,0,0],1,20)
time = 0
g = 9.8
#height = abs(floor.pos[1] - sphere.pos[1]) # = (1/2)*g*time^2

def set_initial_position():
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    floor_actor.SetPosition(floor.pos[0], floor.pos[1], floor.pos[2])
    wallXPos_actor.SetPosition(floor.posWalls-0.5,1,0)
    wallXNeg_actor.SetPosition(-floor.posWalls+0.5,1,0)
    wallZPos_actor.SetPosition(0,1,floor.posWalls-0.5)
    wallZNeg_actor.SetPosition(0,1,-floor.posWalls+0.5)


def callback_func(caller, timer_event):
    global time

    dist = g*(time**2)
    sphere.pos[0] += dist
    sphere.pos[2] += dist
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])           
    time += 0.001
    render_window.Render()


# source
##sphere
sourceSphere = vtk.vtkSphereSource()
sourceSphere.SetThetaResolution(50)
sourceSphere.SetRadius(sphere.radius)
sourceSphere.Update()

##floor
sourceFloor = vtk.vtkCubeSource()
sourceFloor.SetXLength(40)
sourceFloor.SetYLength(floor.height)
sourceFloor.SetZLength(40)
sourceFloor.Update()

##wall
sourceWallX = vtk.vtkCubeSource()
sourceWallX.SetXLength(floor.height)
sourceWallX.SetYLength(floor.height)
sourceWallX.SetZLength(40)
sourceWallX.Update()

sourceWallZ = vtk.vtkCubeSource()
sourceWallZ.SetXLength(40)
sourceWallZ.SetYLength(floor.height)
sourceWallZ.SetZLength(floor.height)
sourceWallZ.Update()

# mapper

##sphere
sphere_mapper = vtk.vtkPolyDataMapper()
sphere_mapper.SetInputData(sourceSphere.GetOutput())

##floor
floor_mapper = vtk.vtkPolyDataMapper()
floor_mapper.SetInputData(sourceFloor.GetOutput())

##wall
wall_mapperX = vtk.vtkPolyDataMapper()
wall_mapperX.SetInputData(sourceWallX.GetOutput())


wall_mapperZ = vtk.vtkPolyDataMapper()
wall_mapperZ.SetInputData(sourceWallZ.GetOutput())

#actor

##sphere
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)
sphere_actor.GetProperty().SetColor(0.0, 1.0, 0.0)

##floor
floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.GetProperty().SetColor(1, 1, 0.0)
floor.actor = floor_actor
 ##walls
wallXPos_actor = vtk.vtkActor()
wallXPos_actor.SetMapper(wall_mapperX)
wallXPos_actor.GetProperty().SetColor(1, 1, 0.0)

wallXNeg_actor = vtk.vtkActor()
wallXNeg_actor.SetMapper(wall_mapperX)
wallXNeg_actor.GetProperty().SetColor(1, 1, 0.0)

wallZPos_actor = vtk.vtkActor()
wallZPos_actor.SetMapper(wall_mapperZ)
wallZPos_actor.GetProperty().SetColor(1, 1, 0.0)

wallZNeg_actor = vtk.vtkActor()
wallZNeg_actor.SetMapper(wall_mapperZ)
wallZNeg_actor.GetProperty().SetColor(1, 1, 0.0)




#axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(axes)
renderer.AddActor(floor_actor)
renderer.AddActor(wallXPos_actor)
renderer.AddActor(wallXNeg_actor)
renderer.AddActor(wallZPos_actor)
renderer.AddActor(wallZNeg_actor)
renderer.AddActor(sphere_actor)


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

set_initial_position()

interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()