# nmm-week5

What is a particle? In celebration of spherical cows, this week introduces Coarse-Grained MD, where the beads of the simulation do not necessarily correspond to individual atoms. These models lose predictive power but gain tremendous flexibility. In this week's assignment you will focus on separate particles with complex interatomic interactions, able to represent many materials from Quantum Dots to Yogurt!

## Assignment 1

The key for building new CG models is to calibrate the definition and interactions of your CG beads, either with bottom-up (e.g. from AA simulations) or top-down (e.g. from experimental results) approaches. For simple spherical particles, a common approach is to calculate the Potential of Mean Force (PMF) between two "particles". Let's do that for fullerene!

### Instructions

1a Use the structure file "fullerene.data" (ADAPT FROM https://www.ericnhahn.com/tutorials/lammps-tutorials/carbon-structures, REMOVING A BOND FROM THE GRAPHULLERINE STRUCTURE) and the in.PMF script (CREATE THIS. THINK WHAT SHOULD BE ALREADY THERE AND WHAT THEY SHOULD DO). Systematically move the two fullerene particles and calculate the intermolecular force as a function of distance. Fit the function with a Lennard-Jones potential (TEST IF EASY) and report your findings.

1b Create two simulations, one with many fullerene molecules and one with many CG beads (adapt in.3dlj, but with proper units BE MORE SPECIFIC ON INSTRUCTIONS HERE) interacting with the potential derived in 1a. Compare the radial distribution functions between the two simulations.

## Assignment 2

Not bound to the periodic table anymore! We can now design "atoms" with arbitrary interactions begging the question: what structures will they form based on their pair interactions? In this assignment let's play with pairwise interactions and phase diagrams.

### Instructions

2a. Take again the in.3dlj script from the first assignment, but change the Lennard-Jones cutoff from 1.2 to 2.5. Now interactions are attractive! Fix the temperature to 1.0, and vary the density and the interaction strength. Briefly discuss the differences between varying temperature and varying LJ interaction strength.
Run a set of simulations to identify and discuss the expected theoretical phase diagram https://en.wikipedia.org/wiki/Lennard-Jones_potential. Support your arguments with the set of structural and dynamics properties that you deem appropriate.

2b. DLVO, charges. CHECK PAIR_COLLOID AND PHASE DIAGRAMS IN LITERATURE.

## Assignment 3



### Instructions

3a. Switch to patchy particles with 2 patches. Check phase diagram. (CHECK PAPERS, QUESTIONS DEPEND ON LITERATURE AND MODELS WE IMPLEMENT)


3b. Switch to 3-4 patches. Check phase diagram. (CHECK PAPERS, QUESTIONS DEPEND ON LITERATURE AND MODELS WE IMPLEMENT)

## Assignment 4

Intro

### Instructions

4a. 

4b. 
