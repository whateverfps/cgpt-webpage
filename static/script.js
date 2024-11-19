document.getElementById("sendButton").addEventListener("click", async function () {
    const userMessage = document.getElementById("userInput").value;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById("chatbox").innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;
            document.getElementById("chatbox").innerHTML += `<div><strong>GPT:</strong> ${data.response}</div>`;
        } else {
            document.getElementById("chatbox").innerHTML += `<div><strong>Error:</strong> ${data.error}</div>`;
        }

        document.getElementById("userInput").value = ""; // Clear input
    } catch (error) {
        document.getElementById("chatbox").innerHTML += `<div><strong>Error:</strong> ${error.message}</div>`;
    }
});
