// retorna a sequencia de Collatz para o número dado
// Argumento deve ser um número inteiro
func collatz(n){
  if(n == 1){
    return [1]
  }
  else if(n % 2 == 0){
    return collatz(n / 2)
  }
  else{
    return collatz((3 * n) + 1)
  }

}

// Imprime a sequência de Collatz de 42
printf(collatz(42))
