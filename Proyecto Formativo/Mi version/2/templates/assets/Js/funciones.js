document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://127.0.0.1:5000/api/";

let carrusel = []

function init() {
    verImagenes()
}

async function verImagenes() {
    let url = URL_API + "carrusel"
    //hacer la peticion
    let response = await fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });

    carrusel = await response.json();
    let html = "";
    let botones = "";
    let c = 0;
    for (dato of carrusel) {
        if (c == 0) {
            contador = "active";
        } else {
            contador = ""
        }
        let row2 = `
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="`+ c + `" class="` + contador + `" aria-current="true" aria-label="Slide 1">
        </button>
        `;

        c++;

        let row = `
            <div class="carousel-item img-1 min-vh-100 `+contador+`" 
              style = "background-image: url(Assets/Img/carrusel/${dato.img});">
                <div class="carousel-caption text-center d-md-block">
                  <h5 class="fw-bold">${dato.descripcion}</h5>
                  <p>
                    <a href="#login" class="fw-bold Sesion">
                      Ingresa
                      <i class="bi bi-arrow-down-circle-fill estilo-especial"></i>
                    </a>
                  </p>
                </div>
            </div>
        `
        botones = botones + row2;
        html = html + row;
    }

    document.getElementById("carruselContenido").innerHTML = html;
    document.getElementById("carruselBotones").innerHTML = botones;
}
