// Aqui se importa la libreria estandar de entra y salida                                 
#Include <stdio.h>

// Se define la funcion principal la cual no devuelve ningun tipo de dato                 
void main() {
  // definimos una variable entera llamada edad                                           
    int edad = 40;
    /*                                                                                    
     * Definimos un puntero el cual hace referencia                                       
     * a la variable edad .                                                               
     */
    int *edad_puntero = &edad;
  // Mostramos en pantalla el valor que tiene la variable edad                          
    printf("El valor de la edad es: %d \n", edad);
    /**                                                                                   
     * Mostramos en pantalla la direccion en memoria de la variable edad                  
     * mediante el apuntador                                                              
     */
    printf("La direccion de la variable edad es: %p \n", edad_puntero);
    /**                                                                                   
     * Mostramos en pantalla el valor que tiene la referencia en memoria                          
     * mediante el apuntador                                                              
     */
    printf("El valor de la variables a la que hace referencia es: %d \n", *edad_puntero);

}
