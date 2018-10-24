%{
    Name: Ruben Vazquez
    UFID: 2143-1351
    Title: Kernel Least Mean Squares Algorithm
    Description: An implementation of a kernel least mean squares filter
    Hyper-parameters:
        1. learning step
        2. kernel width
%}

%{
    Pre-conditions:
        train_data: MxN matrix, rows are observations, columns are measured
        features
        test_data: TxN matrix, rows are observations, columns are measured
        features
        train_desired: Mx1 matrix, rows are observations, columns are
        desired outputs
        test_desired: Tx1 matrix, rows are observations, columns are
        desired outputs
        learning_step: scalar
        kernel_width: scalar
%}

% Enable debug messages
DEBUG = 2;

mu = 0;
sigma = 1;
num_data_points = 3229;
num_test_points = 400;
filter_size = 5;
use_real_data = 1;

% Test the KLMS algorithm for correctness.
if (DEBUG > 0)
    
    [train_data, train_desired, test_data, test_desired] = generate_data(mu,sigma,num_data_points,num_test_points,filter_size,use_real_data,DEBUG);
    %[test_data, test_desired] = generate_data(mu,sigma,num_test_points,filter_size,DEBUG);
    
    learning_step = 0.04;
    kernel_width = (1/50000);
    
    [centers, coefficients] = initialization(DEBUG);
    [centers, coefficients] = train(train_data, train_desired, learning_step, kernel_width, centers, coefficients, DEBUG);
    error = test(test_data, test_desired, kernel_width, centers, coefficients, DEBUG);
end

% Generate or import the data used to train the KLMS algorithm
function [x,t,z,d] = generate_data(mu, sigma, num_data_points, num_test_points, filter_size, use_real_data, DEBUG)

if (DEBUG > 1)
    disp('Generate new data from normal distribution...')
end

% Predict (D+1) values into the future
D = 0;

% Generate data from a normal distribution
if (use_real_data == 0)
    data = normrnd(mu,sigma,num_data_points,1);
    y = [data ; zeros(1,1)];
    t = -0.8*y(1:num_data_points) + 0.7*y(2:num_data_points+1);
    q = t + 0.25*t.^2 + 0.11*t.^3;
    
    x_temp = q;
    
% Import the monthly sunspot data
else
    a = importdata('SN_m_tot_V2.0.csv');
    x_temp = a(:,4);
end

% Temp structures that hold the training and testing data
train_temp = x_temp(1:num_data_points-num_test_points);
test_temp = x_temp(num_data_points-num_test_points+1:end);

% Initialize structures to hold the training and testing data in the
% proper format for the algorithm implementation
x = zeros(size(train_temp,1)-(filter_size-1)-(D+1),filter_size);
t = zeros(size(train_temp,1)-(filter_size-1)-(D+1),1);

z = zeros(size(test_temp,1)-(filter_size-1)-(D+1),filter_size);
d = zeros(size(test_temp,1)-(filter_size-1)-(D+1),1);

% Store the training and testing data into the structures
for i=1:size(train_temp,1)-(filter_size+D)
    x(i,:) = train_temp(i:i+(filter_size-1));
    t(i,:) = train_temp(i+filter_size+D);
end

for i=1:size(test_temp,1)-(filter_size+D)
    z(i,:) = test_temp(i:i+(filter_size-1));
    d(i,:) = test_temp(i+filter_size+D);
end

end

% Function to initialize the required data structures for the KLMS
% algorithm
function [c,h] = initialization(DEBUG)

if (DEBUG > 1)
    disp('Initializing parameter structures...')
end

% Create empty structures
c = [];
h = [];

end

% Function to the determine the centers and coefficients of the KLMS
% algorithm
function [c,h] = train(train_data, train_desired, learning_step, kernel_width, centers, coefficients, DEBUG)

if (DEBUG > 1)
    disp('Determinining centers and coefficients...')
end

% Initialize the centers and the coefficients
centers = [centers ; train_data(1,:)];
coefficients = [coefficients ; learning_step*train_desired(1,:)];

% Determine the rest of the centers and the coefficients.
for i=2:size(train_data,1)
    
    f = sum(coefficients.*kernel(centers,train_data(i,:),kernel_width));
    e = train_desired(i,:) - f;
    
    centers = [centers ; train_data(i,:)];
    coefficients = [coefficients ; learning_step*e];
    
end

c = centers;
h = coefficients;

end

% Function that tests the performance of the KLMS algorithm with the
% determined centers and coefficients.
function test_error = test(test_data, test_desired, kernel_width, centers, coefficients, DEBUG)

if (DEBUG > 1)
    disp('Getting error...')
end

% Inatialize structure to hold the predicted outputs
f = zeros(size(test_data,1),1);

% Calculate the predicted outputs.
for i=1:size(test_data,1)
    
    f(i,:) = sum(coefficients.*kernel(centers,test_data(i,:),kernel_width));
    %e(i,:) = test_desired(i,:) - f;
    
end

% Calculate the mean of the predicted and determined outputs.
f_mean = mean(f);
test_desired_mean = mean(test_desired);

% Calculate the normalized mean-squared error of the test data.
%test_error = immse(f,test_desired);
test_error = ((f-test_desired)'*(f-test_desired)/size(test_data,1))/(f_mean*test_desired_mean);
%test_error = f;

% Plot the predicted output against the desired output.
if (DEBUG > 1)
    figure
    plot(test_desired)
    hold on
    plot(f)
end

end

% Auxillary kernel function used in the KLMS algorithm
function k = kernel(centers,data_point,kernel_width)

k = exp(-((vecnorm((centers-data_point),2,2).^2)*(kernel_width)));

end