const pixel = document.getElementById("pixel");
const byte = document.getElementById("byte");

async function getDialogue() {
  const res = await fetch('http://localhost:8000/dialogue'); // Or your hosted backend
  const data = await res.json();

  // Just log for now
  console.log("Pixel:", data.pixel);
  console.log("Byte:", data.byte);
}

setInterval(getDialogue, 6000); // Call every few seconds
