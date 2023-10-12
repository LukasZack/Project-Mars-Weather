import * as THREE from 'three';

// Creating a scene, camera and renderer
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

// Append towards HTML
document.getElementById('scene-container').appendChild(renderer.domElement);

// Creating a sphere geometry, material and mesh
const sphereGeometry = new THREE.SphereGeometry(1, 32, 32);

const sphereMaterial = new THREE.MeshBasicMaterial({ color: 0xFF5733 });

const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

// Adding the sphere to the scene, ambient light and directional light
scene.add(sphere);

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(1, 1, 1);
scene.add(directionalLight);

// Animation loop
const animate = () => {
  requestAnimationFrame(animate);

  // Rotate the sphere
  sphere.rotation.x += 0.01;
  sphere.rotation.y += 0.01;

  renderer.render(scene, camera);
};

animate();
