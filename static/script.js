const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

setInterval(() => {
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

async function sendFrame() {
  if (video.readyState === video.HAVE_ENOUGH_DATA) {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);

    const image = canvas.toDataURL('image/jpeg');
    const res = await fetch('/detect', {
      method: 'POST',
      body: JSON.stringify({ image }),
      headers: { 'Content-Type': 'application/json' }
    });

    const blob = await res.blob();
    result.src = URL.createObjectURL(blob);
  }

  requestAnimationFrame(sendFrame);
}

sendFrame();
}, 1000); 
