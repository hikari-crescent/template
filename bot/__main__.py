import hikari
import crescent

from bot.model import Model


bot = hikari.GatewayBot("1234")

model = Model()
client = crescent.ClientBuilder().with_model(model).gateway(bot)

bot.subscribe(hikari.StartedEvent, model.on_start)
bot.start()
