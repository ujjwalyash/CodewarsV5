import numpy as np
from teams.helper_function import Troops, Utils

def sigmoid_activate(layer): #Sigmoid function
    return 1/(1+np.exp(-layer))


def softmax_activate(layer): #Softmax function
    m = np.exp(layer)
    return m/np.sum(m)

class NeuralNetwork():
    def __init__(self):
        self._layers = []
        self._biases = []
        self._outputs = np.random.rand(4,10)

        input_size = 3
        neurons=10 #remove later

        #making layers
        self._layers.append(np.random.rand(neurons ,input_size)) #we initialize random values
        self._biases.append(np.random.rand(neurons, 1)) #we initialize random values.

        self._layers.append(np.random.rand(neurons ,neurons)) #we initialize random values
        self._biases.append(np.random.rand(neurons, 1)) #we initialize random values.

        self._layers.append(np.random.rand(neurons ,neurons)) #we initialize random values
        self._biases.append(np.random.rand(neurons, 1)) #we initialize random values.
    

    def forward(self, inputs):
        # inputs = inputs.reshape((-1,1))
        
        for layer, bias in zip(self._layers, self._biases): #we zip the biases to the layer
            inputs = np.matmul(layer,inputs)
            inputs = inputs+bias
            inputs = sigmoid_activate(inputs)
        
        output_layer = np.matmul(self._outputs, inputs)
        #Does not take into account the different size of the matrix.
        #We will fix it soon!
        
        return softmax_activate(output_layer)#Updated to softmax
        

    def mutate(self):
        pass


team_name = "Pratyaksh"
troops = [
    Troops.wizard, Troops.minion, Troops.archer, Troops.musketeer,
    Troops.dragon, Troops.skeleton, Troops.valkyrie, Troops.barbarian
]
deploy_list = Troops([])
team_signal = "h, Prince, Knight, Barbarian, Princess"

def deploy(arena_data: dict):
    """
    DON'T TEMPER DEPLOY FUNCTION
    """
    deploy_list.list_ = []
    logic(arena_data)
    return deploy_list.list_, team_signal

def logic(arena_data: dict):
    global team_signal

    my_tower = arena_data["MyTower"]
    my_troops = arena_data["MyTroops"]
    opp_tower = arena_data["OppTower"]
    opp_troops = arena_data["OppTroops"]

    #one hot encoding for deployable troops
    dep_troops = np.zeros(8,1)
    for i, troop in enumerate(troops):
        if troop in my_tower.deployable_troops:
            dep_troops[i] = 1
        else:
            dep_troops[i] = 0

    print(dep_troops)

    # input_NN=np.array([my_tower.total_elixir],
    #                   [my_tower.health],
    #                   [my_tower.deployable_troops[0]])