from helper import *
from pypaths import astar


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

        # Write your bot here. Use functions from aiHelper to instantiate your actions.

        # Create map array
        map_vision = []
        for y in range(gameMap.yMin,gameMap.yMax):
            map_vision.append([])
            for x in range(gameMap.xMin, gameMap.xMax):
                map_vision[y - gameMap.yMin].append(gameMap.getTileAt(Point(x,y)).value)

        # initialize direction
        # player is in constant motion

        # MOVE

        # while the ADJACENT TILE TO THE RIGHT is empty, move 1
        while self.x(TileContent) == 0:
            
            # coordinates in (x,y)
            # x increasing left to right
            # y increasing top to bottom
            create_move_action(1,0)



        # ATTACK

        if TileContent == 6:
            create_attack_action(1,0)

        # COLLECT

        # STEAL

        # HEAL

        # PURCHASE

        # Show map
        # for x in map_vision:
        #     for y in x:
        #         print(y,end="")
        #     print()

        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
