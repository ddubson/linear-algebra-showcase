% Generate two vectors 
v1 = [ -3 4 5]';
v2 = [ 3 6 -3]';

% Generate two scalars
s1 = 2;
s2 = 3;

% Compute dot product between two vectors
disp(['Original: ' num2str(dot(v1,v2))]);

% Compute the dot product between scaled vectors
disp(['Scaled:   ' num2str(dot((s1*v1),(s2*v2))) ])