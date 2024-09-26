// static/js/app.js
function initializeBanner() {
    // Seleciona todas as imagens no banner
    const bannerImages = document.querySelectorAll('.banner-image');
    let currentIndex = 0;

    // Função para mostrar a próxima imagem
    function showNextImage() {
        // Remove a classe 'active' da imagem atual
        bannerImages[currentIndex].classList.remove('active');

        // Atualiza o índice para a próxima imagem
        currentIndex = (currentIndex + 1) % bannerImages.length;

        // Adiciona a classe 'active' à próxima imagem
        bannerImages[currentIndex].classList.add('active');
    }

    // Inicializa o banner com a primeira imagem visível
    bannerImages[currentIndex].classList.add('active');

    // Define o intervalo de troca de imagens (5 segundos neste caso)
    setInterval(showNextImage, 5000);
}

// Chama a função para inicializar o banner
initializeBanner();

// JS para o PAINEL ADM
document.querySelector('.toggle-menu').addEventListener('click', () => {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('show');
});