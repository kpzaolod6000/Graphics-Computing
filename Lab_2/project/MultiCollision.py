import vtk
import math

class MySphere:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius    
        self.velocity = [-30,0,-30] # la esfera avanza hacia el eje X Y z
        self.last_velocity = [-30,0,-30]
        self.actor = None

class MyFloor:
    def __init__(self, pos, height,width,depth):
        self.pos = pos
        self.height = height    
        self.actor = None
        self.width = width
        self.depth = depth
        self.height = height

sphere = MySphere([-10,2.5,10], 2)
floor = MyFloor([0,0,0],1,40,40)
time = 0.05
aceleration = 2 #m/(s**2)
#height = abs(floor.pos[1] - sphere.pos[1]) # = (1/2)*g*time^2

def set_initial_position():
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    floor_actor.SetPosition(floor.pos[0], floor.pos[1], floor.pos[2])
    wallXPos_actor.SetPosition((floor.width/2)-0.5,1,0)
    wallXNeg_actor.SetPosition((-floor.width/2)+0.5,1,0)
    wallZPos_actor.SetPosition(0,1,(floor.depth/2)-0.5)
    wallZNeg_actor.SetPosition(0,1,(-floor.depth/2)+0.5)


def callback_func(caller, timer_event):
    global aceleration,time
    print('pos: ', sphere.pos)
    print('time',time)
    print('aceleration: ', aceleration)
    print('velocity: ', sphere.velocity)
    sphere.pos[0] = sphere.pos[0] + sphere.velocity[0]*time #MRU
    sphere.pos[2] = sphere.pos[2] + sphere.velocity[2]*time #MRU
    
    if (sphere.pos[0] + sphere.radius > (floor.width/2) - 1) or ((sphere.pos[0]) - sphere.radius < (-1*(floor.width/2)) + 1):

        sphere.velocity[0] = (-1*sphere.velocity[0])#MRUV
        #aceleration-=1
    elif(sphere.pos[2] + sphere.radius > (floor.depth/2) - 1) or ((sphere.pos[2]) - sphere.radius < (-1*(floor.depth/2)) + 1):
        sphere.velocity[2] = (-1*sphere.velocity[2]) #MRUV
        #aceleration-=1
    else:
    
        sphere.velocity[0] = sphere.velocity[0] + aceleration*time #MRUV
        sphere.velocity[2] = sphere.velocity[2] + aceleration*time #MRUV      

    sphere.actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    #time+=0.00000001
    if time <= 0.0:
        time = 0
        aceleration = 0
    else:
        time -= 0.0001
        aceleration -= 0.01
    render_window.Render()
    
#image for texture
reader = vtk.vtkJPEGReader()
reader.SetFileName("ball13.jpg")

reader_cube = vtk.vtkJPEGReader()
reader_cube.SetFileName("pasto.jpg")


# Create texture object
texture = vtk.vtkTexture()
texture_cube = vtk.vtkTexture()
if vtk.VTK_MAJOR_VERSION <= 5:
    texture.SetInput(reader.GetOutput())
    texture_cube.SetInput(reader_cube.GetOutput())
else:
    texture.SetInputConnection(reader.GetOutputPort())
    texture_cube.SetInputConnection(reader_cube.GetOutputPort())

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

# Map texture coordinates
map_to_sphere = vtk.vtkTextureMapToSphere()
map_to_cube = vtk.vtkTextureMapToPlane()
if vtk.VTK_MAJOR_VERSION <= 5:
    map_to_sphere.SetInput(sourceSphere.GetOutput())
    map_to_cube.SetInput(sourceFloor.GetOutput())
else:
    map_to_sphere.SetInputConnection(sourceSphere.GetOutputPort())
    map_to_cube.SetInputConnection(sourceFloor.GetOutputPort())


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
if vtk.VTK_MAJOR_VERSION <= 5:
    sphere_mapper.SetInput(map_to_sphere.GetOutput())

else:
    sphere_mapper.SetInputConnection(map_to_sphere.GetOutputPort())

#sphere_mapper = vtk.vtkPolyDataMapper()
#sphere_mapper.SetInputData(map_to_sphere.GetOutput())


##floor

floor_mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    floor_mapper.SetInputData(map_to_cube.GetOutput())
    
else:
    floor_mapper.SetInputConnection(map_to_cube.GetOutputPort())

##wall
wall_mapperX = vtk.vtkPolyDataMapper()
wall_mapperX.SetInputData(sourceWallX.GetOutput())


wall_mapperZ = vtk.vtkPolyDataMapper()
wall_mapperZ.SetInputData(sourceWallZ.GetOutput())

#actor

##sphere
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(sphere_mapper)
#sphere_actor.GetProperty().SetColor(0.0, 1.0, 0.0)
sphere_actor.SetTexture(texture)
sphere.actor = sphere_actor

##floor
floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.SetTexture(texture_cube)
#floor_actor.GetProperty().SetColor(1, 1, 0.0)
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
# transform = vtk.vtkTransform()
# transform.Translate(0.0, 0.0, 0.0) 
# axes = vtk.vtkAxesActor()
# axes.SetUserTransform(transform)


#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,0,0)
#camera.SetPosition(0,sphere.pos[1],sphere.pos[1]*2.7)
camera.SetPosition(0,150,50)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
#renderer.AddActor(axes)
renderer.AddActor(floor_actor)
renderer.AddActor(wallXPos_actor)
renderer.AddActor(wallXNeg_actor)
renderer.AddActor(wallZPos_actor)
renderer.AddActor(wallZNeg_actor)
renderer.AddActor(sphere_actor)
renderer.SetActiveCamera(camera)


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