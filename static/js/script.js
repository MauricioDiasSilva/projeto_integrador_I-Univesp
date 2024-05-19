var slides = document.querySelectorAll('.carrossel .slide');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide, 2000); // Muda o slide a cada 2 segundos

function nextSlide() {
    slides[currentSlide].style.opacity = 0;
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].style.opacity = 1;
}