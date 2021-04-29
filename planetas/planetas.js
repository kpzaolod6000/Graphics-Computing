var scene = new THREE.Scene();
scene.background =  new THREE.TextureLoader().load( 'textures/estrellas.jpg' );

var camera = new THREE.PerspectiveCamera(
    75, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.1, // near
    2000 // far
);        
camera.position.z = 10;

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry(2,2,2,3,3,3);        
var material = new THREE.MeshBasicMaterial( {color:0x00ff00, wireframe: true} );
var cube = new THREE.Mesh( geometry, material ); 

var sphere = new THREE.Mesh( new THREE.SphereGeometry(1, 32, 32), material ); 
sphere.position.y = 3;
sphere.position.x = -5;

var plane = new THREE.Mesh( new THREE.PlaneGeometry(2, 2, 5, 4), material ); 
        plane.position.y = 3;
        plane.position.x = 5;

scene.add(sphere);
scene.add(plane);

renderer.render( scene, camera );
var controls = new THREE.OrbitControls( camera, renderer.domElement );
controls.minDistance = 3;
controls.maxDistance = 10;

window.addEventListener('resize', redimensionar);
function redimensionar(){
    // actualizamos las vcariables que dependen del tamanio delñ navegador
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.render( scene, camera );
}

var animate = function(){
    requestAnimationFrame(animate);            

    // para recorrer cada objeto de la scena (tambien incluye la camara)
    scene.traverse(function(object){
        if (object.isMesh == true){ // para evitar rotar la camara
            object.rotation.x += 0.01;
            //object.rotation.y += 0.01;
        }
    });

    //circle.rotation 
    renderer.render( scene, camera );
}
animate();