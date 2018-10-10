%{
    Name: Ruben Vazquez
    UFID: 2143-1351
    Title: Artificial Neural Network Algorithm
    Description: An implementation of an artifical neural network
    Hyper-parameters:
        1. Learning rate (scalar)
        2. Size of network (vector)
%}

%{
    Pre-conditions:
        train_data: MxN matrix, rows are observations, columns are measured
        features
        test_data: TxN matrix, rows are observations, columns are measured
        features
        train_desired: MxP matrix, rows are observations, columns are
        desired outputs
        test_desired: TxP matrix, rows are observations, columns are
        desired outputs
        learning_rate: scalar
        network_size: Qx1 vector, rows are size of q-th hidden layer
%}

% Enable debug messages
DEBUG = 0;

% DEBUG values that meet the aforementioned pre-conditions.
% train_data = importdata('EEMBC/dcache/fv4000000.csv');
% train_desired = importdata('EEMBC/dcache/d.dat');

% Test the ANN algorithm for correctness.
if (DEBUG > 0)
    train_data = [0 0; 0 1; 1 0; 1 1];
    train_desired =[0 0 0 1; 0 0 1 0; 0 1 0 0; 1 0 0 0];
    network_size = [3];
    learning_rate = 0.02;
    
    weights = initialization(train_data, train_desired, network_size, DEBUG);
    weights = train(train_data, train_desired, learning_rate, weights, DEBUG);
    error = test(train_data, train_desired, weights, DEBUG);
end

%{
    Post-conditions:
        weights: 1x(Q+1) cell vector. Each cell is a RxS matrix, with R
        inputs and S processing elements, representing the set of layer weights.
%}
function weights = initialization(train_data, train_desired, network_size, DEBUG)

if (DEBUG > 1)
    disp('Initializing weights...')
end

for i=1:size(network_size,1)
    
    if (i == 1)
        weights{i} = rand(size(train_data,2)+1,network_size(i));
    else
        weights{i} = rand(network_size(i-1)+1,network_size(i));
    end
    
end

weights{i+1} = rand(network_size(i)+1,size(train_desired,2));

end

%{
    Post-conditions:
        weights: 1x(Q+1) cell vector with updated weights from training
%}
function trained_weights = train(train_data, train_desired, learning_rate, weights, DEBUG)

if (DEBUG > 1)
    disp('Training weights...')
end

y{1} = train_data;

for j=1:10000
        
        % Forward computations
        % Calculate all of the layer inputs and layer outputs
        for i=1:size(weights,2)

            v{i} = [ones(size(y{i},1),1) y{i}]*weights{i};
            if (i < size(weights,2))
                y{i+1} = sigmoid(v{i}, false);
            else
                y{i+1} = identity(v{i}, false);
            end

        end

        % Error computations
        e = y{i+1} - train_desired;
        sum_e = sum(e,2);
        sum_e2 = sum((e.*e),2);
        
        if (DEBUG > 1)
            disp(sum(sum_e2))
            disp(y{i+1})
        end

        %Backward computations
        for i=size(weights,2):-1:1
            if (i < size(weights,2))
                delta{i} = e.*sigmoid(v{i},true);
            else
                delta{i} = e.*identity(v{i},true);
            end

            e = delta{i}*weights{i}(2:end,:)';

        end

        % Update weights
        for i=1:size(weights,2)
            
            change = -learning_rate*([ones(size(y{i},1),1) y{i}]'*delta{i});
            weights{i} = weights{i} + change;

        end

end

trained_weights = weights;

end

%{
    Post-conditions:
        test_error: a scalar
%}
function test_error = test(test_data, test_desired, weights, DEBUG)

if (DEBUG > 1)
    disp('Getting error...')
end

y{1} = test_data;

% Forward computations
for i=1:size(weights,2)

    v{i} = [ones(size(y{i},1),1) y{i}]*weights{i};
    if (i < size(weights,2))
        y{i+1} = sigmoid(v{i}, false);
    else
        y{i+1} = identity(v{i}, false);
    end

end

% Error computations
e = y{i+1} - test_desired;
sum_e = sum(e,2);
sum_e2 = sum((e.*e),2);

if (DEBUG > 1)
    disp(sum(sum_e2))
    disp(y{i+1})
end

test_error = (1/2)*sum(sum_e2);

end

% Sigmoid activation function.
function sig = sigmoid(x, deriv)

if (deriv)
    
    temp = sigmoid(x, false);
    sig = temp.*(1 - temp);
    
else
    
    sig = 1./(1 + exp(-x));
    
end

end

% Identity activation function.
function iden = identity(x, deriv)

if (deriv)
    
    iden = 1;
    
else
    
    iden = x;
    
end

end