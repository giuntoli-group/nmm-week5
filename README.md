# nmm-week5

In celebration of spherical cows, this week introduces Coarse-Grained MD, where the beads of the simulation do not necessarily correspond to individual atoms. These models lose predictive power but gain tremendous flexibility. In this week's assignment, you will focus on separate particles with complex interatomic interactions, able to represent any colloidal material from Quantum Dots to Yogurt!

## Assignment 1 - What is a particle?

The key for building new CG models is to calibrate the definition and interactions of your CG beads, either with bottom-up (e.g. from AA simulations) or top-down (e.g. from experimental results) approaches. For simple spherical particles, a common approach is to calculate the [Potential of Mean Force (PMF)](https://en.wikipedia.org/wiki/Potential_of_mean_force) between two "particles". Let's do that for fullerene in vacuum!

### Instructions

1a. After visualizing the c60-bonds.data file, run the fullerene-PMF.in simulation. 

(i) What is the role of the looping structure in this simulation?

(ii) From the thermodynamic information in the log file/the trajectory, extract two plots: the force and the potential energy between the two molecules as a function of the distance between their centers of mass. GIVE POST-PROCESSING INSTRUCTIONS HERE. 
Note that the sampling done in the given simulation script is quite simplistic to make the simulation shorter. OPTIONAL: how does the result change with much longer sampling at each step of the loop?

1b. Time to coarse-grain!

(i) Fit your potential energy plot with an interatomic potential function of your choice and report the values of the fitting parameters.

(ii) How would you now define a simulation of coarse-grained particles interacting with your effective potential? Specify all the information you would need to set it up.

## Assignment 2 - Just Jamming

Not bound to the periodic table anymore! We can now design "atoms" with arbitrary interactions, begging the question: what structures will they form based on their interaction potentials? In this assignment, let's discover the phases of the well-known [Lennard-Jones fluid](https://en.wikipedia.org/wiki/Lennard-Jones_potential).

### Instructions

2a. Take the new in.3dlj script, using a cutoff of 2.5 for the Lennard-Jones potential. 

(i) Fix the temperature to 1.0, and vary the particle density and interaction strength. Report snapshots and quantitative metrics (on structure and/or dynamics) for different phases of the system, including at least a liquid phase, a "gas+solid" phase, and a crystalline phase. Pro tip: equilibrate long enough, and stay far away from the phase boundaries unless you want to wait for a long time.

## Assignment 3 - Patch up

Not all colloidal particles have spherical, isotropic interactions! Directional interactions are often present as a result of internal chemical structure or functionalization. In this assignment, learn how directional interactions can be implemented by adding attractive patches on inert cores.

### Instructions MORE DETAILS AFTER TESTING

3a. Switch to patchy particles with 2 patches. Explore phase diagram/structures.

3b. Switch to 3-4 patches. Explore phase diagram, find at least N phases.

## Assignment 4 - Look Ma, no hands!

Equilibrium phase diagrams are fun, but colloids are very interesting non-Newtonian fluids! Let's check their rheological properties in this assignment. 

### Instructions

4a. Shear thinning: start from final structure of assignment 2, with epsilon=? and density=? 

(i) run the simulation shear.in, extract+plot stress curve, calculate viscosity in steady state.

(ii) repeat for different shear rates. Plot viscosity(shear rate). Power law? Lower limit for zero shear viscosity? 

4b. (OPTIONAL, HARD) Calculate the zero shear viscosity. This can be done in a couple of ways [(or more, none easy)](https://docs.lammps.org/Howto_viscosity.html):

(i) Keep doing what you were doing in 4a, but MUUUCH slower. Arm yourself with patience, and good luck!

(ii) Use the Green-Kubo formalism to extract the viscosity from the ensemble average of the auto-correlation of the stress tensor. Good luck!


