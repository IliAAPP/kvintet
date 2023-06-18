'use client'
import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";
import Dropdown from '@/components/Dropdown';
import Image from 'next/image'
import Form from '@/components/Form';
import Link from "next/link";
function CityModel(props) {
  const { scene } = useGLTF("/probki.glb");
  return <primitive object={scene} {...props} />;
}

export default function Home() {
  return (
    <div style={{
        padding:0,margin:0,height:'100vh'
    }}>
      <Dropdown/><Image src="/plus.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:550}}/>
      <Form />
      <Link href={'/mapprobki'}>
      <Image src="/car.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:957}}/>
      </Link>
      <Link href={'/home'}>
      <Image src="/exit.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:752}}/>
      </Link>
      <Image src="/cranes.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:852}}/>
      <Image src="/fire.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1482}}/>
      <Image src="/light.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1062}}/>
      <Image src="/parking.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1167}}/>
      <Image src="/water.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1272}}/>
      <Link href={'/mapwater'}>
      <Image src="/waterbottom.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1587}}/>
      </Link>
      <Link href={'/mapelectr'}>
      <Image src="/zip.png" alt="3D модель здания" width={75} height={75} style={{position:'absolute',zIndex:11,top:30,left:1377}}/>
      </Link>






      <Canvas  style={{ width: "100vw", height: "100vh" ,padding:0,}}
        camera={{ position: [0, 10, 0], rotation: [-Math.PI / 2, 0, 0] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <CityModel position={[0, 0, 0]} scale={[0.1, 0.1, 0.1]} />
        <OrbitControls />
      </Canvas>
    </div>
  );
}
