from helper import *

def get_path(curr_pos, tar_pos):
    delta = curr_pos - tar_pos
    if delta.x < 0:
        return Point(1, 0)
    elif delta.x > 0:
        return Point(-1, 0)
    elif delta.y < 0:
        return Point(0, 1)
    else:
        return Point(0, -1)


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        curr_pos = self.PlayerInfo.Position
        house_loc = self.PlayerInfo.HouseLocation

        # Create map array
        map_info = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        map_weight = []
        for y in range(gameMap.yMin, gameMap.yMax):
            map_weight.append([])
            for x in range(gameMap.xMin, gameMap.xMax):
                tile_type = gameMap.getTileAt(Point(x, y)).value

                map_info[tile_type].append(Point(x, y))

        print("CollectingSpeed:", self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed),
              "\nCarryingCapacity:",self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity))

        if curr_pos == house_loc and self.PlayerInfo.TotalResources >= 10000:
            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed) < 1:
                return create_upgrade_action(UpgradeType.CollectingSpeed)

            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) < 1:
                return create_upgrade_action(UpgradeType.CarryingCapacity)

        if curr_pos == house_loc and self.PlayerInfo.TotalResources >= 15000:
            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed) < 2:
                return create_upgrade_action(UpgradeType.CollectingSpeed)

            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) < 2:
                return create_upgrade_action(UpgradeType.CarryingCapacity)

        if curr_pos == house_loc and self.PlayerInfo.TotalResources >= 25000:
            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed) < 3:
                return create_upgrade_action(UpgradeType.CollectingSpeed)

            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) < 3:
                return create_upgrade_action(UpgradeType.CarryingCapacity)

        if curr_pos == house_loc and self.PlayerInfo.TotalResources >= 50000:
            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed) < 4:
                return create_upgrade_action(UpgradeType.CollectingSpeed)

            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) < 4:
                return create_upgrade_action(UpgradeType.CarryingCapacity)

        if curr_pos == house_loc and self.PlayerInfo.TotalResources >= 100000:
            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed) < 5:
                return create_upgrade_action(UpgradeType.CollectingSpeed)

            if self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) < 5:
                return create_upgrade_action(UpgradeType.CarryingCapacity)

        if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
            try_move = get_path(curr_pos, house_loc)
            if curr_pos + try_move in map_info[1]:
                return create_attack_action(try_move)
            return create_move_action(get_path(curr_pos, house_loc))
        else:
            closest_mine = Point(9999999999, 999999999)

            for mine in map_info[4]:
                delta = Point.Distance(house_loc, mine)
                if delta < Point.Distance(closest_mine, house_loc):
                    closest_mine = mine

            delta = closest_mine - curr_pos
            if delta in [Point(0,1), Point(0,-1), Point(1,0), Point(-1,0)]:
                return create_collect_action(delta)

            try_move = get_path(curr_pos, closest_mine)
            if curr_pos + try_move in map_info[1]:
                return create_attack_action(try_move)

            return create_move_action(try_move)



        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
