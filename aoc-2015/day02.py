packages = []
for line in open("input/02.txt"):
    package = list(map(int, line.split("x")))
    packages.append(sorted(package))

areas = [(2*x*y + 2*x*z + 2*y*z + min(x*y, x*z, y*z), 2*x + 2*y + x*y*z) for (x, y, z) in packages]
required_materials = [sum(x) for x in zip(*areas)]
print(*required_materials, sep="\n")
