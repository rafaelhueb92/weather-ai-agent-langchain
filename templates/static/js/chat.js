const chatScroll = document.getElementById("chatScroll");
const chatBox = document.getElementById("chatBox");
const chatForm = document.getElementById("chatForm");
const processingIndicator = document.getElementById("processingIndicator");

if (chatScroll) {
    chatScroll.scrollTop = chatScroll.scrollHeight;
}

if (chatForm && processingIndicator && chatScroll && chatBox) {
    chatForm.addEventListener("submit", function () {
        const textArea = chatForm.querySelector("textarea[name='message']");
        const submitButton = chatForm.querySelector("button[type='submit']");

        if (textArea && !textArea.value.trim()) {
            return;
        }

        processingIndicator.classList.add("visible");
        processingIndicator.setAttribute("aria-hidden", "false");

        if (submitButton) {
            submitButton.disabled = true;
        }

        if (textArea) {
            textArea.setAttribute("readonly", "true");
        }

        chatScroll.scrollTop = chatScroll.scrollHeight;
    });
}
