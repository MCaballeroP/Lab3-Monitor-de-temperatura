//Variable donde almacenaremos el numero aleatorio
long randomNumber;
 
//Función de inicialización
void setup() {
  
  //Inicializamos la comunicación serial
  Serial.begin(9600);
  
  //Escribimos por el puerto serie mensaje de inicio
  Serial.println("Inicio de sketch - secuencia de numeros aleatorios");
      
  //Establecemos la semilla fija
  randomSeed(39);         
}
 
//Bucle principal
void loop() {
 
  //Genera un numero aleatorio entre 20 y 45
  randomNumber = random(20,45);
  
  Serial.print("la temperatura es = ");
  Serial.println(randomNumber);
 
  //Esperamos 1 segundo para repetir
  delay(1000);
}
