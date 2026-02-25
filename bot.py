import random
from bot_logic import gen_pass
from discord.ext import commands
import discord
# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
# Criar o bot com prefixo $
bot = commands.Bot(command_prefix="$", intents=intents)
# Evento: quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")
# Evento: quando alguém entra no servidor
@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="geral")
    if canal:
        await canal.send(f"🎉 Bem-vindo(a) ao servidor, {member.mention}!")
    else:
        print("⚠️ Canal 'geral' não encontrado!")
# Comando: hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
# Comando: bye
@bot.command()
async def bye(ctx):
    await ctx.send("🙂")
# Comando: senha
@bot.command()
async def senha(ctx):
    senha_gerada = gen_pass(10)
    await ctx.send(f"🔐 Sua senha gerada é: {senha_gerada}")
# Comando: info bonitinha
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="🤖 Meu Bot",
        description="Eu sou um bot em desenvolvimento na aula de hoje!",
        color=discord.Color.green()
    )
    embed.add_field(
        name="📌 Comandos disponíveis:",
        value="$hello\n$bye\n$senha\n$info\n$roll",
        inline=False
    )
    embed.set_footer(text="Criado durante a aula de programação 😄")
    await ctx.send(embed=embed)
@bot.command()
async def roll(ctx, dice: str  = "1d6"):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.run("MTQ3MTI3NzUyNDIyMTk1NjMxOQ.G-4MkE.BLeKz6rfqelaFPe69YkqaCy6nE_juHKweqO3O4")
