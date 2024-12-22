document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent form from submitting normally

    let formData = new FormData(this);  // Create FormData object with form data
    let resultDiv = document.getElementById('result');  // Result div where output will be shown
    resultDiv.innerHTML = '<p>Processing your file... Please wait.</p>';
    resultDiv.style.display = 'block';  // Show the result section

    // Make an asynchronous request to the backend
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Check if the result is a video or audio
            const videoUrl = data.video_url;
            const fileExtension = videoUrl.split('.').pop().toLowerCase();

            if (fileExtension === 'mp4') {
                // If it's a video, display the video player
                resultDiv.innerHTML = `
                    <h2>Processing Complete!</h2>
                    <p>Your video has been processed successfully. Watch it below:</p>
                    <video width="100%" controls>
                        <source src="${videoUrl}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                `;
            } else if (fileExtension === 'mp3') {
                // If it's an audio file, display the audio player
                resultDiv.innerHTML = `
                    <h2>Processing Complete!</h2>
                    <p>Your audio has been processed successfully. Listen to it below:</p>
                    <audio controls>
                        <source src="${videoUrl}" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                `;
            }
        } else {
            resultDiv.innerHTML = `
                <h2>Error:</h2>
                <p>${data.error}</p>
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `
            <h2>Error:</h2>
            <p>There was an issue while processing your request. Please try again.</p>
        `;
    });
});
