# nmm-week5

In celebration of spherical cows, this week introduces Coarse-Grained MD, where the beads of the simulation do not necessarily correspond to individual atoms. These models lose predictive power but gain tremendous flexibility. In this week's assignment, you will focus on separate particles with complex interatomic interactions, able to represent any colloidal material from Quantum Dots to Yogurt!

## Assignment 1 - What is a particle?

The key for building new CG models is to calibrate the definition and interactions of your CG beads, either with bottom-up (e.g. from AA simulations) or top-down (e.g. from experimental results) approaches. For simple spherical particles, a common approach is to calculate the [Potential of Mean Force (PMF)](https://en.wikipedia.org/wiki/Potential_of_mean_force) between two "particles". Let's do that for fullerene in vacuum!

### Instructions

1a. After visualizing the c60-bonds.data file, run the fullerene-PMF.in simulation. MAKE FILE NAMES COHERENT

(i) What is the role of the looping structure in this simulation?

(ii) From the thermodynamic information in the log file/the trajectory, extract two plots: the force and the potential energy between the two molecules as a function of the distance between their centers of mass. GIVE POST-PROCESSING INSTRUCTIONS HERE. 

1b. Time to coarse-grain!

(i) Fit your potential energy plot with an interatomic potential function of your choice and report the values of the fitting parameters. 

(ii) How would you now define a simulation of coarse-grained particles interacting with your effective potential? Specify all the information you would need to set it up.

## Assignment 2 - Just Jamming

Not bound to the periodic table anymore! We can now design "atoms" with arbitrary interactions, begging the question: what structures will they form based on their interaction potentials? In this assignment, let's discover the phases of the well-known [Lennard-Jones fluid](https://en.wikipedia.org/wiki/Lennard-Jones_potential).

### Instructions

2a. Take the new in.3dlj script, using a cutoff of 2.5 for the Lennard-Jones potential. UPDATE SCRIPT, QUESTION MARKS ON KEY PARAMETERS

(i) Fix the temperature to 1.0, and vary the particle density and interaction strength. Report snapshots and quantitative metrics (on structure and/or dynamics) for different phases of the system, including at least a liquid phase and a crystalline phase. Pro tip: equilibrate long enough, and stay far away from the phase boundaries unless you want to wait for a long time.

## Assignment 3 - Patch up

Not all colloidal particles have spherical, isotropic interactions! Directional interactions are often present as a result of internal chemical structure or functionalization. In this assignment, learn how directional interactions can be implemented by adding attractive patches on repulsive cores.

### Instructions 

3a. Explore the phase diagrams of patchy particle systems.

(i) Build at least two initial data files with different compositions of patchy particles, each particle having 2, 3, or 4 patches. To do so PIZZA.PY INSTRUCTIONS 

(ii) For each composition, use the LAMMPS SCRIPT file and vary thermodynamics conditions (temperature, packing fraction) to report at least two different phases. Justify your choice of composition, equilibration time, and quantitative metrics to define the structures. 

Pro tip: you can search the literature to guide your choices. Or just run random simulations and see what sticks, who are we to judge how you want to spend your time.

## Assignment 4 - Look Ma, no hands!

Equilibrium phase diagrams are fun, but colloids are very interesting non-Newtonian fluids! Let's check their rheology in this assignment. 

### Instructions

4a. Start from an equilibrated structure obtained with the in.3dlj script (see assignment 2) with ADD PARAMETERS: SIZE, ETA, T, EPSILON, ETC...

(i) Run the simulation shear.in CHECK NAME (FIX SHEAR RATE TO HIGHEST), and obtain the viscosity from the resulting stress curve by ADD INSTRUCTIONS. What is the algorithm used to stabilize the temperature in the system?

(ii) Repeat the simulation for smaller shear rates. Following the same procedure as before, make a plot of viscosity as a function of shear rate (in log-log scale). Can you fit a power law to it? Can you determine a lower limit for the zero shear viscosity? 

Pro tip: change shear rate logarithmically. Be mindful of the resources needed: anything lower than a shear rate of 0.001 will take at least several hours to run.

4b. (OPTIONAL, HARD) Calculate the zero shear viscosity. This can be done in a couple of ways [(or more, none easy)](https://docs.lammps.org/Howto_viscosity.html):

(i) Keep doing what you were doing in 4a, but MUUUCH slower. Arm yourself with patience, and good luck!

(ii) Use the Green-Kubo formalism to extract the viscosity from the ensemble average of the auto-correlation of the stress tensor. Good luck!


