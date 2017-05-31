% Juppie matlab zoals vroeger!

%% Test of 1/2n^2 formule werkt in python. Goed resultaat!
values = [5, 10, 1, 3, 1, 2, 4, 5, 5, 2, 6, 1, 5, 6, 1,8,1,2,6,8,2,2,2,13];

n = 0;
halfnquad = 0;
for value = values
    halfnquad = halfnquad + 0.5*value.^2
    n = n + value
end

%% plotting timing
clc
close all
clear all
cd('D:\Documents\studie_5_MoL_Prog_CN2\Heuristieken programmeertheorie\fruitvliegen\verslaglegging en presentaties')
load('testruns 2017-18-05.mat')

% x values
x = [5,6,7,8,9,10,15,20,25,30];
% calculate means
depth0av = nanmean(depth0);
depth1av = nanmean(depth1);
breadthav = nanmean(breadthfirst);
bestav = nanmean(bestfirst);
color2 = [0.5, 0.2, 0.0];

% Lines from averages
figure
semilogy(x(1:length(depth0av)), depth0av, 'color', color2, 'linewidth', 2)
hold on
semilogy(x(1:length(depth1av)), depth1av, 'r', 'linewidth', 2)
semilogy(x(1:length(breadthav)), breadthav, 'b', 'linewidth', 2)
semilogy(x(1:length(bestav)), bestav, 'g', 'linewidth', 2)

% Scatterthingies
semilogy(x(1:length(depth0av))-1/6, depth0', 'o', 'color', color2)
semilogy(x(1:length(depth1av)), depth1', 'or')
semilogy(x(1:length(breadthav))+1/6, breadthfirst', 'ob')
semilogy(x(1:length(bestav)), bestfirst', 'og')
xlim([5, 30])

% Text
title('time to first solution with different algorithms')
legend('depthfirst', 'depthfirst with archive', 'breadthfirst with archive',...
    'bestfirst')
xlabel('genome length')
ylabel('time (sec)')
yticks([0.0001, 0.01, 1, 100.00, 10000.0])
yticklabels({'0.0001', '0.01', '1', '100', '10000'})
