carrusel = await Response.json();
let html="";
for (dato of carrusel){
    let contador=0;
    if (contador == 0){
        contador="activo"
    }
}

let row = '
<div class="carousel-item img-1 min-vh-100 active $(dato.descripcion)">
<div class="carousel-caption d-md-block">
  <h5 class="fw-bold">Ingresa tus dispositivos</h5>
  <p>
    <a href="#login" class="fw-bold Sesion">
      Ingresa
      <i class="bi bi-arrow-down-circle-fill estilo-especial"></i>
    </a>
  </p>
</div>
</div>