// Get references to the HTML elements
const codeInput = document.getElementById('codeInput');
const explainButton = document.getElementById('explainButton');
const explanationResult = document.getElementById('explanationResult');
const explanationText = document.getElementById('explanationText');
const loadingIndicator = document.getElementById('loadingIndicator');

// Add an event listener to the button
explainButton.addEventListener('click', handleExplainClick);

async function handleExplainClick() {
    const code = codeInput.value.trim(); // Get code and remove extra whitespace

    if (!code) {
        explanationText.textContent = 'Please paste some code first.';
        explanationResult.style.display = 'block'; // Make sure result box is visible
        loadingIndicator.style.display = 'none';
        return; // Stop if there's no code
    }

    // --- Prepare for API call ---
    explanationText.textContent = ''; // Clear previous explanation
    loadingIndicator.style.display = 'block'; // Show loading indicator
    explanationResult.style.display = 'block'; // Ensure result box is visible
    explainButton.disabled = true; // Disable button during request

    try {
        // --- Send code to backend ---
        // The '/explain' matches the route defined in our Flask app (app.py)
        const response = await fetch('/explain', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Tell the server we're sending JSON
            },
            body: JSON.stringify({ code: code }) // Send the code in JSON format
        });

        // --- Handle backend response ---
        if (!response.ok) {
            // If the server response wasn't successful (e.g., 400, 500 error)
            const errorData = await response.json().catch(() => ({ error: 'Server returned an error, but response was not valid JSON.' }));
            throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
        }

        // If the response is OK (status 200-299)
        const data = await response.json(); // Parse the JSON response from the backend

        // --- Display the explanation ---
        // Use textContent to prevent potential HTML injection issues from the explanation
        explanationText.textContent = data.explanation;

    } catch (error) {
        // --- Handle errors (network issues, server errors) ---
        console.error('Error fetching explanation:', error);
        explanationText.textContent = `Error: ${error.message}`; // Display error to user
    } finally {
        // --- Clean up regardless of success or error ---
        loadingIndicator.style.display = 'none'; // Hide loading indicator
        explainButton.disabled = false; // Re-enable button
    }
}
