// Paso 1. Declara una clase con el nombre exacto: Cuadrado
class Cuadrado {

  // Paso 2. Constructor que recibe el parámetro: lado
  constructor(lado) {
    // Paso 3. Asignación al atributo de instancia
    this.lado = lado;
  }

  // Paso 4. Método para devolver el perímetro (4 * lado)
  calcularPerimetro() {
    return 4 * this.lado;
  }

  // Paso 5. Método para devolver el área (lado * lado)
  calcularArea() {
    return this.lado * this.lado;
  }
}

// Paso 6. Crear una instancia con el valor 7
const figura = new Cuadrado(7);

// Paso 7. Imprimir el perímetro siguiendo el formato exacto
console.log("Perimetro:", figura.calcularPerimetro());

// Paso 8. Imprimir el área siguiendo el formato exacto
console.log("Area:", figura.calcularArea());