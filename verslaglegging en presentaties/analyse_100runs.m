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
% 2: search -> find   true   change to   true   
% 3: search -> find   false  change to   false
% 4: for mutationTracker1 & 2, change outer brackets [ ] to { } quirly
% brackets, because the mutationtracker vectors have different lengths

%% The data
clc
clear all
close all
load('100runsOUTPUT.mat')

%% Analysis code
clc
nruns = length(levels);
fprintf('number of runs done = %d\n', nruns)

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
    if levels(i) <= fliplevels(i)
        better = better + 1;
    else
        omg(end + 1) = i;
        fprintf('omg flipsorter level is better than bestfirst in run %d\n', i)
        fprintf('level bestfirst:  %d\n', levels(i))
        fprintf('level flipsorter: %d\n', fliplevels(i))
    end
end
better = better/nruns;
if better == 1
    fprintf('\nthe bestfirst always found a shorter solution than flipsorter!\n')
end

%% New cost measures to see what makes a genome difficult

difficulty = zeros(1, nruns);
method = 'positiondist'; % 'positiondist'
for i = 1:nruns
    genome = [0, genomes(i, :), (length(genomes(i,:))+1)]; % Add padding
    if strcmp(method, 'positiondist')
        % Dificulty by how far away each gene is from its desired position 
        % The desired position = j
        for j = 1:length(genome)
            difi = abs(genome(j) - j);
            difficulty(i) = difficulty(i) + difi;
            % fprintf('%f', difficulty(i))
        end
    elseif strcmp(method, 'correct')
        % Difficulty by how many genes still need to be swapped certainly
        for j = 1:length(genome)-1
            if abs(genome(j) - genome(j+1)) == 1 % adjecent to where it will need to be adjecent to
                difficulty(i) = difficulty(i) + 0;
            else
                difficulty(i) = difficulty(i) + 1;
            end
        end
    end
end

%% Fit startcost to depth level
clc
fit = fitlm(difficulty, levels,'linear');
fit.Rsquared.Ordinary

%% Figures!
close all
% Relation between best solution level and starting cost
figure
randX = (rand(1, nruns) - 0.5)/5;
randY = (rand(1, nruns) - 0.5)/5;
% randX = 0;
% randY = 0;
plot(costs+rand(1,1)+randX, levels+randY, 'o')
xlabel('begin costs')
ylabel('solution found at level')
title('relation between beginning cost and solution depth level')


figure
randX = (rand(1, nruns) - 0.5)/2;
randY = (rand(1, nruns) - 0.5)/2;
% randX = 0;
% randY = 0;
plot(difficulty+randX, levels+randY, 'or')
xlabel('begin costs')
ylabel('solution found at level')
title('relation between beginning cost and solution depth level')
%% 
figure
randX = (rand(1, nruns) - 0.5)/3;
randY = (rand(1, nruns) - 0.5)/3;
% randX = 0;
% randY = 0;
plot(difficulty+randX, mutsums+randY, 'og')
xlabel('starting cost')
ylabel('n')
title('relation between beginning cost and mutation points')

%% 
figure
randX = (rand(1, nruns) - 0.5)/3;
randY = (rand(1, nruns) - 0.5)/3;
plot(difficulty+randX, mutsums2+randY, 'ob')
xlabel('starting cost')
ylabel('1/2 n ^2')
title('relation between beginning cost and 1/2n^2 mutation points')



%% Bargraph flipsorter vs bestfirst
figure
hold on
color = winter(5);
bar([1,2],[aver.levels; aver.fliplevels], 'facecolor', color(3,:))
errorbar([1,2],[aver.levels; aver.fliplevels],[STD.levels; STD.fliplevels],'.k','linewidth',2)
xticks([1,2])
xlim([0.5,2.5])
xticklabels({'bestfirst', 'flipsort'})
title('flipsorter vs bestfirst')
ylabel('depth level solution')