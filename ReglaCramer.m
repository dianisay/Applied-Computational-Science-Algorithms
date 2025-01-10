% Matriz de coeficientes
A = [1 3; 1.5 2];

% Vector de términos independientes
b = [300; 350];

% Solución del sistema
x = linsolve(A, b);

fprintf("La empresa puede fabricar %0.1f unidades del tipo A y %0.1f unidades del tipo B al mes\n", x(1), x(2));
