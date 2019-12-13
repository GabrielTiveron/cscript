# cscript

Nossa linguagem é uma representação limitada da linguagem C.

## Como executar
Para executar a linguagem é necessário apenas o docker e o docker-compose, após instalar os dois é necessário utilizar o seguinte comando no terminal
```
sudo docker-compose up
```
## Funções disponíveis

### Operadores lógicos

```
a + b
a / b
a * b
a - b
a ^ b
```

### Operadores condicionais

```
a == b
a != b
a < b
a > b
a <= b
a >= b
```

### Operadores booleanos

```
T para true
F para false
```

### Operador ternário

```
condition ? true : false
```

### Criação de funções

```
func lambda(a, b, ...) {
  code
}
```

### Chamada de funções

```
lambda(a, b, ...);
```

### Loops

```
a = 2;
    for(b = 3; b <= 10; b = b + 1){
        a = a + b
    };
```
Também há a possibilidade de usar loops por meio do while

```
a = 1;
    while(a < 10){
        a = a + 1
    }
```

### Criação de condicionais

```
if (condition) {
  // block of code
} else if (condition) {
  // block of code
} else {
  // block of code
}
```
