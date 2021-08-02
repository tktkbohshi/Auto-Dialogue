from User import User
from System import System

class Dialogue():
    def __init__(self, user=User, system=System, dialogue_turn=10, start_token="", end_token="", whoStart="system"):
        self.user = user
        self.system = system
        self.dialogue_turn = dialogue_turn
        self.start_token = start_token
        self.end_token = end_token
        self.whoStart = whoStart

    def playDialogue(self):
        if self.whoStart == "system":
            first_speaker = self.system
            first_speaker_label = "system"
            second_speaker = self.user
            second_speaker_label = "user"
        elif self.whoStart == "user":
            first_speaker = self.user
            first_speaker_label = "user"
            second_speaker = self.system
            second_speaker_label = "system"

        # play dialogue
        print("Start talking!")
        
        prev_turn_utterance = self.start_token
        for turn_num in range(self.dialogue_turn):
            if turn_num == self.dialogue_turn-1:
                prev_turn_utterance += self.end_token

            # first speaker
            response_first = ""
            if first_speaker_label=="system":
                response_first = first_speaker.returnResponse(prev_turn_utterance)
            else:
                response_first = first_speaker.returnResponse(prev_turn_utterance)
                reward = second_speaker.calcurateReward()
            print("{}: {}".format(first_speaker_label, response_first))

            # second speaker
            response_second = ""
            if second_speaker_label == "system":
                response_second = second_speaker.returnResponse(response_first)
            else:
                response_second = second_speaker.returnResponse(response_first)
                reward = second_speaker.calcurateReward()
            print("{}: {}".format(second_speaker_label, response_second))

            # save current response for the next turn
            prev_turn_utterance = response_second

        print("Finish!")
