const slider = document.querySelector(".top-questions-card")

const slideSections = document.querySelectorAll(".slide-section")

const leftArrow = document.querySelector(".swiper-button-prev")
const rightArrow = document.querySelector(".swiper-button-next")

let slidesArr = Array.from(slideSections)
console.log(slidesArr)

var sectionIndex = 0;

rightArrow.addEventListener("click", function() {
    if (sectionIndex < 0) {
        sectionIndex = 0
    }
    if (sectionIndex == 3) {
        return
    } else {
        if(sectionIndex != slidesArr[sectionIndex]) {
            slidesArr[sectionIndex].style.display = "none"
        } 
        sectionIndex = sectionIndex +1
    }

})

leftArrow.addEventListener("click", function() {
    if (sectionIndex <= -1) {
        return
    } else {
        if(sectionIndex != slidesArr[sectionIndex]) {
            slidesArr[sectionIndex].style.display = "hide"
            sectionIndex = sectionIndex -1
            slidesArr[sectionIndex].style.display = "flex"
        } 

    }
})