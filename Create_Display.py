import tkinter as tk
import Buttons

def create_widgets(app):
    app.lifetimeStats = tk.Label(text="lifetimeStats", relief="raised", bg="#387dba")
    app.lifetimeStats.grid(column=0, columnspan=3, row=0, sticky="nesw")

    app.exitButton = tk.Button(text="X", relief="raised", bg="#d93b45",
                               command=lambda: Buttons.exit_Button())
    app.exitButton.grid(column=3, row=0, sticky="nesw")

    app.clicksDisplay = tk.Label(
        text=app.user_player.display_clicks(),
        relief="raised", bg="#387ec8"
    )
    app.clicksDisplay.grid(column=0, row=1, sticky="nesw")

    app.levelDisplay = tk.Label(
        text=app.user_player.display_level(),
        relief="raised", bg="#387ec8"
    )
    app.levelDisplay.grid(column=1, row=1, sticky="nesw")

    app.rebirthDisplay = tk.Label(
        text=app.user_player.display_rebirth(),
        relief="raised", bg="#387ec8"
    )
    app.rebirthDisplay.grid(column=2, row=1, sticky="nesw")

    app.SaveLoad = tk.Button(text="Save / Load", relief="raised", bg="#3c82c8")
    app.SaveLoad.grid(column=3, row=1, sticky="nesw")

    app.clicksButton = tk.Button(
    text=app.user_player.display_clicksPerClick(),
    relief="raised", bg="#3c82c8",
    command=lambda: Buttons.clicks_Button(app.user_player)
    )
    app.clicksButton.grid(column=0, row=2, sticky="nesw")

    app.levelButton = tk.Button(
        text=app.user_player.display_levelCost(),
        relief="raised", bg="#3c82c8",
        command=lambda: Buttons.level_Button(app.user_player)
    )
    app.levelButton.grid(column=1, row=2, sticky="nesw")

    app.rebirthButton = tk.Button(text="rebirthButton", relief="raised", bg="#3c82c8",
                                  command=lambda: Buttons.rebirth_Button(app.user_player))
    app.rebirthButton.grid(column=2, row=2, sticky="nesw")

    app.ascendButton = tk.Button(text="ascendButton", relief="raised", bg="#3c82c8")
    app.ascendButton.grid(column=3, row=2, sticky="nesw")
