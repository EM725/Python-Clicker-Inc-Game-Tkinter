import sys

def exit_Button():
    sys.exit()

def clicks_Button(player):
    clicks_per_click = player.get_clicksPerClick()

    player.add_clicks(clicks_per_click)
    player.add_lifetimeClicks(clicks_per_click)


def level_Button(player):
    if player.get_clicks() >= player.get_levelCost():
        player.sub_clicks(player.get_levelCost())
        player.add_level(1)
        player.add_lifetimeLevels(1)
        player.add_clicksPerClickPerLevel(1)
        player.update_clicksPerClick()


def rebirth_Button(player):
    if player.get_level() >= player.get_rebirthCost():
        player.sub_level(player.get_rebirthCost())
        player.add_rebirth(1)
        player.add_lifetimeRebirths(1)
        player.change_clicksPerClickPerLevel(0)
        player.add_clicksPerClickPerRebirth(5)
        player.update_clicksPerClick()