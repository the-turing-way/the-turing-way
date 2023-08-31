document.addEventListener("DOMContentLoaded", function () {
    let pathwayValue = sessionStorage.getItem("pathwayValue") || null;

    document.addEventListener('click', function (event) {
        const card = event.target.closest('.card-text .sphinx-bs');
        if (card) {
            pathwayValue = card.textContent.trim();
            sessionStorage.setItem("pathwayValue", pathwayValue);
        }

        const link = event.target.closest('.bd-links');
        if (link) {
            pathwayValue = null;
            sessionStorage.setItem("pathwayValue", null);
        }
    });

    const images = document.querySelectorAll('img[src^="https://img.shields.io/static/v1?label=pathway"]');
    let colour = "blue";
    if (pathwayValue === "Data Study Group") {
        colour = "white";
    } else if (pathwayValue === "Phd Students") {
        colour = "blue";
    } else if (pathwayValue === "Group Leaders") {
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