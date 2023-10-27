from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1845829
    API_HASH = "334d370d0c39a8039e6dfc53dd0f6d75"
    # the name to display in your alive message
    ALIVE_NAME = "Hi Im BruteWoorse"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = None
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOLMBu13E20SKXL7NIThS6ibU8pv7IYRMMkvytmOtu5VvcomTJ88wnVut6TLokIXBYovohP5xopI_a7_ma7odbGT7TzRQuqGHhJ-Rq75ERN9iXxszhNzLgMNnQ0MvwvtLdcokTFul4zKLRmSEYq8uQUBGbXg79ce6X1xDlOjaQZjPPiYBkM_l7mjy0gqpj_6fEFdL7-6Nbas_UAlrenBQ4dEm64Rv3gYeUniAYeZViNcKThR_RLTVpL5V9LK7kEenGWGKwMjJlg587iNmF5q8sNSGqXhCJefujWSEUKyJ2AOAtxI5-W16SnX0FNAM1NFl4rvO73Y-2ueEO0MQqLoNir_atDU="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6838526055:AAFqYnACYbxVIvfO7jamQEenM56ZHuCzEPE"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"