import crescent
from crescent.ext import cooldowns

bot = crescent.Bot("...")


# The user can use the command 3 times in 20 seconds
@bot.include
@crescent.hook(cooldowns.cooldown(20, 3))
@crescent.command
async def my_command(ctx: crescent.Context) -> None:
    await ctx.respond("Hello!")


async def on_rate_limited(ctx: crescent.Context, time_remaining: float) -> None:
    await ctx.respond(f"You are ratelimited for {time_remaining}s.")


@bot.include
@crescent.hook(cooldowns.cooldown(100, 1, callback=on_rate_limited))
@crescent.command
async def my_command2(ctx: crescent.Context) -> None:
    await ctx.respond("Hello!")


bot.run()
