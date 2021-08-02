import random
from transformers import BertJapaneseTokenizer
from transformers import BertConfig
from transformers import BertForNextSentencePrediction
from tqdm import tqdm
import torch
from Agent import Agent


class User(Agent):
    def __init__(self, useContext, contextType, contextLength, canditates, modelType, model_path, isManual):
        super().__init__(useContext=useContext, contextType=contextType, contextLength=contextLength,
                         canditates=canditates, modelType=modelType, model_path=model_path, isManual=isManual)

    # response retrieval
    def selectResponse(self, input):
        response = self.calcuratedHighestResponse(input)
        return response

    # for reinforcement learning
    def calcurateReward(self):
        return 0

if __name__=="__main__":
    print("test")
    user = User()
