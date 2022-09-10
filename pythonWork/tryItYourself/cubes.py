# A number raised to the third power is called a cube. Written in python like: 2 ** 3
# Make a list of the first 10 cubes using a for loop to print out the value of the cube.

cubes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for cube in cubes:
    print(cube ** 3)

cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)
