// Efecto de animación al hacer scroll
const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY + window.innerHeight / 1.2;

  sections.forEach(section => {
    if (scrollY > section.offsetTop) {
      section.style.opacity = 1;
      section.style.transform = 'translateY(0)';
    }
  });
});

// Animación inicial de las secciones
sections.forEach(section => {
  section.style.opacity = 0;
  section.style.transform = 'translateY(50px)';
  section.style.transition = 'all 0.8s ease-out';
});

// Botón para ir directo a descargar
const downloadBtn = document.querySelector('.download');
if (downloadBtn) {
  downloadBtn.addEventListener('click', () => {
    alert('¡Descargando Turbo Galaxy! 🚀🌴');
  });
}
