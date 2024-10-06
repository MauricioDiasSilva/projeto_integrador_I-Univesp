// Primeiro carrossel - troca automática
let slideIndex1 = 0;
function showSlides1() {
    const slides = document.getElementsByClassName("carousel-item");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Esconde todos os slides
    }
    slideIndex1++;
    if (slideIndex1 > slides.length) { slideIndex1 = 1; } // Reinicia o índice se passar do total de slides
    slides[slideIndex1 - 1].style.display = "block"; // Mostra o slide atual
}

// Função para trocar slides automaticamente no primeiro carrossel
function autoSlides1() {
    showSlides1();
}

document.addEventListener('DOMContentLoaded', () => {
    showSlides1(); // Mostra o primeiro slide no carregamento
    setInterval(autoSlides1, 3000); // Muda o slide a cada 3 segundos
});

// Segundo carrossel - troca automática
let slideIndex2 = 0;
function showSlides2() {
    const slides = document.getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Esconde todos os slides
    }
    slideIndex2++;
    if (slideIndex2 > slides.length) { slideIndex2 = 1; } // Reinicia o índice se passar do total de slides
    slides[slideIndex2 - 1].style.display = "block"; // Mostra o slide atual
}

// Função para trocar slides automaticamente no segundo carrossel
function autoSlides2() {
    showSlides2();
}

document.addEventListener('DOMContentLoaded', () => {
    showSlides2(); // Mostra o primeiro slide no carregamento
    setInterval(autoSlides2, 3000); // Muda o slide a cada 3 segundos
});

// Lista de valores
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
    ulValores.innerHTML = ''; // Limpa a lista para evitar duplicações

    valores.forEach(valor => {
        const li = document.createElement('li');
        li.innerHTML = `<span class="titulo-valor">${valor.split(':')[0]}:</span> ${valor.split(':')[1]}`;
        ulValores.appendChild(li);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    gerarListaValores(); // Gera a lista de valores
});
