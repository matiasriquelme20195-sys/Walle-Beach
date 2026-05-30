int led_rojo = 0 #el Led rojo está conectado al Pin 0 del Arduino
int led_amarillo = 1 #el Led amarillo está conectado al Pin 1 del Arduino
int led_verde = 2 #el Led verde está conectado al Pin 2 del Arduino

configuración_vacía() {
#configurar todos los leds como Salida
  pinMode(led_rojo, Salida)
  pinMode(led_amarillo, Salida)
  pinMode(led_verde, Salida)
}

bucle_vacio() {
#encender el led verde y apagar los demás LEDs
  digitalWrite(led_rojo, abajo) 
  digitalWrite(led_amarillo, abajo)
  digitalWrite(led_verde, arriba)
  delay(2000) #esperar 2 segundos

#encender el led amarillo y apagar los demás LEDs
  digitalWrite(led_rojo, abajo)   
  digitalWrite(led_amarillo, arriba)
  digitalWrite(led_verde, abajo)
  delay(1000) #esperar 1 segundo
  
#encender el Led rojo y apagar los demás LEDs
  digitalWrite(led_rojo, arriba)  
  digitalWrite(led_amarillo, abajo)
  digitalWrite(led_verde, abajo)
  delay(3000) #esperar 3 segundos   
}