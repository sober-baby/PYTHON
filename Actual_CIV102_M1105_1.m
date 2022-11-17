clear; close all;
L = 1200; % Length of the bridge 
n = 1200; % Number of subsections
P = 400; % Total weight of the train
x = linspace(0, L, n + 1); % All the x-position 

% The variables sfd and bmd hold a matrix of the SFD and BMD at the three
% positions: Far left, middle, and far right as a martrix with 3 rows
%
% Far Left --> sfd @ 1mm, sfd @ 2mm, ...
% Middle   -->  ~     ~ , ~      ~ , ...
% Far right-->  ~     ~ , ~      ~ , ...
%
% And repeat for the BMD
[sfd, bmd] = get_initial_forces(n, P, x);

% Opens a new figure
figure(1);
% Divides the figure into a matrix with 2 rows and 1 column, then puts this
% figure (SFD) into position 1 (top)
subplot(2, 1, 1); 
% Forces plots onto the same graph
hold on
% Plots the sfd against the "x" values (when plotting a matrix, plots an
% individual line per row (3 SFD's in all)
plot(x, sfd, "-b"); % Blue solid lines
% Plots the 
plot([0 1200], [0 0], "-k", LineWidth=2)
title("SFD for trains at beginning, middle, and end")
xlabel("Distance Along Bridge (mm)")
ylabel("Shear Force (N)")
legend("Shear Force")
hold off

subplot(2, 1, 2);
plot([0 1200], [0 0], "-b", LineWidth=2)
plot(x, bmd, "-k");
title("BMD for trains at beginning, middle, and end")
xlabel("Distance Along Bridge (mm)")
ylabel("Bending Moment (N mm)")
legend("Bending Moment")
axis ij;

param = [0];

function [sfd, bmd] = get_initial_forces(n, P, x)
init_train_pos = [52 228 392 568 732 908];
load = P/6;
sfd = zeros(3, n + 1);
bmd = zeros(3, n + 1);
for i=1:3
    % i = 1 --> far left
    % i = 2 --> middle 
    % i = e --> far right
    train_pos = init_train_pos + (i - 1) * 120;
    sfd(i, :) = getSFD(train_pos, load, n, x);
    bmd(i, :) = getBMD(sfd(i, :), n, x);
end

end

function sfd_y = getSFD(train_pos, weight_per_wheel, n, x)
reactionForces = getReactionForces(train_pos, weight_per_wheel);

sfd_y = zeros(1, n + 1);
sfd_y(1) = reactionForces(1);

for i = 1:n+1
    sfd_y(i) = sfd_y(1) - sum(train_pos <= x(i)) * weight_per_wheel;
end

end

function reactionForces = getReactionForces(train_pos, weight_per_wheel)
moment_sum = 0;
for i = 1:length(train_pos)
    moment_sum = moment_sum + train_pos(i) * weight_per_wheel;
end
reactionForces = 0;
reactionForces(2) = moment_sum / 1200;
reactionForces(1) = length(train_pos) * weight_per_wheel - reactionForces(2);

end

function bmd_y = getBMD(sfd_y, n, x)

bmd_y = zeros(1, n + 1);
dx = x(2) - x(1);

for i = 2:n+1
    bmd_y(i) = bmd_y(i-1) + sfd_y(i)*dx;

end
end
