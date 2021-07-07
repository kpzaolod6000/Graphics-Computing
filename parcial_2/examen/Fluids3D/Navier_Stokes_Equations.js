var N;
function IX(x, y, z) {
    return x + y * N + z * N * N;
}

class FluidCube {
    constructor(size,diffusion,viscosity,dt){
        this.size = size; // int
        this.dt = dt; //float
        this.diff = diffusion; // float
        this.visc = viscosity; //float
        N = size;
        
        this.s = new Array(N*N*N).fill(0);
        this.density = new Array(N*N*N).fill(0);
        
        this.Vx = new Array(N*N*N).fill(0);
        this.Vy = new Array(N*N*N).fill(0);
        this.Vz = new Array(N*N*N).fill(0);

        this.Vx0 = new Array(N*N*N).fill(0);
        this.Vy0 = new Array(N*N*N).fill(0);
        this.Vz0 = new Array(N*N*N).fill(0);
    }

    addDensity(x,y,z,amount)
    {
        //N = cube.size;
        this.density[IX(x, y, z)] += amount;
    }
    addVelocity(x,y,z,amountX,amountY,amountZ)
    {
        var index = IX(x, y, z);
        this.Vx[index] += amountX;
        this.Vy[index] += amountY;
        this.Vz[index] += amountZ;
    }

    Step()
    {
        var N       = this.size;//int
        var visc    = this.visc;//float
        var diff    = this.diff;//float
        var dt      = this.dt;//float
        var Vx      = this.Vx;//float //array
        var Vy      = this.Vy;//float //array
        var Vz      = this.Vz;//float //array
        var Vx0     = this.Vx0;//float //array
        var Vy0     = this.Vy0;//float //array
        var Vz0     = this.Vz0;//float //array
        var s       = this.s;//float //array
        var density = this.density;//float //array
        
        diffuse(1, Vx0, Vx, visc, dt, 4, N);
        diffuse(2, Vy0, Vy, visc, dt, 4, N);
        diffuse(3, Vz0, Vz, visc, dt, 4, N);
        
        project(Vx0, Vy0, Vz0, Vx, Vy, 4, N);
        
        advect(1, Vx, Vx0, Vx0, Vy0, Vz0, dt, N);
        advect(2, Vy, Vy0, Vx0, Vy0, Vz0, dt, N);
        advect(3, Vz, Vz0, Vx0, Vy0, Vz0, dt, N);
        
        project(Vx, Vy, Vz, Vx0, Vy0, 4, N);
        
        diffuse(0, s, density, diff, dt, 4, N);
        advect(0, density, s, Vx, Vy, Vz, dt, N);
    }
}
function diffuse(b,x,x0,diff,dt,iter,N) //x and x0 are arrays
{
    var a = dt * diff * (N - 2) * (N - 2); // float
    lin_solve(b, x, x0, a, 1 + 6 * a, iter, N);
}

function lin_solve(b,x,x0,a,c,iter,N) //x and x0 are arrays
{
    var cRecip = 1.0 / c;
    for (var k = 0; k < iter; k++) {
        for (var m = 1; m < N - 1; m++) {
            for (var j = 1; j < N - 1; j++) {
                for (var i = 1; i < N - 1; i++) {
                    x[IX(i, j, m)] =(x0[IX(i, j, m)] + a*(    
                                    x[IX(i+1, j  , m  )]
                                    +x[IX(i-1, j  , m  )]
                                    +x[IX(i  , j+1, m  )]
                                    +x[IX(i  , j-1, m  )]
                                    +x[IX(i  , j  , m+1)]
                                    +x[IX(i  , j  , m-1)]
                           )) * cRecip;
                }
            }
        }
        set_bnd(b, x, N);
    }
}


function project(velocX,velocY,velocZ,p,div,iter,N)//velocX , velocY,velocZ,p,div are arrays
{
    for (var k = 1; k < N - 1; k++) {
        for (var j = 1; j < N - 1; j++) {
            for (var i = 1; i < N - 1; i++) {
                div[IX(i, j, k)] = -0.5*(
                         velocX[IX(i+1, j  , k  )]
                        -velocX[IX(i-1, j  , k  )]
                        +velocY[IX(i  , j+1, k  )]
                        -velocY[IX(i  , j-1, k  )]
                        +velocZ[IX(i  , j  , k+1)]
                        -velocZ[IX(i  , j  , k-1)]
                    )/N;
                p[IX(i, j, k)] = 0;
            }
        }
    }
    set_bnd(0, div, N); 
    set_bnd(0, p, N);
    lin_solve(0, p, div, 1, 6, iter, N);
    
    for (var k = 1; k < N - 1; k++) {
        for (var j = 1; j < N - 1; j++) {
            for (var i = 1; i < N - 1; i++) {
                velocX[IX(i, j, k)] -= 0.5 * (  p[IX(i+1, j, k)]
                                                -p[IX(i-1, j, k)]) * N;
                velocY[IX(i, j, k)] -= 0.5 * (  p[IX(i, j+1, k)]
                                                -p[IX(i, j-1, k)]) * N;
                velocZ[IX(i, j, k)] -= 0.5 * (  p[IX(i, j, k+1)]
                                                -p[IX(i, j, k-1)]) * N;
            }
        }
    }
    set_bnd(1, velocX, N);
    set_bnd(2, velocY, N);
    set_bnd(3, velocZ, N);
}


function advect(b,d, d0, velocX,velocY,velocZ, dt, N)//d,d0,velocX,velocY,velocZ are arrays
{
    var i0, i1, j0, j1, k0, k1; // float
    
    var dtx = dt * (N - 2);//float
    var dty = dt * (N - 2);//float
    var dtz = dt * (N - 2);//float
    
    var s0, s1, t0, t1, u0, u1;
    var tmp1, tmp2, tmp3, x, y, z;
    
    var Nfloat = N;//float
    var ifloat, jfloat, kfloat;//float
    var i, j, k; //float
    
    for(k = 1, kfloat = 1; k < N - 1; k++, kfloat++) {
        for(j = 1, jfloat = 1; j < N - 1; j++, jfloat++) { 
            for(i = 1, ifloat = 1; i < N - 1; i++, ifloat++) {
                tmp1 = dtx * velocX[IX(i, j, k)];
                tmp2 = dty * velocY[IX(i, j, k)];
                tmp3 = dtz * velocZ[IX(i, j, k)];
                x    = ifloat - tmp1; 
                y    = jfloat - tmp2;
                z    = kfloat - tmp3;
                
                if(x < 0.5) x = 0.5; 
                if(x > Nfloat + 0.5) x = Nfloat + 0.5; 
                i0 =  Math.floor(x); 
                i1 = i0 + 1.0;
                if(y < 0.5) y = 0.5; 
                if(y > Nfloat + 0.5) y = Nfloat + 0.5; 
                j0 =  Math.floor(y);
                j1 = j0 + 1.0; 
                if(z < 0.5) z = 0.5;
                if(z > Nfloat + 0.5) z = Nfloat + 0.5;
                k0 =  Math.floor(z);
                k1 = k0 + 1.0;
                
                s1 = x - i0; 
                s0 = 1.0 - s1; 
                t1 = y - j0; 
                t0 = 1.0 - t1;
                u1 = z - k0;
                u0 = 1.0 - u1;
                
                var i0i = parseInt(i0);//int
                var i1i = parseInt(i1);//int
                var j0i = parseInt(j0);//int
                var j1i = parseInt(j1);//int
                var k0i = parseInt(k0);//int
                var k1i = parseInt(k1);//int
                
                d[IX(i, j, k)] = 
                
                    s0 * ( t0 * (u0 * d0[IX(i0i, j0i, k0i)]
                                +u1 * d0[IX(i0i, j0i, k1i)])
                        +( t1 * (u0 * d0[IX(i0i, j1i, k0i)]
                                +u1 * d0[IX(i0i, j1i, k1i)])))
                   +s1 * ( t0 * (u0 * d0[IX(i1i, j0i, k0i)]
                                +u1 * d0[IX(i1i, j0i, k1i)])
                        +( t1 * (u0 * d0[IX(i1i, j1i, k0i)]
                                +u1 * d0[IX(i1i, j1i, k1i)])));
            }
        }
    }
    set_bnd(b, d, N);
}

function set_bnd(b,x,N) //x is a array
{
    for(var j = 1; j < N - 1; j++) {
        for(var i = 1; i < N - 1; i++) {
            x[IX(i, j, 0  )] = b == 3 ? -x[IX(i, j, 1  )] : x[IX(i, j, 1  )];
            x[IX(i, j, N-1)] = b == 3 ? -x[IX(i, j, N-2)] : x[IX(i, j, N-2)];
        }
    }
    for(var k = 1; k < N - 1; k++) {
        for(var i = 1; i < N - 1; i++) {
            x[IX(i, 0  , k)] = b == 2 ? -x[IX(i, 1  , k)] : x[IX(i, 1  , k)];
            x[IX(i, N-1, k)] = b == 2 ? -x[IX(i, N-2, k)] : x[IX(i, N-2, k)];
        }
    }
    for(var k = 1; k < N - 1; k++) {
        for(var j = 1; j < N - 1; j++) {
            x[IX(0  , j, k)] = b == 1 ? -x[IX(1  , j, k)] : x[IX(1  , j, k)];
            x[IX(N-1, j, k)] = b == 1 ? -x[IX(N-2, j, k)] : x[IX(N-2, j, k)];
        }
    }
    
    x[IX(0, 0, 0)]       = 0.33 * (x[IX(1, 0, 0)]
                                  + x[IX(0, 1, 0)]
                                  + x[IX(0, 0, 1)]);
    x[IX(0, N-1, 0)]     = 0.33 * (x[IX(1, N-1, 0)]
                                  + x[IX(0, N-2, 0)]
                                  + x[IX(0, N-1, 1)]);
    x[IX(0, 0, N-1)]     = 0.33 * (x[IX(1, 0, N-1)]
                                  + x[IX(0, 1, N-1)]
                                  + x[IX(0, 0, N)]);
    x[IX(0, N-1, N-1)]   = 0.33 * (x[IX(1, N-1, N-1)]
                                  + x[IX(0, N-2, N-1)]
                                  + x[IX(0, N-1, N-2)]);
    x[IX(N-1, 0, 0)]     = 0.33 * (x[IX(N-2, 0, 0)]
                                  + x[IX(N-1, 1, 0)]
                                  + x[IX(N-1, 0, 1)]);
    x[IX(N-1, N-1, 0)]   = 0.33 * (x[IX(N-2, N-1, 0)]
                                  + x[IX(N-1, N-2, 0)]
                                  + x[IX(N-1, N-1, 1)]);
    x[IX(N-1, 0, N-1)]   = 0.33 * (x[IX(N-2, 0, N-1)]
                                  + x[IX(N-1, 1, N-1)]
                                  + x[IX(N-1, 0, N-2)]);
    x[IX(N-1, N-1, N-1)] = 0.33 * (x[IX(N-2, N-1, N-1)]
                                  + x[IX(N-1, N-2, N-1)]
                                  + x[IX(N-1, N-1, N-2)]);
}

export { FluidCube,IX};