
var nombre = "toni";
var altura = 170;


 
// document.write(nombre); // mostrando datos por pantalla
// document.write(altura);

// var concatenar = nombre + " " + altura

// var datos = document.getElementById("datos"); // llamamos elementos por id.
// datos.innerHTML = `

//     <h1> hablo desde la caja </h1>
//     <h2> Mi nombre es: ${nombre}</h2> 
//     <h3> mido: ${altura} cm </h3>

//     `;

// if (altura >= 190) {

//     datos.innerHTML += '<h1> Eres una persona alta </h1>';

// }else{
//     datos.innerHTML += '<h1> Eres una persona bajita </h1>';
// }


// for (let i = 0; i < 2020 ; i++) {
//     datos.innerHTML += "<h2> Estamos en el año: "+i;
    
// }
 
function MuestraNombre(nombre, altura) {
    

    var misDatos = `

        <h1> hablo desde la caja </h1>
        <h2> Mi nombre es: ${nombre}</h2> 
        <h3> mido: ${altura} cm </h3>

    `;
    return misDatos;
}

function Imprimir() {
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraNombre("Piraña guau", 70)
    
}

Imprimir();


var nombres = ['toni','piraña','mandy'];
// alert(nombres[1]);

document.write('<h1>Listado de nombres</h1>');
// for(i = 0; i < nombres.length; i++){
//     document.write(nombres[i] + '<br/>');
// }

nombres.forEach((nombre) => {
    document.write(nombre + '<br/>');
})






