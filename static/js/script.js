const slider = document.querySelector(".top-questions-card")

const slideSections = document.querySelectorAll(".slide-section")

const leftArrow = document.querySelector(".swiper-button-prev")
const rightArrow = document.querySelector(".swiper-button-next")

let slidesArr = Array.from(slideSections)
for(i in slidesArr) {
    if(i > 0) {
        slidesArr[i].style.display = "none"
    }
}

var sectionIndex = 0;

rightArrow.addEventListener("click", function() {
    if (sectionIndex < 0) {
        sectionIndex = 0
    }
    if (sectionIndex == 3) {
        return
    } else {
        slidesArr[sectionIndex].style.display = "none"
        sectionIndex = sectionIndex +1
        slidesArr[sectionIndex].style.display = "flex"
    }

})

leftArrow.addEventListener("click", function() {
    if (sectionIndex == 0) {
        return
    } else {
        slidesArr[sectionIndex].style.display = "none"
        sectionIndex = sectionIndex -1
        slidesArr[sectionIndex].style.display = "flex"
    }
    }
)

