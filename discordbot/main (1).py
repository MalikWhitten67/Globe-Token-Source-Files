
import asyncio
import functools
import itertools
import math
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import random
import os
import json
import datetime
from discord import Activity, ActivityType
import discord
from discord.ext import commands, tasks
from threading import Thread
from discord import Activity, ActivityType
from discord.utils import get
import os




intents = discord.Intents().all()
bot = commands.Bot(command_prefix="^", intents=intents)

@bot.event
async def on_ready():
    print('The bot is logged in.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" Watching globe Decentralized Services| ^help"))




@bot.command()
@commands.has_permissions(ban_members = True)
@commands.is_owner()
async def restart(ctx):
    await ctx.send(f'Restarting')
    os.system('python startup.py')
    exit()




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(' You need to specify the given command:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry you lack the necessary roles:angry:")


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)


@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="Unmuted", description=f" {member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)



@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")




bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='**My commands!!**',
        description='Below is a list of commands',
        colour=discord.Color.green(),
        timestamp=datetime.datetime.now()

       


        ).add_field(
        name='**kick**',
        value='^kick | [ allows you to kick @mentioned  member   ]',
        inline=False

        ).add_field(
        name='**ban**',
        value='^ban | [ allows you to ban @mentioned  member   ]',
        inline=False


        ).add_field(
        name='**mute**',
        value='^mute | [ mutes @mentioned member   ]',
        inline=False



        
        ).add_field(
        name='**unmute**',
        value='^unmute | [ unmutes @mentioned member   ]',
        inline=False


        
        ).add_field(
        name='**chart**',
        value='^chart | [ shows an embed message of links to view Jetokens price   ]',
        inline=False


        
        ).add_field(
        name='**contract**',
        value='^contract | [  Shows an embed message of jetokens custom contract   ]',
        inline=False


         ).add_field(
        name='**links**',
        value='^links | [Gives you links to learn more about JeToken!  ]',
        inline=False



        
        ).add_field(
        name='**purge**',
        value='^purge | [  Deletes messages in specified channel  ]',
        inline=False


        ).add_field(
        name='**buy**',
        value='^buy | [ Gives user info on how to purchase JETS  ]',
        inline=False





        ).add_field(
        name='**new**',
        value='^new | [ Creates a new ticket and pings admin!  ]',
        inline=False



        ).add_field(
        name='**close**',
        value='^close {channel name} |closes a ticket ]',
        inline=False


        ).add_field(
        name='**tickethelp**',
        value='^tickethelp  |Gives you a help guide on how to use the ticket system ]',
        inline=False



        






        ).set_footer(
        text='Requested!',
        icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_image(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_thumbnail(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
        )

    await ctx.send(embed=embed)



@bot.command()
async def chart(ctx):
    embed = discord.Embed(
        title='**GLB Price Charts**',
        description='',
        colour=discord.Color.green(),
        timestamp=datetime.datetime.now()

       


    
        
        ).add_field(
        name='**Poo coin**',
        value='https://poocoin.app/tokens/0xf46b841f9367f5ff559c8670617129452607e722',
        inline=False

        
        ).add_field(
        name='**Bog**',
        value='https://charts.bogged.finance/0xf46B841F9367f5fF559c8670617129452607e722',
        inline=False



        ).set_footer(
        text='Requested!',
        icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_image(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_thumbnail(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
        )

    await ctx.send(embed=embed)



@bot.command()
async def contract(ctx):
    embed = discord.Embed(
        title='**GLB Contract **',
        description='⚠️DO Not SEND FUNDS TO THIS ADDRESS... ONLY TO VIEW YOUR TOKENS⚠️',
        colour=discord.Color.green(),
        timestamp=datetime.datetime.now()

       


    
        
        ).add_field(
        name='**Contract Adress**',
        value='0xf46b841f9367f5ff559c8670617129452607e722',
        inline=False


        ).add_field(
        name='**Name**',
        value='Globe Token',
        inline=False


        ).add_field(
        name='**Symbol**',
        value='GLB',
        inline=False


        ).add_field(
        name='**Decimals**',
        value='18',
        inline=False


        ).add_field(
        name='**Bsc Scanner**',
        value='https://bscscan.com/token/0xf46b841f9367f5ff559c8670617129452607e722',
        inline=False


       


        ).set_footer(
        text='Requested!',
        icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_image(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_thumbnail(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
        )

    await ctx.send(embed=embed)





intents = discord.Intents.default()
intents.members = True
@bot.event
async def on_member_join(member):
    if member.guild.name == '$GLB':  #type your server name
        embed = discord.Embed(title=f'Hello Welcome to The official $GLB Discord server Please make sure to abide by the rules thankyou!!',
                    color=0x0061ff,
                    font_size=200)
        await bot.get_channel(898463880035069963).send(f"{member.mention}")
        await bot.get_channel(898463880035069963).send(embed=embed)
        role = discord.utils.get(member.guild.roles, name="Passengers")
        await member.add_roles(role)
    else:
        return



























@bot.command()
async def buy(ctx):
    embed = discord.Embed(
        title='**How To Buy GLB**',
        description='⚠️DO Not SEND FUNDS TO The  ADDRESS... It is only for you to buy!!',
        colour=discord.Color.green(),
        timestamp=datetime.datetime.now()

       


    
        
        ).add_field(
        name='**Import the  Contract Adress**',
        value='0xf46b841f9367f5ff559c8670617129452607e722',
        inline=False




         
        ).add_field(
        name='**Buy GLB on Pancake**',
        value='https://pancakeswap.finance/swap?outputCurrency=0xf46b841f9367f5ff559c8670617129452607e722',
        inline=False







        ).set_footer(
        text='Requested!',
        icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_image(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_thumbnail(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
        )

    await ctx.send(embed=embed)




@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.kick()
    await ctx.send(f"**{user}** has been kicked for **no reason**.")
  else:
    await user.kick(reason=reason)
    await ctx.send(f"**{user}** has been kicked for **{reason}**.")




























@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')

@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')















import requests

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
        
   
    if message.content.startswith('^price'):

        
        coinpaprika = 'https://api.coinpaprika.com/v1/'

        
        r = requests.get(url=coinpaprika)

        
        data = r.json()

        
        price = data['globe token']['usd']

        
        price = format(price, '.12f')

       
        await message.channel.send(f'The price is: {price} USD')





































@bot.command()
async def links(ctx):
    embed = discord.Embed(
        title='** JeToken Links **',
        description='',
        colour=discord.Color.green(),
        timestamp=datetime.datetime.now()

       


    
        
        ).add_field(
        name='**Website**',
        value='https://www.globetoken.gq',
        inline=False




       ).add_field(
        name='**Twitter**',
        value='https://twitter.com/GlobeTokenLLC',
        inline=False

     

       ).add_field(
        name='**GitHub**',
        value='https://github.com/Treyyyy0338/Globe-Token-Source-Files',
        inline=False




       
       ).add_field(
        name='**Youtube**',
        value='https://www.youtube.com/channel/UCjHyWxRTVaMFm5syeJrujDQ',
        inline=False


      
       ).add_field(
        name='**Telegram**',
        value='https://t.me/+8jKbQxRgRrwxYmJh',
        inline=False





      


        ).set_footer(
        text='Requested!',
        icon_url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_image(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'

        ).set_thumbnail(
        url='https://cdn.discordapp.com/avatars/694446165197979670/eb946325b85f913abdec645d0c14b98a.webp?size=1024'
        )

    await ctx.send(embed=embed)



@bot.command()
async def new(ctx):
     
        ticket_channel = await ctx.guild.create_text_channel(name=f":ticket-{ctx.author}") 
        await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)  
        
        guild = ctx.guild 
        rolesearch = discord.utils.get(guild.roles,  name="Ticket-Helper")
        await ticket_channel.set_permissions(rolesearch, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True, manage_channels=True)  
        
        await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False) 
   
        embed=discord.Embed(color=0xff8103)
        embed.add_field(name="Support Ticket", value=f"Ticket by {ctx.author.mention}", inline=False)
        embed.add_field(name="Option:", value=":lock: - ```^close - <#ticket>```", inline=False)
        embed.set_footer(text=f"Ticket | {ctx.author}")
        await ticket_channel.send(embed=embed)
        await ticket_channel.send(f"Hello, {ctx.author.mention} ! Please give us details upon your problem,  <@&897993774788128819> <@&898201303568752682> Will assist you keep in mind if we do not reply in time it is because one of us are busy, thankyou for understanding.  ") 


@bot.command()
@commands.has_permissions(manage_channels=True)
async def close(ctx, channel: discord.TextChannel): 

         await ctx.channel.delete()      

@bot.command()
@commands.has_permissions(administrator=True) 
async def setup(ctx):
           
        guild = ctx.guild
        await ctx.guild.create_role(name="Ticket-Helper", colour=discord.Colour(0xE03400)) 
        em=discord.Embed(title="Information", description="Ticket System was successfully installed. | Attention If you run ```^setup``` again, the ticket system will no longer work and report an error. Since there are there 2 roles of ticket helper you have to delete one then, color=0x00ff00")                                    
        await ctx.send(embed=em) 
           

        
@bot.command() 
async def tickethelp(ctx):
	       
        embed=discord.Embed(title="Help", description="```^new``` - Ticket create, ```^setup``` - Install Ticket System, ```^tickethelp``` - support ```^close <#ticket>``` - delete a Ticket", color=0x00ff00)                                                                                  
                                                   
        await ctx.send(embed=embed) 





















@bot.command(aliases=['c'])
@commands.has_permissions(kick_members= True)
async def purge(ctx,amount=2):
	await ctx.channel.purge(limit = amount)








bot.run('')
