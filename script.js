const socket = io.connect("http://localhost:5000");

// Real-time webcam ASCII
socket.on("ascii_frame", function(data) {
    document.getElementById("ascii-video-output").textContent = data.ascii;
});

// Image Upload ASCII Conversion
function uploadImage() {
    const fileInput = document.getElementById("imageUpload");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("ascii-image-output").textContent = data.ascii;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
