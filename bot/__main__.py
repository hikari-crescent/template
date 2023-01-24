import hikari
import crescent

from bot.model import Model


bot = hikari.GatewayBot("1234")

model = Model()

client = crescent.Client(bot, model)
client.plugins.load_folder("bot.plugins")

bot.subscribe(hikari.StartingEvent, model.on_start)
bot.subscribe(hikari.StoppedEvent, model.on_stop)

bot.run()
