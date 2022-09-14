let equipo1 = document.getElementById('equipo1');
let equipo2 = document.getElementById('equipo2');
let equipo3 = document.getElementById('equipo3');

let infoequipo1 = document.getElementById('infoequipo1');
let infoequipo2 = document.getElementById('infoequipo2');
let infoequipo3 = document.getElementById('infoequipo3');
let carouselid = document.getElementById('carouselExampleIndicators');

let control1 = 0;
let control2 = 0;
let control3 = 0;

let clickmodificar = document.getElementById('clickmodificar');
let btneliminar = document.getElementById('btneliminar');


equipo1.addEventListener('click',()=>{
    control2=0;
    control3=0;
    if (control1 == 0){
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 2; opacity: 1;"
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control1=1;
    }else{
        carouselid.style ="z-index: 2; opacity: 1;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control1=0;
    }
})

equipo2.addEventListener('click',()=>{
    control1=0;
    control3=0;
    if (control2 == 0){
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 2; opacity: 1;"
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control2=1;
    }else{
        carouselid.style ="z-index: 2; opacity: 1;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control2=0;
    }
})

equipo3.addEventListener('click',()=>{
    control1=0;
    control2=0;
    if (control3 == 0){
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 2; opacity: 1;"
        carouselid.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control3=1;
    }else{
        carouselid.style ="z-index: 2; opacity: 1;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        control3=0;
    }
})
let checkTrue1 = false;
let checkTrue2 = false;
let checkTrue3 = false;
function doubleclick(){
    checkTrue1 = document.getElementById('modificar1').checked;
    checkTrue2 = document.getElementById('modificar2').checked;
    checkTrue3 = document.getElementById('modificar3').checked;
    if(checkTrue1){ 
        clickmodificar.setAttribute("data-bs-toggle","modal")
        clickmodificar.setAttribute("data-bs-target","#modificarequipo1")
    }
    else if(checkTrue2){
        clickmodificar.setAttribute("data-bs-toggle","modal")
        clickmodificar.setAttribute("data-bs-target","#modificarequipo2")
    }
    else if(checkTrue3){
        clickmodificar.setAttribute("data-bs-toggle","modal")
        clickmodificar.setAttribute("data-bs-target","#modificarequipo3")
    }
}
function validarCheck(){
    if(!checkTrue1 && !checkTrue2 && !checkTrue3){
        alert("Selecciona algún equipo a modificar.")
    }
}

let checkarTrue1 = document.getElementById('modificar1')
let checkarTrue2 = document.getElementById('modificar2')
let checkarTrue3 = document.getElementById('modificar3')



checkarTrue1.addEventListener('click',()=>{
    doubleclick()
})
checkarTrue2.addEventListener('click',()=>{
    doubleclick()
})
checkarTrue3.addEventListener('click',()=>{
    doubleclick()
})

let generarqr = document.getElementById('generarqr');
let qr1 = document.getElementById('qr1');
let qr2 = document.getElementById('qr2');
let qr3 = document.getElementById('qr3');
let controlqr1 = 0;
let controlqr2 = 0;
let controlqr3 = 0;


generarqr.addEventListener('click',()=>{
    let checkTrueV1 = document.getElementById('modificar1').checked
    let checkTrueV2 = document.getElementById('modificar2').checked
    let checkTrueV3 = document.getElementById('modificar3').checked
    control1 = 0;
    control2 = 0;
    control3 = 0;
    if (checkTrueV1){
        controlqr1 = 1;
        controlqr2 = 0;
        controlqr3 = 0;
    }
    if (checkTrueV2){
        controlqr1 = 0;
        controlqr2 = 1;
        controlqr3 = 0;
    }
    if (checkTrueV3){
        controlqr1 = 0;
        controlqr2 = 0;
        controlqr3 = 1;
    }
    if (controlqr1 == 1){
        carouselid.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 2; opacity: 1;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        controlqr1=2;
    }else if (controlqr1 == 2){
        carouselid.style ="z-index: 2; opacity: 1;"
        qr1.style ="z-index: 1; opacity: 0;"
        controlqr1=0;
    }
    else if (controlqr2 == 1){
        carouselid.style ="z-index: 1; opacity: 0;"
        qr2.style ="z-index: 2; opacity: 1;"
        qr1.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"
        controlqr2=2;
    }else if (controlqr2 == 2){
        carouselid.style ="z-index: 2; opacity: 1;"
        qr2.style ="z-index: 1; opacity: 0;"
        controlqr2=0;
    }
    else if (controlqr3 == 1){
        carouselid.style ="z-index: 1; opacity: 0;"
        qr3.style ="z-index: 2; opacity: 1;"
        qr2.style ="z-index: 1; opacity: 0;"
        qr1.style ="z-index: 1; opacity: 0;"
        infoequipo2.style ="z-index: 1; opacity: 0;"
        infoequipo1.style ="z-index: 1; opacity: 0;"
        infoequipo3.style ="z-index: 1; opacity: 0;"    
        controlqr3=2;
    }else if (controlqr3 == 2){
        carouselid.style ="z-index: 2; opacity: 1;"
        qr3.style ="z-index: 1; opacity: 0;"
        controlqr3=0;
    }

    
})


btneliminar.addEventListener('click',()=>{
    let checkTrue1 = document.getElementById('modificar1').checked;
    let checkTrue2 = document.getElementById('modificar2').checked;
    let checkTrue3 = document.getElementById('modificar3').checked;
    if(checkTrue1){
        alert('¿Desea eliminar el equipo "Hp"?')
    }
    else if(checkTrue2){
        alert('¿Desea eliminar el equipo "Acer"?')
    }
    else if(checkTrue3){
        alert('¿Desea eliminar el equipo "Toshiba"?')
    }
})