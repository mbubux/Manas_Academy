
// PROGRESS BAR

const filled = document.querySelector('.filled');

function updateProgressBar() {
    filled.style.width = `${((window.scrollY) / (document.body.scrollHeight - window.innerHeight) * 100)}%`;
    requestAnimationFrame(updateProgressBar)
}

updateProgressBar();
// Open Menu
function openMenu() {
    document.getElementById('navbar-lists').style.display = "flex";
    document.getElementById('close-icon').style.display = "block";
    document.getElementById('menu-icon').style.display = "none";
    document.getElementById('close-icon').style.zIndex = "999";
    document.querySelector('body').style.overflow = "hidden";

}

// Close Menu
function closeMenu() {
    document.getElementById('navbar-lists').style.display = "none";
    document.getElementById('close-icon').style.display = "none";
    document.getElementById('menu-icon').style.display = "block";
    document.querySelector('body').style.overflow = "visible";
}

// Play video
function playVideo() {
    document.getElementById('play-icon').style.display = "none";
    document.getElementById('about-video').play();
    document.getElementById('about-video').addEventListener('play', () => {
        document.getElementById('pause-icon').style.display = "block";
    });
}

// Pause Video
function pauseVideo() {
    document.getElementById('pause-icon').style.display = "none";
    document.getElementById('about-video').pause();
    document.getElementById('about-video').addEventListener('pause', () => {
        document.getElementById('play-icon').style.display = "block";
    });
}

// CAROUSEL
let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}



function showEvent(n) {
    let id_num = n.id;
    if (id_num == 1) {
        for (let i = 1; i <= 5; ++i) {
            if (i == id_num) {
                document.getElementById("event" + i).style.display = "flex";
                document.getElementById(i).style.color = "var(--primary-green-color)";
            }
            else {
                document.getElementById("event" + i).style.display = "none";
                document.getElementById(i).style.color = "#000";
            }
        }
    }
    else if (id_num == 2) {
        for (let i = 1; i <= 5; ++i) {
            if (i == id_num) {
                document.getElementById("event" + i).style.display = "flex";
                document.getElementById(i).style.color = "var(--primary-green-color)";
            }
            else {
                document.getElementById("event" + i).style.display = "none";
                document.getElementById(i).style.color = "#000";
            }
        }
    }
    else if (id_num == 3) {
        for (let i = 1; i <= 5; ++i) {
            if (i == id_num) {
                document.getElementById("event" + i).style.display = "flex";
                document.getElementById(i).style.color = "var(--primary-green-color)";
            }
            else {
                document.getElementById("event" + i).style.display = "none";
                document.getElementById(i).style.color = "#000";
            }
        }
    }
    else if (id_num == 4) {
        for (let i = 1; i <= 5; ++i) {
            if (i == id_num) {
                document.getElementById("event" + i).style.display = "flex";
                document.getElementById(i).style.color = "var(--primary-green-color)";
            }
            else {
                document.getElementById("event" + i).style.display = "none";
                document.getElementById(i).style.color = "#000";
            }
        }
    }
    else if (id_num == 5) {
        for (let i = 1; i <= 5; ++i) {
            if (i == id_num) {
                document.getElementById("event" + i).style.display = "flex";
                document.getElementById(i).style.color = "var(--primary-green-color)";
            }
            else {
                document.getElementById("event" + i).style.display = "none";
                document.getElementById(i).style.color = "#000";
            }
        }
    }
}


// ====== ADMISSION FORM PHOTO UPLOAD ======

// $("input[type='image']").click(function() {
//     $("input[id='studentPhoto']").click();
// });

// let imgUpload = document.querySelector('input[type=image]');
// imgUpload.addEventListener('click', function() {
//     let studentPhoto = document.querySelector('input[id=studentPhoto]');
//     studentPhoto.click();
// })

// Copyright year update
// const date = new Date();
// let year = date.getFullYear();
// let copyrightYear = document.querySelector('#copyright-year');
// copyrightYear.innerHTML = year;
// ====================x==================

// document.querySelectorAll("input[type='image']").click(function() {
//     document.querySelectorAll("input[id='studentPhoto']").click();
//     let i = document.querySelectorAll("input[type='file']");
//     console.log(i.id);
// });


