
function newChat() {
    document.getElementById("question").value = "";
    document.getElementById("response").innerText =
        "New chat started! Ask your question.";
}

function showTool(tool) {
    document.getElementById("response").innerText =
        tool + " selected! This feature will be developed in the next version.";

    document.getElementById("response").scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}

async function sendMessage() {
    const question = document.getElementById("question").value.trim();
    const branch = document.getElementById("branch").value;
    const year = document.getElementById("year").value;
    const response = document.getElementById("response");

    if (!question) {
        response.innerText = "Please enter a question first.";
        return;
    }

    if (!branch || !year) {
        response.innerText =
            "Please select your B.Tech branch and year first.";
        return;
    }

    response.innerText = "BTech GPT is thinking...";

    try {
        const result = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: `Branch: ${branch}, Year: ${year}. Question: ${question}`
            })
        });

        const data = await result.json();

        if (!result.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        response.innerText = data.answer;
        document.getElementById("question").value = "";

    } catch (error) {
        response.innerText = "Error: " + error.message;
    }

    response.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}

document.getElementById("question").addEventListener(
    "keydown",
    function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    }
);

