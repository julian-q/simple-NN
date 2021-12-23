s = 'relu'

match s:
    case 'relu':
        activation_derivative = relu_derivative
    case 'sigmoid':
        activation_derivative = sigmoid_derivative
    case _:
        raise Exception('Activation function not supported:', s)