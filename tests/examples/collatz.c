// retorna a sequencia de Collatz para o número dado
// Argumento deve ser um número inteiro
func collatz(n){
  if(n == 1){
    [1];
  }
  else if(n % 2 == 0){
    n = collatz(n / 2);
  }
  else{
    n = collatz((3 * n) + 1);
  }

}

// Imprime a sequência de Collatz de 42
printf(collatz(42))
