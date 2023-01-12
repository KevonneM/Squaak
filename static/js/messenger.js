console.log("Js check from messenger.js.");

// Used to focus on 'roomInput' when a user opens the page.
document.querySelector("#roomInput").focus();

// Used to submit if the user presses the enter key.
document.querySelector("#roomInput").onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector("#roomConnect").click();
    }
};

// Used to redirect to chat_room/room_input.
document.querySelector("#roomConnect").onclick = function() {
    let roomName = document.querySelector("#roomInput").value;
    window.location.pathname = "messenger/chat_room/" + roomName + "/";
}

// Used to redirect to roomSelect.
document.querySelector("#roomSelect").onchange = function() {
    let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
    window.location.pathname = "messenger/chat_room/" + roomName + "/"
}