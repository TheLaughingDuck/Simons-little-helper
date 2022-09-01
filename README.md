# Default-DiscordBot

## Introduction and Purpose
A clonable repository that can be used as a starting point for new discord bot projects. This repo contains my own instructions or "modus operandi", and might not work for you. Follow the instructions under "Getting started" below to get started.


## Getting started
* Setup Github repository and working environment.
    - Start by forking this repository.
    - Rename and change the description of the new repository.
    - Clone the repository into a suitable local folder with git (for example with Github Desktop).
    - Remove the "#" from the .gitignore file. (This will prevent changes in your .environ file from being uploaded. That would be VERY bad)

* Create a Discord Application.
    - Go to the (discord developer portal)[https://discord.com/developers/docs/intro], select **Applications** -> create a **New application**.
    - Choose a project name and provide a short description of your project. **Note:** This project name can be different from the bots username.
    - Go to **Settings** -> **Bot** and create a Bot user.
    - Configure the bot settings. Specifically: Toggle Public, and enable the **Presence-** **Server members-** and **Message Content -** Intents.
    - Go to the OAuth2 URL Generator, select scopes (specifically **bot**), select bot permissions (for example **Send Messages**, **Read Messages/View Channels**). Copy and paste the generated URL in a browser Tab.

* Launch the bot.
    - Grab your bot token (in **Settings** -> **Bot**), and put it into your .environ file. Formatting should be:

        ```
        KEY1 = 12345
        ```

    - Enable the client.run() command at the bottom of main.py.
    - Try running the bot.

* Host the bot on Heroku (Heroku will **not** offer free Dynos starting **November 28, 2022**)
    - Go to Heroku.com, create a new app, give it a name and region.
    - Go to **Settings** -> **Add buildpack** -> choose **python**.
    - Go to **Deploy** and follow the instructions to **Deploy using Heroku Git** (assuming you already have the Heroku CLI downloaded). Start by "connecting" your previously existing repository (see bottom of the instructions).
    - Go to **Resources** -> **Dynos** and activate the "worker" dyno.

## Additional Nice Things
* Upload an App Icon and **Bot Icon** in the discord developer portal.
* Change your bots