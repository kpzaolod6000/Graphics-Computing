import * as THREE from './jsm/three.module.js';
import {STLLoader} from './jsm/STLLoader.js';
class Planets{
    getMesh(setGeometry,setPostion,setTexture){
        var geometry = new THREE.SphereGeometry(setGeometry[0], setGeometry[1],setGeometry[2]);
        const texture = new THREE.TextureLoader().load( setTexture );
        var material = new THREE.MeshPhongMaterial( {map: texture } );
        var mesh = new THREE.Mesh( geometry,material ); 
        mesh.position.x = setPostion[0];
        mesh.position.y = setPostion[1];
        mesh.position.z = setPostion[2];
        return mesh;
    }
    getModel(setGeometry,setPosition,setModel,setTexture) {
            
        var loader2 = new STLLoader();
        loader2.load( setModel,function ( geometry) {
            var material = new THREE.MeshLambertMaterial( { map: setTexture } );
            var mesh = new THREE.Mesh( geometry, material );
            
            mesh.scale.set( setGeometry[0], setGeometry[1], setGeometry[2] );
            mesh.position.set( setPosition[0], setPosition[1],setPosition[2]);
            mesh.rotation.x = -Math.PI/2;

        });
        return meshSatelite;
        //console.log(MeshSatelite);
  
    }
}


class Mercury extends Planets{
    
    constructor(){
        super();
        this.geometry= [0.5, 32, 32];
        this.position= [5.8,0,0,];
        this.texture = 'textures/mercury.png';
        this.daysOrbit = 88;
        this.velocityTraslation = 47.87;
        this.velocityRotate = 0.003;
        this.mesh = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);

    }
}
class Venus extends Planets{
    
    constructor(){ 
        super();
        this.geometry= [0.7, 32, 32];
        this.position= [10.8,0,0,]
        this.texture = 'textures/venus.jpg';
        this.daysOrbit = 225;
        this.velocityTraslation = 53.02;
        this.velocityRotate = 0.000041;
        this.mesh = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
}

class Earth extends Planets{

    constructor(){
        super();
        this.geometry= [1, 32, 32];
        this.position= [14.9,0,0,]
        this.texture = 'textures/earth.jpg';
        this.daysOrbit = 366;
        this.velocityTraslation = 29.78;
        this.velocityRotate = 0.01;
        this.mesh = null;
        this.satelites = [];
    }
   
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
    getMeshSatelite(setGeometry,setPostion,setTexture){
        var geometry = new THREE.SphereGeometry(setGeometry[0], setGeometry[1], setGeometry[2]);        
        const texture = new THREE.TextureLoader().load( setTexture );
        var material= new THREE.MeshPhongMaterial( {map: texture } );
        var satel = new THREE.Mesh( geometry,material ); 
        satel.position.x = setPostion[0];
        satel.position.y = setPostion[1];
        satel.position.z = setPostion[2];
        this.satelites.push(satel);
    }
}

class Mars extends Planets{

    constructor(){
        super();
        this.geometry= [0.8, 32, 32];
        this.position= [22.8,0,0,]
        this.texture = 'textures/marte.jpg';
        this.daysOrbit = 687;
        this.velocityTraslation = 24.07;
        this.velocityRotate = 0.00997;
        this.mesh = null;
        this.satelites = [];
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);

    }
    getMeshSatelite(setGeometry,setPostion,setTexture){
        var geometry = new THREE.SphereGeometry(setGeometry[0], setGeometry[1], setGeometry[2]);        
        const texture = new THREE.TextureLoader().load( setTexture );
        var material= new THREE.MeshPhongMaterial( {map: texture } );
        var satel = new THREE.Mesh( geometry,material ); 
        satel.position.x = setPostion[0];
        satel.position.y = setPostion[1];
        satel.position.z = setPostion[2];
        this.satelites.push(satel);
    }
    getModel(setGeometry,setPosition,setModel,setTexture){
        this.satelites.push(super.getModel(setGeometry,setPosition,setModel,setTexture));
    }
    
}


class Jupiter extends Planets{
    constructor(){
        super();
        this.geometry= [2, 32, 32];
        this.position= [77.8,0,0,]
        this.texture = 'textures/jupiter.jpg';
        this.daysOrbit = 4339;
        this.velocityTraslation = 13.07;
        this.velocityRotate = 0.0244;
        this.mesh = null;
      
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
}


class Saturn extends Planets{
    constructor(){
        super();
        this.geometry= [1.5, 32, 32];
        this.position= [142.6,0,0,]
        this.texture = 'textures/saturn.jpg';
        this.daysOrbit = 10752;
        this.velocityTraslation = 9.69;
        this.velocityRotate = 0.0223;
        this.mesh = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);

    }
}

class Uranus extends Planets{
    constructor(){
        super();
        this.geometry= [1.4, 32, 32];
        this.position= [287,0,0,]
        this.texture = 'textures/uranus.jpg';
        this.daysOrbit = 30667;
        this.velocityTraslation = 6.81;
        this.velocityRotate = 0.0139;
        this.mesh = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
}

class Neptune extends Planets{
    constructor(){
        super();
        this.geometry= [1, 32, 32];
        this.position= [449.8,0,0,]
        this.texture = 'textures/neptune.jpg';
        this.daysOrbit = 60140;
        this.velocityTraslation = 5.43;
        this.velocityRotate = 0.0149;
        this.mesh = null;
        this.meshSatelite = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
    
}
class Pluto extends Planets{
    constructor(){
        super();
        this.geometry= [0.5, 32, 32];
        this.position= [590,0,0,]
        this.texture = 'textures/pluto.jpg';
        this.daysOrbit = 90404;
        this.velocityTraslation = 4.66;
        this.velocityRotate = 0.001563;
        this.mesh = null;
    }
    getMesh(){
        this.mesh = super.getMesh(this.geometry,this.position,this.texture);
    }
}


export class ProductionPlanets{

    constructor(name){
        switch (name) {
            case "mercury":
                return new Mercury(name);
            case "venus":
                return new Venus(name);
            case "earth":
                return new Earth(name);
            case "mars":
                return new Mars(name);
            case "jupiter":
                return new Jupiter(name);
            case "jupiter":
                return new Jupiter(name);
            case "saturn":
                return new Saturn(name);
            case "uranus":
                return new Uranus(name);
            case "neptune":
                return new Neptune(name);
            case "pluto":
                return new Pluto(name);            
            default:
                return null;
        }

    }
}
