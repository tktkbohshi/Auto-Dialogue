import random
from transformers import BertJapaneseTokenizer
from transformers import BertConfig
from transformers import BertForNextSentencePrediction
from tqdm import tqdm
import torch
from Agent import Agent


class System(Agent):
    def __init__(self, useContext, contextType, contextLength, canditates, modelType, model_path, isManual, action_list):
        super().__init__(useContext=useContext, contextType=contextType, contextLength=contextLength,
                         canditates=canditates, modelType=modelType, model_path=model_path, isManual=isManual)
        self.action_list = action_list
        self.reward = 0

    # response retrieval
    def selectResponse(self, input, action=""):
        # concatnate action
        input += action
        response = self.calcuratedHighestResponse(input)

        return response

    # for reinforcement learning
    def policy(self):
        # randomly choose
        action = random.randomint(0, len(self.action_list))
        return self.action_list[action]

if __name__ == "__main__":
    print("test")
    system = System()
