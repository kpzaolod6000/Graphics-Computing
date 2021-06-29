let fluid;

function setup() {
  createCanvas(300, 300);
  frameRate(22);
  fluid = new FluidCube(0.2, 0, 0.0000001);
}

function draw() {
    stroke(51);
    strokeWeight(2);

    let cx = int((0.5 * width) / SCALE);
    let cy = int((0.5 * height) / SCALE);
    //console.log(cx);
    //console.log(cy);
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            fluid.addDensity(cx + i, cy + j, random(50, 150));
        }
    }

    for (let i = 0; i < 2; i++) {
        let angle = noise(t) * TWO_PI * 2;
        let v = p5.Vector.fromAngle(angle);
        //console.log(angle);
        //console.log(v);
        v.mult(0.2);
        //console.log(v);
        t += 0.01;
        fluid.addVelocity(cx, cy, v.x, v.y);
    }

    fluid.step();
    fluid.renderD();
}