# Heuristics: Fruitvliegen

> Nina Cialdella<br>
> Leander de Kraker<br>
> 2017-6-1<br>

Python code files.<br>
Code that can be called and used by the user:

- bestfirstsearch.py: runs a bestfirst search for any genome you want, normally the official genome.
- flipsorter.py: Runs the flipsorter algorithm on any genome you want, normally the official genome.
- bestfirsRunneR.py: Specify your search parameters in the code and run bestfirstsearches and flipsorters as you want on random genomes. Gives a lot of output, some of which is also Matlab compatible for further analysis after following the steps specified in 'analyse_100runs.m'.

Code with helper functions:

- cost.py: Costfunctions to sort the bestfirst search priority queue.
- helperFunctions.py: Many necessary functions for the bestfirstsearch and depthfirstsearch
- plotters.py: Creates nice plots of the found paths between 2 genomes.
- mutations.py: creates an object which specifies what mutations can be done on a genome.
