# If you are running this script on Habrok, don't forget to load Python2!
# First run: module load Python/2.7.18-GCCcore-12.2.0-bare

from patch import patch

p = patch(vfrac=0.1)
p.lattice = [8, 8, 8]
p.build(4*8**2, "ring", 2, 2, 1, 2) # particles with 2 patches
p.build(4*8**2, "ring", 2, 3, 1, 2) # particles with 3 patches
p.write("init.data")
