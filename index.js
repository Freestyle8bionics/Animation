const Character = document.querySelector('.Character');
let rotation = 0;

function rotateCharacter() {
    rotation += 5;
    Character.style.transform = `rotateY(${rotation}deg)`;
    requestAnimationFrame(rotateCharacter);
}

rotateCharacter();

// const audioElement = document.getElementById("bg-audio");

// // Try to unmute after page load

// window.addEventListener("load", () => {

//     setTimeout(() => {

//         audioElement.muted = false;

//         audioElement.play().catch(err => console.log("Autoplay blocked:", err));

//     }, 500);

// });

// // Allow click anywhere to start playback if blocked

// document.body.addEventListener("click", () => {

//     if (audioElement.paused) {

//         audioElement.play().catch(err => console.log("Play blocked:", err));

//     }

// });