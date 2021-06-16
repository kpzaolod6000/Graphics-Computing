import * as THREE from './jsm/three.module.js';
import { GUI } from './jsm/dat.gui.module.js';
import {OrbitControls} from './jsm/OrbitControls.js';
import {ProductionPlanets} from './planets.js';
import {STLLoader} from './jsm/STLLoader.js';



var guiOrbit = {Ejecutar_Traslacion: true, Ejecutar_Rotacion: true};
/*
* utilizado cuando queremos poner la lampara dentro de la scene como un mesh
*/
function makeXYZGUI(gui, vector3, name, onChangeFn) {
    const folder = gui.addFolder(name);
    folder.add(vector3, 'x', -20, 20).onChange(onChangeFn);
    folder.add(vector3, 'y', 0, 20).onChange(onChangeFn);
    folder.add(vector3, 'z', -20, 20).onChange(onChangeFn);
    folder.open();
}      
/*
* utilizado por GUI para modificar los parametros de light en la scena
*/
class ColorGUIHelper {
    constructor(object, prop) {
        this.object = object;
        this.prop = prop;
    }
    get value() {
        return `#${this.object[this.prop].getHexString()}`;
    }
    set value(hexString) {
        this.object[this.prop].set(hexString);
    }
}

/*
* camera        
*/
var camera = new THREE.PerspectiveCamera(
    102, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.5, // near
    2000 // far
);  
camera.position.z = 50;


/*
* scene        
*/
var scene = new THREE.Scene();
scene.background =  new THREE.TextureLoader().load( 'textures/estrellas.jpg' );

/*
* mesh
*/
/*
* ring 
*/

function createRing(distanceAxi,setSegments,thetaSegments,setColor,setPosicion,setRotation) {
    const geometryRing = new THREE.RingGeometry( distanceAxi,distanceAxi-setSegments, thetaSegments );
    const materialRing = new THREE.MeshBasicMaterial( { color: setColor, side: THREE.DoubleSide ,transparent:true} );
    const ring  = new THREE.Mesh( geometryRing, materialRing );
    
    ring.position.set(setPosicion[0],setPosicion[1],setPosicion[2]);
    ring.rotation.x = setRotation;
    scene.add(ring);
    return ring;

}

/*
* sphere
*/
var geometrySun = new THREE.SphereGeometry(3, 32, 32);        
const textureSun = new THREE.TextureLoader().load( 'textures/8k_sun.jpg' );
//var materialSun = new THREE.MeshPhongMaterial( {map: textureSun ,transparent: true});
const materialSun = new THREE.MeshBasicMaterial({
    map: textureSun,
    transparent: true,
  });

var sun = new THREE.Mesh( geometrySun,materialSun ); 
sun.position.y = 0;
sun.position.x = 0;
sun.position.z = 0;
scene.add( sun );

const planets = [];
const namePlanet = ["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"];

namePlanet.forEach(item => {
    const Planet_ = new ProductionPlanets(item);
    Planet_.getMesh();    
    scene.add(Planet_.mesh);
    
    if(item == "earth"){
        Planet_. getMeshSatelite([0.3,32,32],[15.2,0,0],"textures/moon.jpg")
        Planet_.satelites.forEach(satel => {
            scene.add(satel);
        });
    }
    if(item == "mars"){
        Planet_. getMeshSatelite([0.2,32,32],[23.7,0,0],"textures/FobosMars.jpg")
        Planet_.satelites.forEach(satel => {
            scene.add(satel);
        });
        
    }

    planets.push(Planet_);
});


/*
* axis        
*/
const axesHelper = new THREE.AxesHelper( 15 );
scene.add( axesHelper );

/*
* light 
*/
/*
*HemisphereLight 
*/
const skyColor = 0xB1E1FF;  // light blue
const groundColor = 0x59340B;  // black
const hemisphere_light = new THREE.HemisphereLight(skyColor, groundColor, 0.5);
scene.add(hemisphere_light);        

/*
* PointLight
*/
const color = 0xFFFFFF;
const intensity = 4;
const distance = 90;
const light = new THREE.PointLight(color, intensity,distance);
light.position.set(0, 0, 0);
scene.add(light);

const helper = new THREE.PointLightHelper(light);
scene.add(helper);

function updateLight() {
    helper.update();
}
updateLight();

const positionCamera = {
    X: 0,
    Y: 0,
    Z: 0
}

const gui = new GUI();
gui.addColor(new ColorGUIHelper(light, 'color'), 'value').name('color');
gui.add(light, 'intensity', 0, 6, 0.01);
gui.add(light, 'distance', 0, 200).onChange(updateLight);
gui.add(guiOrbit, 'Ejecutar_Traslacion', 0, 1);
gui.add(guiOrbit, 'Ejecutar_Rotacion', 0, 1);
makeXYZGUI(gui, light.position, 'position', updateLight);
var guicamera  = gui.addFolder("Camera");
guicamera .add( positionCamera, 'X', -600, 600 ).onChange( function( value ){ camera.position.x = value; controls.maxDistance = value+10;controls.minDistance = value;} );
guicamera .add( positionCamera, 'Y', -600, 600 ).onChange( function( value ){ camera.position.y = value; } );
guicamera .add( positionCamera, 'Z', -600, 600 ).onChange( function( value ){ camera.position.z = value; } );
// makeXYZGUI(gui, camera.position, 'camera', 0);
/*
* renderer
*/
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
renderer.render( scene, camera );

/*
* para los controles del mouse
*/
// var controls = new THREE.OrbitControls( camera, renderer.domElement );
var controls = new OrbitControls( camera, renderer.domElement );
controls.minDistance = 0; // minima distancia a q puede hacer zoom
controls.maxDistance = 20;// maxima distancia a q puede hacer zoom

/*
* para que el renderer se actualize al redimensionar el navegador
*/
window.addEventListener('resize', redimensionar);
function redimensionar(){
    // actualizamos las variables que dependen del tamanio del navegador
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.render( scene, camera );
}



/*
* para controlar la animacion
*/


var clock = new THREE.Clock();
var time = 0;
var delta = 0;
function traslationPlanets(dataPlanet,time,daybyOrbit,velocity,distanceAxis){
 
    //earth.rotation.x = time * 4;
    if(guiOrbit.Ejecutar_Traslacion){
        dataPlanet.position.x = Math.cos(time*(1.0/daybyOrbit*velocity)+10) * distanceAxis;
        dataPlanet.position.z =Math.sin(time*(1.0/daybyOrbit*velocity)+10) * distanceAxis;
    }
    
}
function traslationSatelite(dataSatelite,dataPlanet,time,daybyOrbit,velocity,distanceAxis,setRotation){
    if(guiOrbit.Ejecutar_Traslacion){
        traslationPlanets(dataSatelite,time,daybyOrbit,velocity,distanceAxis);
        dataSatelite.position.x = dataSatelite.position.x + dataPlanet.position.x;
        dataSatelite.position.z = dataSatelite.position.z + dataPlanet.position.z;
    }
    if(guiOrbit.Ejecutar_Rotacion){
        dataSatelite.rotation.x += setRotation[0];
        dataSatelite.rotation.y += setRotation[1];
        dataSatelite.rotation.z += setRotation[2];            
    }
}

/*
* saturn ring 
*/
var saturnRing = [];
var ring_;
var updatePosition = 1.5+0.5;//modificar para notar que gira los anillos
for (let index = 0; index < 10; index++) {
   
    if(index > 6 )
        ring_= createRing(updatePosition,0.1,100,0x404718,[5.8,0,0],Math.PI / 2);
    else if(index == 6)
        ring_= createRing(updatePosition,0.1,100,0x060601,[5.8,0,0],Math.PI / 2);
    else
        ring_= createRing(updatePosition,0.1,100,0x797E5C,[5.8,0,0],Math.PI / 2);
    updatePosition += 0.1;
    saturnRing.push(ring_);
    
}
console.log(saturnRing);

var animate = function(){
    requestAnimationFrame(animate);   
    //earth         
    delta = clock.getDelta();
    time += delta;
    // earth.position.x = Math.cos(time*(1.0/366*200)+10) * 14.9;
    // earth.position.z = Math.sin(time*(1.0/366*200)+10)*14.9;
    planets.forEach(item => {
        traslationPlanets(item.mesh,time,item.daysOrbit,item.velocityTraslation,item.position[0]);
        if(guiOrbit.Ejecutar_Rotacion){
            item.mesh.rotation.y += item.velocityRotate;
        }
    });

    // traslationPlanets(earth,time,366,29.78 ,14.9);
    // traslationSatelite(item.satelites[0],item.mesh,time,30,15,1.6,[0,0.01,0]);
    traslationSatelite(planets[2].satelites[0],planets[2].mesh,time,30,15,1.6,[0,0.01,0]);
    traslationSatelite(planets[3].satelites[0],planets[3].mesh,time,50,20,1.6,[0,0.01,0]);
    // planets.forEach(item => {
    //     if(item == "earth"){
            
    //     }
    // });

  
    saturnRing.forEach(ring => traslationSatelite(ring,planets[5].mesh,time,10752,9.69,0.1,[0,0,0.3]));
    sun.rotation.y += 0.0004;

    renderer.render( scene, camera );
}
animate();
var rotation_= Math.PI / 2;
var position_ = [0,0,0];
planets.forEach(item => {
    createRing(item.position[0],0.02,100,0xffffff,position_,rotation_);
});
