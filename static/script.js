const video = document.getElementById('video');
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

function captureImage() {
  const canvas = document.getElementById('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0);

  const dataURL = canvas.toDataURL('image/jpeg');
  fetch('/detect', {
    method: 'POST',
    body: JSON.stringify({ image: dataURL }),
    headers: { 'Content-Type': 'application/json' }
  })
  .then(res => res.blob())
  .then(blob => {
    document.getElementById('result').src = URL.createObjectURL(blob);
  });
}
