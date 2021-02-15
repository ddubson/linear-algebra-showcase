# Create a complex number
z = complex(3, 4);

# Magnitude
norm(z)

# By transpose?
transpose(z)*z

# By Hermitian transpose
z'*z

# Not the Hermitian
z.'*z

# More complex vector
v = [ 3 4i 5+2i complex(2,-5) ]
v'
v.'
transpose(v)