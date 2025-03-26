# nmm-week5

What is a particle? In celebration of spherical cows, this week introduces Coarse-Grained MD, where the beads of the simulation do not necessarily correspond to individual atoms. These models lose predictive power but gain tremendous flexibility. In this week's assignment you will focus on separate particles with complex interatomic interactions, able to represent any colloidal material from Quantum Dots to Yogurt!

## Assignment 1

The key for building new CG models is to calibrate the definition and interactions of your CG beads, either with bottom-up (e.g. from AA simulations) or top-down (e.g. from experimental results) approaches. For simple spherical particles, a common approach is to calculate the Potential of Mean Force (PMF) between two "particles". Let's do that for fullerene!

### Instructions

1a Use the structure file "fullerene.data" (ADAPT FROM https://www.ericnhahn.com/tutorials/lammps-tutorials/carbon-structures, REMOVING A BOND FROM THE GRAPHULLERINE STRUCTURE) and the in.PMF script (CREATE THIS. THINK WHAT SHOULD BE ALREADY THERE AND WHAT THEY SHOULD DO). Systematically move the two fullerene particles and calculate the intermolecular force as a function of distance. Fit the function with a Lennard-Jones potential (TEST IF EASY) and report your findings.

1b Create two simulations, one with many fullerene molecules and one with many CG beads (adapt in.3dlj, but with proper units BE MORE SPECIFIC ON INSTRUCTIONS HERE) interacting with the potential derived in 1a. Compare the radial distribution functions between the two simulations. Compare also the computational efficiency of the two simulations.

## Assignment 2

Not bound to the periodic table anymore! We can now design "atoms" with arbitrary interactions begging the question: what structures will they form based on their pair interactions? In this assignment let's play with widely-used pairwise interactions and phase diagrams.

### Instructions

2a. Take again the in.3dlj script from the first assignment, but change the Lennard-Jones cutoff from 1.2 to 2.5. Now interactions are attractive! Fix the temperature to 1.0, and vary the density and the interaction strength. Briefly discuss the differences between varying temperature and varying LJ interaction strength.
Run a set of simulations to identify and discuss the expected theoretical phase diagram https://en.wikipedia.org/wiki/Lennard-Jones_potential. Support your arguments with the set of structural and dynamics properties that you deem appropriate.

2b. DLVO. CHECK PAIR_YUKAWA/COLLOID AND PHASE DIAGRAMS IN LITERATURE (E.G., CHECK https://doi.org/10.1063/1.453924).

## Assignment 3

Not all colloidal particles have spherical, isotropic interactions! Directional interactions are often present, as a result of internal chemical structure or functionalization. In this assignment, learn how directional interactions can be implemented by adding attractive patches.

### Instructions

3a. Switch to patchy particles with 2 patches. Check phase diagram. (CHECK PAPERS, QUESTIONS DEPEND ON LITERATURE AND MODELS WE IMPLEMENT)


3b. Switch to 3-4 patches. Check phase diagram. (CHECK PAPERS, QUESTIONS DEPEND ON LITERATURE AND MODELS WE IMPLEMENT)

## Assignment 4

Equilibrium phase diagrams are fun, but colloids are very interesting non-newtonian fluids! Let's check their rheological properties in this assignment. 

### Instructions

4a. Shear thinning: structure/contacts evolution+viscosity

4b. Shear thickening: structure/contacts evolution+viscosity
