from utils.loadSetting import loadSetting
from utils.loadCanditates import loadCanditates
from components.System import System
from components.User import User
from components.Dialogue import Dialogue


def main():
    setting = loadSetting()

    # general setting
    dialogueTurn = setting["General"]["dialogue_turn"]
    startToken = setting["General"]["start_token"]
    endToken = setting["General"]["end_token"]
    whoStart = setting["General"]["who_start"]
    
    # user's setting
    userUseContext = setting["User"]["use_context"]
    userContextType = setting["User"]["context_type"]
    userContextLength = setting["User"]["context_length"]
    userModelType = setting["User"]["model_type"]
    userModelPath = setting["User"]["model_path"]
    userIsManual = setting["User"]["isManual"]

    # system's setting
    systemUseContext = setting["System"]["use_context"]
    systemContextType = setting["System"]["context_type"]
    systemContextLength = setting["System"]["context_length"]
    systemModelType = setting["System"]["model_type"]
    systemModelPath = setting["System"]["model_path"]
    systemAction = setting["System"]["action_list"]
    systemIsManual = setting["User"]["isManual"]

    userCanditates, systemCanditates=[], []
    # load data
    if systemModelType=="response_selection":
        userCanditates, systemCanditates = loadCanditates(setting["General"]["canditates_data_path"])

    user = User(useContext=userUseContext, contextType=userContextType, contextLength=userContextLength,
                canditates=userCanditates, modelType=userModelType, model_path=userModelPath, isManual=userIsManual)
    system = System(useContext=systemUseContext, contextType=systemContextType, contextLength=systemContextLength,
                    canditates=systemCanditates, modelType=systemModelType, model_path=systemModelPath, action_list=systemAction, isManual=systemIsManual)
    dialogue_environment = Dialogue(
        user=user, system=system, dialogue_turn=dialogueTurn, start_token=startToken, end_token=endToken, whoStart=whoStart)

    # play
    dialogue_environment.playDialogue()

if __name__ == "__main__":
    main()
