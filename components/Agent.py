from collections import deque
from transformers import BertJapaneseTokenizer
from transformers import BertConfig
from transformers import BertForNextSentencePrediction
from tqdm import tqdm
import torch


class Agent():
    def __init__(self, useContext=False, contextType="turn", contextLength=1, canditates=[], modelType="response_selection", model_path="", isManual=False):
        self.useContext = useContext
        self.contextType = contextType
        self.contextLength = contextLength

        if contextType == "turn":
            self.context = deque([], 2*self.contextLength+1)
        elif contextType == "token":
            self.context = deque([], self.contextLength)

        self.modelType = modelType
        # only use canditates if modelType is response_selection
        if self.modelType=="response_selection":
            self.canditates = canditates

        self.isManual = isManual

        # for Transformers
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(model_path)
        self.config = BertConfig.from_pretrained(model_path)
        self.model = BertForNextSentencePrediction.from_pretrained(model_path)
        self.device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
        self.model.to(self.device)
        self.isManual = isManual

    def returnResponse(self, input):
        response = ""
        # manual mode
        if self.isManual:
            print("input--")
            response = input()
            return response

        # update context
        if self.useContext:
            self.context.append(input)
            # concat context
            input = "[SEP]".join(map(str, self.context))

        # get response
        if self.modelType == "response_selection":
            response = self.selectResponse(input)
        elif self.modelType == "generative":
            response = self.generateResponse(input)

        # update context
        if self.useContext:
            self.context.append(response)

        return response

    # response retrieval
    def selectResponse(self):
        return "work in progress"

    def calcuratedHighestResponse(self, input):
        # calcurate the score at the each canditate.
        pred_list = []
        for canditate in tqdm(self.canditates):
            next_sentence = canditate
            encoding = self.tokenizer(
                input, next_sentence, return_tensors='pt')
            encoding.to(self.device)
            # prediction
            outputs = self.model(
                **encoding, labels=torch.LongTensor([1]).to(self.device))
            softmax = torch.nn.Softmax(dim=1)
            prediction = softmax(outputs.logits)
            pred_list.append([prediction[0, 0].item(), canditate])

        # select the best response
        pred_list = sorted(pred_list, reverse=True, key=lambda x: float(x[0]))
        response = pred_list[0][1]

        return response

    # generate respnose
    def generateResponse(self, input):
        # output: response
        return "work in progress"

    # editing prototype
    def editingPrototype(self):
        return "work in progress"
