% Analyse output from 100 runs of the bestfirst and flipsorter algorithm
% For Fruitvliegen!
%
% Leander de Kraker
% 2017-5-31
%  
% When copying the output it still causes crashes and is difficult to
% analyse. To fix, execute these steps:
%
% 1: search -> find   ],  change to     ];    this changes everything to
% nice matrices instead of very long 1D vectors with no limits between runs
% 2: search -> find   True   change to   true   
% 3: search -> find   False  change to   false
% 4: for mutationTracker1 & 2, change outer brackets [ ] to { } quirly
% brackets, because the mutationtracker vectors have different lengths

clc
clear all
close all
%% The data
levels = [2, 3, 4, 5];
fliplevels = [516, 151, 12, 39];
mutsums = [13, 2];
mutsums2 = [159, 92];
solat = [1,2,3,4,5,6];
costs = [22, 23, 25, 20];
runtimes = [0, 0,0,0,0];
sames = [true, true, true, true, false];

%% Analysis code

nruns = length(levels);
fprintf('number of runs done = %d', nruns)

% Taking the average of all values that need averaging
aver.levels = mean(levels);
aver.fliplevels = mean(fliplevels);
aver.mutsums = mean(mutsums);
aver.mutsums2 = mean(mutsums2);
aver.solat = mean(solat);
aver.costs = mean(costs);
aver.runtimes = mean(runtimes);
aver.sames = mean(sames);

% Taking Standard Deviations from all variables that need SDing
STD.levels = std(levels);
STD.fliplevels = std(fliplevels);
STD.mutsums = std(mutsums);
STD.mutsums2 = std(mutsums2);
STD.solat = std(solat);
STD.costs = std(costs);
STD.runtimes = std(runtimes);
STD.sames = std(sames);

% Checking if bestfirst search always found a shorter path than flipsort
better = 0;
omg = [];
for i = 1:nruns
    if levels(i) < fliplevels(i)
        better = better + 1;
    else
        omg(end + 1) = i;
        fprintf('\nomg flipsorter level is better than bestfirst in run %d', i)
    end
end
better = better/nruns;
if better == 1
    fprintf('\nthe bestfirst always found a shorter solution than flipsorter!\n')
end

%% Figures!
% Relation between best solution level and starting cost
figure
randX = (rand(1, nruns) - 0.5)/2;
randY = (rand(1, nruns) - 0.5)/2;
randX = 0;
randY = 0;
plot(costs+rand(1,1)+randX, levels+randY, 'o')
xlabel('begin costs')
ylabel('solution found at level')
title('relation between beginning cost and solution depth level')



aver
STD