% Generar 16 puntos aleatorios
num_points = 16;
points = randi([1 255], num_points, 2);

% Crear una matriz de 256x256 para representar el espacio de píxeles
pixels = zeros(256, 256);

% Escanear la matriz pixel a pixel y determinar cuál de los 16 puntos es el más cercano a cada píxel
for i = 1:256
for j = 1:256
distances = zeros(num_points, 1);
for k = 1:num_points
distances(k) = norm([i j] - points(k,:));
end
[~, index] = min(distances);
pixels(i, j) = index;
end
end

% Recolorear cada píxel con un color diferente indicativo de su nodo correspondiente
colors = hsv(num_points);
rgb_pixels = zeros(256, 256, 3);
for i = 1:256
for j = 1:256
index = pixels(i, j);
rgb_pixels(i, j, :) = colors(index, :);
end
end

% Visualizar el resultado usando la función mesh() de Matlab
[X, Y] = meshgrid(1:256, 1:256);
Z = zeros(256, 256);

mesh(X, Y, Z, rgb_pixels);
view(3);
