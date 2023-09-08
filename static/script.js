document.getElementById("colorChangeButton").addEventListener("click", function () {
    if (this.style.backgroundColor === "rgb(0, 128, 0)") {
        this.style.backgroundColor = "#ff0000";
        this.textContent = "문닫힘";
    } else {
        this.style.backgroundColor = "#008000";
        this.textContent = "문열림";
    }

    setTimeout(function () {
        document.getElementById("colorChangeButton").style.backgroundColor = "#ff0000";
        document.getElementById("colorChangeButton").textContent = "문닫힘";
    }, 3000);
});