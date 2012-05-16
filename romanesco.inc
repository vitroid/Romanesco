#declare S=1.2;
light_source {<2000,-1000,2000> color rgb<S/2,S/2,S/2> }
light_source {<2000,-1000,-2000> color rgb<S/3,S/3,S/3> }
//light_source {<-2000,-1000,2000> color rgb<S,S,S> }
//light_source {<2000,-1000,-2000> color rgb<S,S,S> }
light_source {<-2000,-1000,-2000> color rgb<S,S,S> }
//light_source {<600,-1000,800> color rgb<1,1,1>}
global_settings { max_trace_level 100 } 

camera {
    //location <250,-6500,-6500>
    //angle 3
    location <250,-1000000,250>
    angle 0.022
    up    <0,0,-1>
    right <-1,0,0>
    look_at  <250, 350,  0>
}

background { White}

//#declare tRom=texture{pigment {color rgb<0.7 1 0.1>}finish{ diffuse 1 ambient 0.1 specular 0.5}}
#declare tRom=texture{pigment {color rgb<0.65 1 0.4>}finish{ diffuse 0.8 ambient 0 specular 0.2}}
//phong 0.8 phong_size 3
