import crescent
import hikari

from bot.model import Model


class Plugin(crescent.UserPlugin[hikari.GatewayBot, Model]):
    ...
