from helper import *

def get_path(curr_pos, tar_pos, map):
    delta = curr_pos - tar_pos
    if delta.x < 0 and delta in map[0]:
        return Point(1, 0)
    elif delta.x > 0 and delta in map[0]:
        return Point(-1, 0)
    elif delta.y < 0 and delta in map[0]:
        return Point(0, 1)
    else:
        return Point(0, -1)


def go_home(curr_pos, target, map):
    return get_path(curr_pos, target, map)


def go_mine(curr_pos, target, map):
    return get_path(curr_pos, target, map)


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
        map_info = {0:[], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        map_weight = []
        for y in range(gameMap.yMin, gameMap.yMax):
            map_weight.append([])
            for x in range(gameMap.xMin, gameMap.xMax):
                tile_type = gameMap.getTileAt(Point(x, y)).value
                # if tile_type in [0, 2, 4, 5, 6]:
                #     map_weight[y - gameMap.yMin].append((1))
                # elif tile_type == 3:
                #     map_weight[y - gameMap.yMin].append((999999))
                # elif tile_type == 1:
                #     map_weight[y - gameMap.yMin].append((9))

                map_info[tile_type].append(Point(x, y))

        if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
            return create_move_action(go_home(curr_pos, house_loc, map_info))
        else:
            closest_mine = Point(9999999999, 999999999)

            for mine in map_info[4]:
                delta = Point.Distance(house_loc, mine)
                if delta < Point.Distance(closest_mine, house_loc):
                    closest_mine = mine

            delta = closest_mine - curr_pos
            if delta in [Point(0,1), Point(0,-1), Point(1,0), Point(-1,0)]:
                return create_collect_action(delta)

            return create_move_action(go_mine(curr_pos, closest_mine, map_info))



        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
