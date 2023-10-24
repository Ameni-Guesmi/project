const slide = ["caméra.jpg", "phone.jpg", "samsung.jpg"];
let numero = 0;

function ChangeSlide(sens) {
    numero = numero + sens;
    if (numero > slide.length - 1)
        numero = 0;
    if (numero < 0)
        numero = slide.length - 1;

    const staticImagePath = "{% static 'image/' %}";
    const imageSrc = staticImagePath + slide[numero];
    document.getElementById("slide").src = imageSrc;
}

setInterval(() => ChangeSlide(1), 4000);