class Player_Class:
    def __init__(self):
        self.__lifetimeClicks = 0
        self.__lifetimeLevels = 0
        self.__lifetimeRebirths = 0
        self.__lifetimeAscend = 0
        self.__clicks = 1000000000000
        self.__level = 0
        self.__rebirth = 0
        self.__ascend = 0
        self.__clicksPerClick = 1
        self.__clicksPerClickPerLevel = 0
        self.__clicksPerClickPerRebirth = 0
        self.__levelCost = 10
        self.__rebirthCost = 5
        self.__ascendCost = 10

   
    def get_lifetimeClicks(self):
        return (self.__lifetimeClicks)

    def add_lifetimeClicks(self, number):
        self.__lifetimeClicks += number


    def get_lifetimeLevels(self):
        return (self.__lifetimeLevels)

    def add_lifetimeLevels(self, number):
        self.__lifetimeLevels += number


    def get_lifetimeRebirths(self):
        return (self.__lifetimeRebirths)

    def add_lifetimeRebirths(self, number):
        self.__lifetimeRebirths += number


    def get_lifetimeAscend(self):
        return (self.__lifetimeAscend)

    def add_lifetimeAscend(self, number):
        self.__lifetimeAscend += number

    

    def get_clicks(self):
        return self.__clicks

    def display_clicks(self):
        return f"Clicks: {self.__clicks}"

    def change_clicks(self, clicks):
        self.__clicks = max(0, clicks)

    def add_clicks(self, number):
        self.change_clicks(self.__clicks + number)

    def sub_clicks(self, number):
        self.change_clicks(self.__clicks - number)


    def get_level(self):
        return self.__level

    def display_level(self):
        return f"Levels: {self.__level}"

    def change_level(self, level):
        self.__level = max(0, level)
        self.change_levelCost()

    def add_level(self, number):
        self.change_level(self.__level + number)

    def sub_level(self, number):
        self.change_level(self.__level - number)


    def get_rebirth(self):
        return self.__rebirth

    def display_rebirth(self):
        return f"Rebirth: {self.__rebirth}"

    def change_rebirth(self, rebirth):
        self.__rebirth = max(0, rebirth)
        self.change_rebirthCost()

    def add_rebirth(self, number):
        self.change_rebirth(self.__rebirth + number)

    def sub_rebirth(self, number):
        self.change_rebirth(self.__rebirth - number)


    def get_ascend(self):
        return self.__ascend

    def change_ascend(self, ascend):
        self.__ascend = max(0, ascend)
        self.change_ascendCost()

    def add_ascend(self, number):
        self.change_ascend(self.__ascend + number)



    def get_clicksPerClick(self):
        return self.__clicksPerClick

    def display_clicksPerClick(self):
        return f"{self.__clicksPerClick} Clicks Per Click"

    def change_clicksPerClick(self, clicksPerClick):
        self.__clicksPerClick = max(1, clicksPerClick)

    def add_clicksPerClick(self, number):
        self.change_clicksPerClick(self.__clicksPerClick + number)

    def update_clicksPerClick(self):
        self.__clicksPerClick = 1 + self.__clicksPerClickPerLevel + self.__clicksPerClickPerRebirth + (self.__ascend * 100)


    def get_clicksPerClickPerLevel(self):
        return self.__clicksPerClickPerLevel

    def change_clicksPerClickPerLevel(self, clicksPerClickPerLevel):
        self.__clicksPerClickPerLevel = max(0, clicksPerClickPerLevel)

    def add_clicksPerClickPerLevel(self, number):
        self.change_clicksPerClickPerLevel(self.__clicksPerClickPerLevel + number)


    def get_clicksPerClickPerRebirth(self):
        return self.__clicksPerClickPerRebirth

    def change_clicksPerClickPerRebirth(self, clicksPerClickPerRebirth):
        self.__clicksPerClickPerRebirth = max(0, clicksPerClickPerRebirth)

    def add_clicksPerClickPerRebirth(self, number):
        self.change_clicksPerClickPerRebirth(self.__clicksPerClickPerRebirth + number)



    def get_levelCost(self):
        return self.__levelCost

    def display_levelCost(self):
        return f"{self.__levelCost} Clicks Per Level"

    def change_levelCost(self):
        self.__levelCost = 10 if self.__level <= 0 else (10 * self.__level) + 10


    def get_rebirthCost(self):
        return self.__rebirthCost

    def display_rebirthCost(self):
        return f"{self.__rebirthCost} Levels Per Rebirth"

    def change_rebirthCost(self):
        self.__rebirthCost = 5 if self.__rebirth <= 0 else (5 * self.__rebirth) + 5


    def get_ascendCost(self):
        return self.__ascendCost

    def display_ascendCost(self):
        return f"{self.__ascendCost} Rebirth Per Ascension"

    def change_ascendCost(self):
        self.__ascendCost = 25 if self.__ascend <= 0 else (25 * self.__ascend) + 25
