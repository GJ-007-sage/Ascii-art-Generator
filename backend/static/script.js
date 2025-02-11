function uploadImage() {
    let input = document.getElementById("imageInput");
    if (input.files.length === 0) {
        alert("Please select an image!");
        return;
    }

    let formData = new FormData();
    formData.append("image", input.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            document.getElementById("asciiOutput").textContent = data.ascii;
        }
    })
    .catch(error => console.error("Error:", error));
}
