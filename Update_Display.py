def update_widgets(app):
    user_player_lifetimeStats = f"Clicks: {app.user_player.get_lifetimeClicks()}    Levels: {app.user_player.get_lifetimeLevels()}    Rebirths: {app.user_player.get_lifetimeRebirths()}    Ascends: {app.user_player.get_lifetimeAscend()}"
    app.lifetimeStats.configure(text=user_player_lifetimeStats)
    app.clicksDisplay.configure(text=app.user_player.display_clicks())
    app.levelDisplay.configure(text=app.user_player.display_level())
    app.rebirthDisplay.configure(text=app.user_player.display_rebirth())
    app.clicksButton.configure(text=app.user_player.display_clicksPerClick())
    app.levelButton.configure(text=app.user_player.display_levelCost())
    app.rebirthButton.configure(text=app.user_player.display_rebirthCost())
    app.ascendButton.configure(text=app.user_player.display_ascendCost())

    app.after(100, lambda: update_widgets(app))
