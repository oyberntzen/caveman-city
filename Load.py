import Stat



def load():
    for Monster in Stat.MonsterImp:
        monster = Monster.Main()
        Stat.MonsterGroup.add(monster)
        Stat.MonserList.append(monster)