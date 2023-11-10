document.addEventListener("DOMContentLoaded", function () {
    let pathwayValue = sessionStorage.getItem("pathwayValue") || null;
    var cards = document.querySelectorAll(".card");
    var sideBar = document.querySelectorAll(".bd-links");
    cards.forEach(function (card) {
        card.addEventListener("click", function () {
            var header = card.querySelector(".card-header span").textContent;

            pathwayValue = header;
            sessionStorage.setItem("pathwayValue", pathwayValue);

            console.log("pathwayValue set to:", pathwayValue);
        })});
    sideBar.forEach(function(link){
        link.addEventListener("click",function(){
            sessionStorage.setItem("pathwayValue" , null);
        })
    });
    
    const images = document.querySelectorAll('img[src^="https://img.shields.io/static/v1?label=pathway"]');
    let colour = "orange";
    if (pathwayValue === "Early Career Researchers") {
        colour = "white";
    } else if (pathwayValue === "Project Leaders") {
        colour = "blue";
    } else if (pathwayValue === "Research Software Engineers") {
        colour = "purple";
    } else {
        colour = "green";
    }


    if (pathwayValue !== "null") {
        for (let i = 0; i < images.length; i++) {
            if (i === 0) {
                images[i].setAttribute('src', `https://img.shields.io/static/v1?label=pathway&message=${pathwayValue}&color=${colour}`);
            } else {
                images[i].remove();
            }
        }
    }
});
