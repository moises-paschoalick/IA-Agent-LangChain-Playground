let fullText = "";
let renderedLength = 0;
let isAnimating = false;
let streamFinished = false;

function startStream() {
    const chat = document.getElementById("chat");
    chat.innerText = ""; // limpa antes de começar

    fullText = "";
    renderedLength = 0;
    isAnimating = false;
    streamFinished = false;

    const cursor = document.createElement("span");
    cursor.classList.add("cursor");
    chat.appendChild(cursor);

    const eventSource = new EventSource("http://localhost:8000/agent/stream");

    eventSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
          fullText += data.content;

        if (!isAnimating) {
            isAnimating = true;
            requestAnimationFrame(() => animate(chat, cursor));
        }
    };

    eventSource.addEventListener("end", function() {
        console.log("Stream finished");
        eventSource.close();
    });

    eventSource.onerror = function(err) {
        console.error("Stream error:", err);
        eventSource.close();
    };
}

function animate(chat, cursor) {
    if (renderedLength < fullText.length) {
        const nextChunk = fullText.slice(renderedLength, renderedLength + 3);
        cursor.insertAdjacentText("beforebegin", nextChunk);
        renderedLength += nextChunk.length;

        requestAnimationFrame(() => animate(chat, cursor));
    } else {
        if (!streamFinished) {
            requestAnimationFrame(() => animate(chat, cursor));
        } else {
            isAnimating = false;
        }
    }
}