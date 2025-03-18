# from teams.helper_function import Troops, Utils

# team_name = "DELHI"
# troops = [Troops.dragon,Troops.skeleton,Troops.wizard,Troops.minion,Troops.archer,Troops.giant,Troops.balloon,Troops.barbarian]
# deploy_list = Troops([])
# team_signal = ""

# def deploy(arena_data:dict):
#     """
#     DON'T TEMPER DEPLOY FUCNTION
#     """
#     deploy_list.list_ = []
#     logic(arena_data)
#     return deploy_list.list_, team_signal

# def logic(arena_data:dict):
#     global team_signal
#     deploy_list.deploy_dragon((-16,0))

from teams.helper_function import Troops, Utils

team_name = "Priyam"
troops = [Troops.wizard,Troops.minion,Troops.archer,Troops.giant,Troops.dragon,Troops.skeleton,Troops.balloon,Troops.barbarian]
deploy_list = Troops([])
team_signal = ""

def deploy(arena_data:dict):
    """
    DON'T TEMPER DEPLOY FUCNTION
    """
    deploy_list.list_ = []
    logic(arena_data)
    return deploy_list.list_, team_signal

def logic(arena_data:dict):
    global team_signal
    deploy_list.list_.append((arena_data["MyTower"].deployable_troops[0],(-25,0)))
    deploy_list.list_.append((arena_data["MyTower"].deployable_troops[1],(25,0)))
    print("                       ")
    print("My troops", arena_data["MyTroops"])
    # print("Opp troops", arena_data["OppTroops"])
    print("                       ")