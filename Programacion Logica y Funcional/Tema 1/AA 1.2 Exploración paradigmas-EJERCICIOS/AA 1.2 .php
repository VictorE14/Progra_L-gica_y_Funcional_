
<?php
echo "Ejercicio 1\n";
// Ejercicio 1: Solo imprimir texto
// Se ejecuta de manera secuencial, de la línea 4 a la 5.

echo "¡Hola! Este es un programa secuencial muy sencillo en PHP.\n";
?>


<?php
// Ejercicio 2: Uso de funciones integradas (built-in) de PHP

echo "Ejercicio 2\n";
$texto_original = "ingeniería en sistemas";

// Usamos strtoupper() para convertir a mayúsculas y strlen() para contar caracteres
$texto_mayusculas = strtoupper($texto_original);
$longitud = strlen($texto_original);

echo "Texto original: " . $texto_original . "\n";
echo "Texto modificado: " . $texto_mayusculas . "\n";
echo "El texto tiene " . $longitud . " caracteres.\n";

// Usamos rand() de la biblioteca matemática para generar un número aleatorio
$numero_aleatorio = rand(1, 100);
echo "Número de la suerte generado: " . $numero_aleatorio . "\n";

?>

<?php
// Ejercicio 3: Control de flujo (Toma de decisiones)
echo "Ejercicio 3\n";


$calificacion = 85;

echo "Calificación obtenida: " . $calificacion . "\n";

// Estructura de control if / elseif / else
if ($calificacion >= 90) {
    echo "Resultado: Excelente desempeño. ¡Felicidades!\n";
} elseif ($calificacion >= 70) {
    echo "Resultado: Aprobado. Buen trabajo.\n";
} else {
    echo "Resultado: No aprobado. Es necesario repasar los conceptos.\n";
}
?>


<?php
// Ejercicio 4: Concatenación de distintos tipos de datos
echo "Ejercicio 4\n";
$nombre_lenguaje = "PHP"; // Cadena (String)
$version = 8.3;           // Valor numérico (Float)
$paradigma = "estructurado"; // Cadena (String)

// Concatenación de cadenas y variables usando el punto (.)
$mensaje = "El lenguaje " . $nombre_lenguaje . " (en su versión " . $version . ") " . 
           "es muy flexible y permite programar usando el paradigma " . $paradigma . ".\n";

echo $mensaje;
?>

<?php
// Ejercicio 5: Ejemplificación del paradigma estructurado
echo "Ejercicio 5\n";
/* * 1. MODULARIDAD: Dividimos el problema en funciones más pequeñas.
 * Esta función evalúa si un número es par.
 */
function esPar($numero) {
    // 2. SELECCIÓN: Toma de decisiones
    if ($numero % 2 == 0) { 
        return true;
    } else {
        return false;
    }
}

/*
 * Función principal que orquesta el proceso.
 */

function procesarLista($lista) {
    $sumaPares = 0; // 3. SECUENCIA: Declaración e inicialización
    
    echo "Iniciando análisis de la lista...\n";

    // 4. ITERACIÓN: Bucle para recorrer los datos
    foreach ($lista as $valor) { 
        
        // Llamada a la subrutina (función)
        if (esPar($valor)) { 
            echo "El número " . $valor . " es PAR.\n";
            $sumaPares = $sumaPares + $valor;
        } else {
            echo "El número " . $valor . " es IMPAR.\n";
        }
    }

    echo "-> La suma total de los números pares es: " . $sumaPares . "\n";
}

// Bloque principal de ejecución (Secuencia principal)
$numeros_a_evaluar = [4, 7, 10, 15, 22];
procesarLista($numeros_a_evaluar);

?>




