
import numpy as np

def sigmoid(z):
    """

    Returns the sigmoid function of the input.

    Parameters
    ----------
    z : float / int
        The value to act on.

    Returns
    -------
    sigma : float
        A value between 0 and 1 from the sigmoid curve.

    """

    return(1.0 / (1.0 + np.exp(-z)))



class Layer:
    """

    A single neuron layer, starting with random weights and biasses.

    """

    def __init__(self , Ninputs , Nneurons):
        """

        Initialises the Layer object.

        Parameters
        ----------
        Ninputs : int
            The number of inputs into the neuron layer (Also the number of neurons in the previous layer).
        Nneurons : int
            The number of neurons in the layer.

        Returns
        -------
        None.

        """
        if type(Ninputs) != int: # Checking the data type of Ninputs
            raise ValueError(f'Ninputs should be type int, it is currently type {type(Ninputs)}')
        if type(Nneurons) != int: # Checking the data type of Nneurons
            raise ValueError(f'Nneurons should be type int, it is currently type {type(Nneurons)}')

        self.Ninputs = Ninputs
        self.Nneurons = Nneurons
        self.weights = np.random.randn(Nneurons , Ninputs) # assigning random values to start with for both biasses and weights
        self.biasses = np.random.randn(Nneurons)


    def forward(self , x):
        """

        Takes a vector of inputs into the layer and returns a vector of the outputs.

        Parameters
        ----------
        x : list
            A vector of inputs for the current layer.

        Returns
        -------
        output : list
            A vector of the output of all neurons in the layer.

        """

        if np.shape(np.shape(x))[0] != 1: # Checking List dimensions
            raise ValueError(f'x array should be 1D. It is currently {np.shape(np.shape(x))[0]}D')
        if len(x) != self.Ninputs: # Checking that the input is the expected length for this layer
            raise ValueError(f'Vector x ({len(x)}) should have a length Ninputs ({self.Ninputs})')

        return(sigmoid(self.weights @ x + self.biasses))

    def __repr__(self):
        return(f"{self.Nneurons} neuron layer with {self.Ninputs} inputs")



class NeuralNetwork:
    """

    A neural network class

    """

    def __init__(self,sizes):
        """

        Initialises the NeuralNetwork object by filling it with Layer objects.

        Parameters
        ----------
        sizes : list
            A list of the numbers of neurons in each layer, starting with the input layer and finishing with the output layer.

        Returns
        -------
        None.

        """

        if np.shape(np.shape(sizes))[0] != 1: # Checking list dimensions
            raise ValueError(f'sizes array should be 1D. It is currently {np.shape(np.shape(sizes))[0]}D')

        self.sizes=sizes
        self.num_layers=len(sizes)-1
        self.layers=np.empty(0,dtype=Layer) # Create Layer list
        for i in range(1,len(sizes)):
            self.layers=np.append(self.layers,Layer(self.sizes[i-1],self.sizes[i]))


    def feedforward(self,values):
        """

        Takes a list of inputs and passes them through each layer of the neural network

        Parameters
        ----------
        values : list
            The initial inputs to be run through the neural network.

        Returns
        -------
        values : list
            The outputs of the neural network.

        """

        if np.shape(np.shape(values))[0] != 1: # Checking list dimensions
            raise ValueError(f'values array should be 1D. It is currently {np.shape(np.shape(values))[0]}D')
        if len(values) != self.layers[0].Ninputs: # Checking that the inputs will fit into the first layer of neurons
            raise ValueError(f'values list must be same size as the input layer {np.shape(values)[0]} != {self.layers[0].Ninputs}')

        for Layer in self.layers:
            values=Layer.forward(values)
        return values


    def evaluate(self,inputs,expected):
        """

        Runs inputs through the network and counts how many outputs match their expected values

        Parameters
        ----------
        inputs : 2D array
            An array made of a list of input vectors to be tested in the neural network.
        expected : 2D array
            An array made of a list of expected output vectors for each input vector.

        Returns
        -------
        correct : int
            A count of how many outputs matched the expected outputs

        """

        if np.shape(np.shape(inputs))[0] != 2: # Checking the dimensions of the inputs array
            raise ValueError(f'inputs array should be 2D. It is currently {np.shape(np.shape(inputs))[0]}D')
        elif np.shape(np.shape(expected))[0] != 2: # Checking the dimensions of the expected array
            raise ValueError(f'expected array should be 2D. It is currently {np.shape(np.shape(expected))[0]}D')

        elif np.shape(inputs)[1] != self.layers[0].Ninputs: # Checking that the inputs will fit into the first layer of neurons
            raise ValueError(f'axis 1 of inputs array must be same size as the input layer {np.shape(inputs)[1]} != {self.layers[0].Ninputs}')
        elif np.shape(expected)[1] != self.layers[-1].Nneurons: # Checking that the shape of the expected values corresponds to the last layer of neurons
            raise ValueError(f'axis 1 of expected array must be same size as the input layer {np.shape(expected)[1]} != {self.layers[0].Nneurons}')

        elif np.shape(inputs)[0] != np.shape(expected)[0]: # Checking that the inputs and expected arrays match in length, so they can represent one another
            raise ValueError(f'axis 0 of expected array must be same size as axis 0 of inputs array {np.shape(inputs)[0]} != {np.shape(expected)[0]}')

        correct=0
        for a,b in zip(inputs,expected):
            if np.argmax(self.feedforward(a)) == np.argmax(b): # Check if the most activated output neuron is the same as expected
                correct+=1
        return(correct)

    def backprop(self,x,y):
        """
        
        Finds the gradient of the cost function relative to bias and weight

        Parameters
        ----------
        x : list
            A list of input values for the neural network.
        y : list
            A list of expected outputs from the neural network.

        Returns
        -------
        nabla_b : 2D array
            A list of vectors for the gradient of the cost function with respect to the bias for each layer.
        nabla_w : 3D array
            A list of 2D arrays representing the gradient of the cost function with respect to the weight for each layer.

        """

        if np.shape(np.shape(x))[0] != 1: # Checking list dimensions
            raise ValueError(f'x array should be 1D. It is currently {np.shape(np.shape(x))[0]}D')
        if np.shape(np.shape(y))[0] != 1: # Checking list dimensions
            raise ValueError(f'y array should be 1D. It is currently {np.shape(np.shape(y))[0]}D')
            
        if len(x) != self.layers[0].Ninputs: # Checking that the inputs will fit into the first layer of neurons
            raise ValueError(f'axis 1 of x array must be same size as the input layer {len(x)} != {self.layers[0].Ninputs}')
        elif len(y) != self.layers[-1].Nneurons: # Checking that the shape of the expected values corresponds to the last layer of neurons
            raise ValueError(f'axis 1 of y array must be same size as the input layer {len(y)} != {self.layers[-1].Nneurons}')

        nabla_b=[] # Initiate arrays
        nabla_w=[]
        for layer in self.layers:
            nabla_b.append(np.zeros(layer.biasses.shape)) # Fill empty arrays with correct shape of zeros
            nabla_w.append(np.zeros(layer.weights.shape))
        z_s=[] # Initiate z vector list
        a_s=[x] # Initiate activation vector list, with the inputs as the first entry
        activation = x
        for layer in self.layers: # Move through each layer, calculating and saving z and activation vectors
            z=layer.weights @ activation + layer.biasses
            z_s.append(z)
            activation=sigmoid(z)
            a_s.append(activation)
        err_final=(a_s[-1]-y)*sigmoid(z_s[-1])*(1-sigmoid(z_s[-1])) # Calculate the error on the output

        nabla_b[-1]=err_final # save the final error vector in the final slot on nabla_b
        err_int=err_final
        for i in reversed (range (len(nabla_b)-1)): # Propagate backwards, calculating and saving the error vector in the corresponding nabla_b slots
            err_int = (np.transpose(self.layers[i+1].weights)) @ err_int * sigmoid(z_s[i]) * (1-sigmoid(z_s[i]))
            nabla_b[i] = (err_int)

        for l in range(len(nabla_w)):
            for j in range(np.shape(nabla_w[l])[0]):
                for k in range(np.shape(nabla_w[l])[1]): # For each index in nabla_w, calculate.
                    nabla_w[l][j][k] = nabla_b[l][j] * a_s[l][k]
        return(nabla_b,nabla_w)

    def SGD(self,Xtrain,ytrain,Xtest,ytest,epochs=10,eta=0.1):
        """

        Trains the neural network using stochastic gradient descent and tests and outputs the accuracy of the network every loop.

        Parameters
        ----------
        Xtrain : 2D array
            An array of training data inputs of shape (n_samples,n_features).
        ytrain : 2D array
            An array of training data expected outputs of shape (n_samples,n_classes).
        Xtest : 2D array
            An array of testing data inputs of shape (n_samples,n_features).
        ytest : 2D array
            An array of testing data expected outputs of shape (n_samples,n_classes).
        epochs : int, optional
            The number of times that the network is trained by the training arrays. The default is 10.
        eta : float, optional
            The size of the step down the gradient taken each time it is updated. The default is 0.1.

        Returns
        -------
        percentagelist : list
            A list of the percentage accuracy scores for each loop.

        """

        for arg in (Xtrain,ytrain,Xtest,ytest):
            if np.shape(np.shape(arg))[0] != 2:  # Checking the dimensions of all the arrays
                raise ValueError(f'{arg} array should be 2D. It is currently {np.shape(np.shape(arg))[0]}D')

        if type(epochs) != int: # Checking the data type of epochs
            raise ValueError(f'epochs should be type int, it is currently type {type(epochs)}')
        try:                    # Checking the data type of eta
            float(eta)          # First trying to float it (in case it is an integer)
        except(ValueError):
            raise ValueError(f'eta should be type float, it is currently type {type(eta)}')
        
        percentagelist=[]
        for repeat in range(epochs): # Looping through repeats
            for i in range(len(Xtrain)): # Looping through the length of input data
                nabla_b,nabla_w = self.backprop(Xtrain[i],ytrain[i]) # Calculate nabla_b and nabla_w for this loop

                for l in range(len(nabla_b)): # Looping through layers, alter the weights and biasses with scale eta
                    self.layers[l].weights=self.layers[l].weights-eta*nabla_w[l]
                    self.layers[l].biasses=self.layers[l].biasses-eta*nabla_b[l]
            percentage=100*self.evaluate(Xtest,ytest)/len(ytest) # test with testing data and print percentage correct
            percentagelist.append(percentage) # also save percentage correct
            print(f'Percentage correct for loop {repeat+1}: {percentage:.2f}%')
        return(percentagelist)

    def __repr__(self):
        return(f"Neural network object with {self.num_layers} layers after the input")

 
