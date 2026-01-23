import asyncio
import datetime
import discord
import env
import json
import re
import os
import shutil
import subprocess
import PyJLogger
from discord.ext import tasks, commands
logger = PyJLogger.get_logger("PyJlogger", 0)

asyncio.set_event_loop(asyncio.new_event_loop())
client = discord.Bot(intents=discord.Intents.all(), status=discord.Status.online)

__version__ = "2.0.3"

whitelist: dict[str, int] = env.whitelist


def whitelisted(user_name: str, user_id: int) -> bool:
    for whitelist_name, discord_id in whitelist.items():
        if int(discord_id) == int(user_id):
            logger.debug(f"Whitelisted LocalName:{whitelist_name} DiscordName:{user_name} DiscordID:{user_id}")
            return True
    logger.debug(f"{user_name} not in whitelist")
    return False


def server_image(server_name: str) -> discord.File:
    match server_name:
        case "AKS1":
            return discord.File(env.aks1serverimage, filename="ServerIcon.png")
        case "AKS2":
            return discord.File(env.aks2serverimage, filename="ServerIcon.png")
        case "AKS3":
            return discord.File(env.aks3serverimage, filename="ServerIcon.png")
        case "AKS4":
            return discord.File(env.aks4serverimage, filename="ServerIcon.png")
        case "AKS5":
            return discord.File(env.aks5serverimage, filename="ServerIcon.png")
        case _:
            return discord.File(env.aks6backupimage, filename="ServerIcon.png") # Fallback image


def sanitize(line: str) -> str:
    try:
        pattern = re.compile(
            r"\[(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
            r".*?message = (?P<message>.*?), playerId = .*?playerName = (?P<name>.+)$")
        match = pattern.search(line)

        if match:
            results = {
                "time": match.group("time"),
                "name": match.group("name"),
                "message": match.group("message")}
        else:
            results = {
                "time": "None",
                "name": "None",
                "message": "None"}

        return f"{results['time']} | {results['name']}: \n{results['message']}"
    except Exception as e:
        logger.exception(repr(e))
        return f""


async def aks1_log():
    try:
        file = env.aks1chatfilepath
        with open(f"{file}", "w") as f_clear:
            f_clear.write("")
        with open(f"{file}", "r") as f_in:
            f_in.seek(0, 2)
            while True:
                line = f_in.readline()
                if not line:
                    await asyncio.sleep(5)
                    continue

                line = sanitize(line=line)
                file = server_image("AKS1")
                embed = discord.Embed(
                    title=f"**AKS1**",
                    description=f"**```{line}```**",
                    color=discord.Color.random())
                try:
                    embed.set_thumbnail(url=f"attachment://ServerIcon.png")
                except Exception as e:
                    logger.exception(repr(e))
                await client.get_channel(env.forwardchattodiscordchannelchatid).send(embed=embed, file=file)
    except Exception as e:
        logger.exception(repr(e))
        await asyncio.sleep(60 * 60 * 24)


async def aks2_log():
    try:
        file = env.aks2chatfilepath
        with open(f"{file}", "w") as f_clear:
            f_clear.write("")
        with open(f"{file}", "r") as f_in:
            f_in.seek(0, 2)
            while True:
                line = f_in.readline()
                if not line:
                    await asyncio.sleep(5)
                    continue

                line = sanitize(line=line)
                file = server_image("AKS2")
                embed = discord.Embed(
                    title=f"**AKS2**",
                    description=f"**```{line}```**",
                    color=discord.Color.random())
                try:
                    embed.set_thumbnail(url=f"attachment://ServerIcon.png")
                except Exception as e:
                    logger.exception(repr(e))
                await client.get_channel(env.forwardchattodiscordchannelchatid).send(embed=embed, file=file)
    except Exception as e:
        logger.exception(repr(e))
        await asyncio.sleep(60 * 60 * 24)


async def aks3_log():
    try:
        file = env.aks3chatfilepath
        with open(f"{file}", "w") as f_clear:
            f_clear.write("")
        with open(f"{file}", "r") as f_in:
            f_in.seek(0, 2)
            while True:
                line = f_in.readline()
                if not line:
                    await asyncio.sleep(5)
                    continue

                line = sanitize(line=line)
                file = server_image("AKS3")
                embed = discord.Embed(
                    title=f"**AKS3**",
                    description=f"**```{line}```**",
                    color=discord.Color.random())
                try:
                    embed.set_thumbnail(url=f"attachment://ServerIcon.png")
                except Exception as e:
                    logger.exception(repr(e))
                await client.get_channel(env.forwardchattodiscordchannelchatid).send(embed=embed, file=file)
    except Exception as e:
        logger.exception(repr(e))
        await asyncio.sleep(60 * 60 * 24)


async def aks4_log():
    try:
        file = env.aks4chatfilepath
        with open(f"{file}", "w") as f_clear:
            f_clear.write("")
        with open(f"{file}", "r") as f_in:
            f_in.seek(0, 2)
            while True:
                line = f_in.readline()
                if not line:
                    await asyncio.sleep(5)
                    continue

                line = sanitize(line=line)
                file = server_image("AKS4")
                embed = discord.Embed(
                    title=f"**AKS4**",
                    description=f"**```{line}```**",
                    color=discord.Color.random())
                try:
                    embed.set_thumbnail(url=f"attachment://ServerIcon.png")
                except Exception as e:
                    logger.exception(repr(e))
                await client.get_channel(env.forwardchattodiscordchannelchatid).send(embed=embed, file=file)
    except Exception as e:
        logger.exception(repr(e))
        await asyncio.sleep(60*60*24)


async def aks5_log():
    try:
        file = env.aks5chatfilepath
        with open(f"{file}", "w") as f_clear:
            f_clear.write("")
        with open(f"{file}", "r") as f_in:
            f_in.seek(0, 2)
            while True:
                line = f_in.readline()
                if not line:
                    await asyncio.sleep(5)
                    continue

                line = sanitize(line=line)
                file = server_image("AKS5")
                embed = discord.Embed(
                    title=f"**AKS5**",
                    description=f"**```{line}```**",
                    color=discord.Color.random())
                try:
                    embed.set_thumbnail(url=f"attachment://ServerIcon.png")
                except Exception as e:
                    logger.exception(repr(e))
                await client.get_channel(env.forwardchattodiscordchannelchatid).send(embed=embed, file=file)
    except Exception as e:
        logger.exception(repr(e))
        await asyncio.sleep(60 * 60 * 24)


async def json_backup():
    while True:
        try:
            timenow = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H-%M-%S")
            for x in range(1, 6):
                shutil.copy2(
                    src=f"{env.aksconfigpath}AKS{x}/config.json",
                    dst=f"{env.aksconfigpath}AKS{x}/Backup/{timenow}.config.json")
                logger.info(f"Backup NR {x}")
        except Exception as e:
            logger.exception(f"Failed Backup {repr(e)}")
        await asyncio.sleep(60 * 60 * 12)  # 12 std

@client.event
async def on_ready():
    #await client.sync_commands(force=False)

    asyncio.create_task(aks1_log())
    asyncio.create_task(aks2_log())
    asyncio.create_task(aks3_log())
    asyncio.create_task(aks4_log())
    asyncio.create_task(aks5_log())
    asyncio.create_task(json_backup())
    logger.info(f"{client.user.name} Ready")


@client.event
async def on_message(message: discord.Message):
    if message.author != client.user:
        logger.info(f"Message In Channel({message.channel}) From({message.author.name}:{message.author.id}) MessageContent({message.content})")


@client.slash_command(name="ping", description="Heartbeat")
async def ping(ctx: discord.ApplicationContext):
    latency = round(client.latency*1000)
    await ctx.respond(f"Pong! `{latency}ms`")


@commands.cooldown(1, 5, commands.BucketType.default)
@client.slash_command(name="mod_list_csv", description="Get the current mods of Server X")
async def mod_list_csv(ctx, server: discord.Option(str, choices=["AKS1", "AKS2", "AKS3", "AKS4", "AKS5"])):
    await ctx.defer()
    timenow = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H-%M-%S")
    config_file_path = f"{env.aksconfigpath}{server}/config.json"
    with open(f"{config_file_path}", "r", encoding="utf-8") as f:
        config = json.load(f)
        mods = config["game"]["mods"]
        modcsv = ""
        for mod in mods:
            modcsv += f"{mod.get('modId')}, {mod.get('name')}\n"
    with open(f"./tmp/{server}_{timenow}-modlist.csv", "w", encoding="utf-8") as f:
        f.write(modcsv)
    await ctx.respond(file=discord.File(f"./tmp/{server}_{timenow}-modlist.csv"))


@mod_list_csv.error
async def mod_list_csv_error(ctx, error):
    await ctx.respond(f"{ctx.author.mention} Triggered Restart_Error:({error})")


@commands.cooldown(1, 20, commands.BucketType.default)
@client.slash_command(name="mod_remove", description="Remove mod X from the Server")
async def remove_mod(ctx, server: discord.Option(str, choices=["AKS1", "AKS2", "AKS3", "AKS4", "AKS5"]), mod_id: str):
    await ctx.defer()
    if not whitelisted(user_name=ctx.author.name, user_id=ctx.author.id):
        await ctx.respond(f"# U SHALL NOT USE WHAT U CAN'T COMPREHEND PEASANT.\nGet Permission from an Admin")
        return
    MOD_ID_TO_REMOVE = str(mod_id.upper())
    config_file_path = f"{env.aksconfigpath}{server}/config.json"
    with open(f"{config_file_path}", "r", encoding="utf-8") as f:
        config = json.load(f)

    mods = config["game"]["mods"]
    filtered_mods = []
    mod_removed = False
    for mod in mods:
        if mod.get("modId") != MOD_ID_TO_REMOVE:
            filtered_mods.append(mod)
        else:
            mod_removed = True

    config["game"]["mods"] = filtered_mods

    with open(f"{config_file_path}", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
    if mod_removed:
        link = f"https://reforger.armaplatform.com/workshop/{mod_id}"
        logger.info(f"{ctx.author.name} removed mod {link} from Server {server}")
        await ctx.respond(f"Removed [Mod]({link}) `{mod_id}` from Server {server}")
    else:
        await ctx.respond(f"Mod `{mod_id}` not found")


@remove_mod.error
async def remove_mod_error(ctx, error):
    await ctx.respond(f"{ctx.author.mention} Triggered Restart_Error:({error})")


@commands.cooldown(1, 20, commands.BucketType.default)
@client.slash_command(name="mod_add", description="Add mod X for the Server X")
async def add_mod(ctx, server: discord.Option(str, choices=["AKS1", "AKS2", "AKS3", "AKS4", "AKS5"]), mod_id: str, mod_name: str):
    await ctx.defer()
    if not whitelisted(user_name=ctx.author.name, user_id=ctx.author.id):
        await ctx.respond(f"# U SHALL NOT USE WHAT U CAN'T COMPREHEND PEASANT.\nGet Permission from an Admin")
        return
    new_mod = {
        "modId": f"{mod_id}",
        "name": f"{mod_name}",
        "version": ""
    }
    config_file_path = f"{env.aksconfigpath}{server}/config.json"

    with open(f"{config_file_path}", "r", encoding="utf-8") as f:
        config = json.load(f)
    with open(f"{config_file_path}", "w", encoding="utf-8") as f:
        mods = config["game"]["mods"]
        mods.insert(0, new_mod)
        json.dump(config, f, indent=4)
    link = f"https://reforger.armaplatform.com/workshop/{mod_id}"
    logger.info(f"{ctx.author.name} added mod {link} to Server {server}")
    await ctx.respond(f"Added [Mod]({link}) ```json\n{new_mod}```\nto {server}")


@add_mod.error
async def add_mod_error(ctx, error):
    await ctx.respond(f"{ctx.author.mention} Triggered Restart_Error:({error})")



def restart_command(server_name: str) -> str or None:
    match server_name:
        case "AKS1":
            return "systemctl restart arma-reforger-HAUPT.service"
        case "AKS2":
            return "systemctl restart arma-reforger-VANILLA1.service"
        case "AKS3":
            return "systemctl restart arma-reforger-PVP.service"
        case "AKS4":
            return "systemctl restart arma-reforger-RESERVE.service"
        case "AKS5":
            return "systemctl restart arma-reforger-TEST.service"
        case _:
            return None


def clear_session_func(server_name: str) -> str:
    match server_name:
        case "AKS1":
            return env.sessionsavepath1
        case "AKS2":
            return env.sessionsavepath2
        case "AKS3":
            return env.sessionsavepath3
        case "AKS4":
            return env.sessionsavepath4
        case "AKS5":
            return env.sessionsavepath5
        case _:
            return env.sessionsavepath5


@commands.cooldown(1, 8, commands.BucketType.default)
@client.slash_command(name="restart", description="Restart an arma instance")
async def restart(ctx, server: discord.Option(str, choices=["AKS1", "AKS2", "AKS3", "AKS4", "AKS5"]), clear_session: discord.Option(bool, choices=[True, False]), comment: str = "No comment given"):
    await ctx.defer()
    if not whitelisted(user_name=ctx.author.name, user_id=ctx.author.id):
        logger.warn(f"{ctx.author.name} tried to restart({server}) comment: {comment} but is not whitelisted")
        await ctx.respond(f"# U SHALL NOT USE WHAT U CAN'T COMPREHEND PEASANT.\nGet Permission from an Admin")
        return
    try:
        command = restart_command(server_name=server)
        if clear_session:
            logger.info(f"Running clear command({command})")
            clear_session_path = clear_session_func(server)
            for entry in os.listdir(clear_session_path):
                if os.path.isdir(f"{clear_session_path}/{entry}"):
                    shutil.rmtree(f"{clear_session_path}/{entry}")
        if command:
            logger.info(f"Running command({command})")
            subprocess.run(command.split(), check=True, timeout=30)
        else:
            raise TypeError(f"Server({server}) restart command not found")
    except Exception as e:
        logger.error(f"{ctx.author.name} tried to restart({server}) but Exception:({repr(e)}) was triggered and couldn't be restarted")
        await ctx.respond(f"{ctx.author.name} `tried to restart({server}) but Exception:({repr(e)}) was triggered`", ephemeral=False)
        return

    try:
        logger.info(f"{ctx.author.name} restarted({server}) comment: {comment}")
        file = server_image(server)
        embed = discord.Embed(
            title=f"**✅ {server}**",
            description=f"{ctx.author.mention} Restarted. \nClear SESSION={str(clear_session)}\n\n"
                        f"Optional comment: \n**```\n{comment}```**",
            color=discord.Color.green()
        )
        try:
            embed.set_image(url="attachment://ServerIcon.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
        except Exception as e:
            logger.exception(f"couldn't set embed image/thumbnail, skipping image E:{repr(e)}")

        await ctx.respond(embed=embed, file=file, ephemeral=False)
        logger.info(f"Restart embed sent successfully")
    except Exception as e:
        logger.error(f"Embed sent failed with {repr(e)}")

@restart.error
async def restart_error(ctx, error):
    logger.error(f"{ctx.author.name} Triggered Restart_Error:({error})")
    await ctx.respond(f"{ctx.author.name} Triggered Restart_Error:({error})")


client.run(str(env.TOKEN))
