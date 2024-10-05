
let slideIndex = 0;
showSlides(slideIndex);

function moveSlide(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("carousel-item");
    if (n >= slides.length) { slideIndex = 0 }
    if (n < 0) { slideIndex = slides.length - 1 }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex].style.display = "block";
}

// Lista de valores a serem adicionados
const valores = [
    "Empatia: Nós nos esforçamos para entender e compartilhar os sentimentos de nossas crianças e suas famílias.",
    "Respeito: Valorizamos a individualidade e a dignidade de cada criança que atendemos.",
    "Integridade: Estamos comprometidos em agir com honestidade, transparência e consistência.",
    "Inovação: Buscamos constantemente novas e melhores maneiras de atender nossas crianças e suas famílias.",
    "Colaboração: Trabalhamos juntos para alcançar nossos objetivos e fazer a diferença."
];

// Função para gerar a lista de valores
function gerarListaValores() {
    const ulValores = document.getElementById('valores');

    // Itera sobre o array de valores e cria elementos <li>
    valores.forEach(valor => {
        const li = document.createElement('li');
        li.innerHTML = `<span class="Empatia">${valor.split(':')[0]}:</span> ${valor.split(':')[1]}`; // Divide o texto em título e descrição
        ulValores.appendChild(li); // Adiciona <li> à <ul>
    });
}

// Chama a função para gerar a lista ao carregar a página
document.addEventListener('DOMContentLoaded', gerarListaValores);
