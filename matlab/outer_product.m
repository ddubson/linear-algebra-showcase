v1 = [ 1 2 3 ]'; % transpose with a single quote to create a column vector
v2 = [-1 0 1 ]';

% dot (inner) product
v1' * v2    % representing the dot product formular a(T)b (a transposed times b)
dot(v1, v2) % same as previous line

% outer product
v1 * v2'    % representing outer product formula vw(T) (v * w transposed)