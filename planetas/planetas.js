import * as THREE from './jsm/three.module.js';
import { GUI } from './jsm/dat.gui.module.js';
import {OrbitControls} from './jsm/OrbitControls.js';

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
    75, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.5, // near
    2000 // far
);  
camera.position.z = 20;


/*
* scene        
*/
var scene = new THREE.Scene();
scene.background =  new THREE.TextureLoader().load( 'textures/estrellas.jpg' );

/*
* mesh
*/
/*
* sphere
*/
var geometrySun = new THREE.SphereGeometry(3, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureSun = new THREE.TextureLoader().load( 'textures/8k_sun.jpg' );
var materialSun = new THREE.MeshPhongMaterial( {map: textureSun } );
var sun = new THREE.Mesh( geometrySun,materialSun ); 
sun.position.y = 0;
sun.position.x = 0;
sun.position.z = 0;
scene.add( sun );

var geometryMercury = new THREE.SphereGeometry(0.5, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureMercury = new THREE.TextureLoader().load( 'textures/mercury.jpg' );
var materialMercury = new THREE.MeshPhongMaterial( {map: textureMercury } );
var mercury = new THREE.Mesh( geometryMercury,materialMercury ); 
mercury.position.y = 0;
mercury.position.x = 5;
mercury.position.z = 0;
scene.add( mercury );

var geometryVenus = new THREE.SphereGeometry(0.7, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureVenus = new THREE.TextureLoader().load( 'textures/venus.jpg' );
var materialVenus = new THREE.MeshPhongMaterial( {map: textureVenus } );
var venus = new THREE.Mesh( geometryVenus,materialVenus ); 
venus.position.y = 0;
venus.position.x = 5;
venus.position.z = 0;
scene.add( venus );

var geometryEarth = new THREE.SphereGeometry(1, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureEarth = new THREE.TextureLoader().load( 'textures/earth.jpg' );
var materialEarth = new THREE.MeshPhongMaterial( {map: textureEarth } );
var earth = new THREE.Mesh( geometryEarth,materialEarth ); 
earth.position.y = 0;
earth.position.x = 10;
earth.position.z = 0;
scene.add( earth );

var geometryMars = new THREE.SphereGeometry(0.8, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureMars = new THREE.TextureLoader().load( 'textures/marte.jpg' );
var materialMars = new THREE.MeshPhongMaterial( {map: textureMars } );
var mars = new THREE.Mesh( geometryMars,materialMars ); 
mars.position.y = 0;
mars.position.x = 15;
mars.position.z = 0;
scene.add( mars );

var geometryJupiter = new THREE.SphereGeometry(2, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureJupiter = new THREE.TextureLoader().load( 'textures/jupiter.jpg' );
var materialJupiter = new THREE.MeshPhongMaterial( {map: textureJupiter } );
var jupiter = new THREE.Mesh( geometryJupiter,materialJupiter ); 
jupiter.position.y = 0;
jupiter.position.x = 20;
jupiter.position.z = 0;
scene.add( jupiter );

var geometrySaturn = new THREE.SphereGeometry(1.5, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureSaturn = new THREE.TextureLoader().load( 'textures/saturn.jpg' );
var materialSaturn = new THREE.MeshPhongMaterial( {map: textureSaturn } );
var saturn = new THREE.Mesh( geometrySaturn,materialSaturn ); 
saturn.position.y = 0;
saturn.position.x = 25;
saturn.position.z = 0;
scene.add( saturn );

var geometryUranus = new THREE.SphereGeometry(1.4, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureUranus = new THREE.TextureLoader().load( 'textures/uranus.jpg' );
var materialUranus = new THREE.MeshPhongMaterial( {map: textureUranus } );
var uranus = new THREE.Mesh( geometryUranus,materialUranus ); 
uranus.position.y = 0;
uranus.position.x = 30;
uranus.position.z = 0;
scene.add( uranus );

var geometryNeptune = new THREE.SphereGeometry(1, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const textureNeptune = new THREE.TextureLoader().load( 'textures/neptune.jpg' );
var materialNeptune = new THREE.MeshPhongMaterial( {map: textureNeptune } );
var neptune = new THREE.Mesh( geometryNeptune,materialNeptune ); 
neptune.position.y = 0;
neptune.position.x = 35;
neptune.position.z = 0;
scene.add( neptune );

var geometryPluto = new THREE.SphereGeometry(0.5, 32, 32);        
//var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
const texturePluto = new THREE.TextureLoader().load( 'textures/pluto.jpg' );
var materialPluto= new THREE.MeshPhongMaterial( {map: texturePluto } );
var pluto = new THREE.Mesh( geometryPluto,materialPluto ); 
pluto.position.y = 0;
pluto.position.x = 40;
pluto.position.z = 0;
scene.add( pluto );
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
* DirectionalLight
*/
const color = 0xFFFFFF;
const intensity = 0.5;
const light = new THREE.DirectionalLight(color, intensity);
light.position.set(5, 10, 10);
light.target.position.set(0, 0, 0);
scene.add(light);
scene.add(light.target);

const helper = new THREE.DirectionalLightHelper(light);
scene.add(helper);

function updateLight() {
    light.target.updateMatrixWorld();
    helper.update();
}
updateLight();        
// gui
const gui = new GUI();
gui.addColor(new ColorGUIHelper(light, 'color'), 'value').name('color');
gui.add(light, 'intensity', 0, 2, 0.01);
makeXYZGUI(gui, light.position, 'position', updateLight);
makeXYZGUI(gui, light.target.position, 'target', updateLight); 

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
controls.minDistance = 3; // minima distancia a q puede hacer zoom
controls.maxDistance = 10;// maxima distancia a q puede hacer zoom

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

var animate = function(){
    requestAnimationFrame(animate);            

    // para recorrer cada objeto de la scena (tambien incluye la camara)
    scene.traverse(function(object){
        if (object.isMesh == true){ // para evitar rotar la camara
            object.rotation.y += 0.01;
            //object.rotation.y += 0.01;
        }
    });

    //circle.rotation 
    renderer.render( scene, camera );
}
animate();