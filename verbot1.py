veraccepted = "Your verification has been accepted. Now, there will be one more part of this, conducted by the server staff."
verdenied = "Your verification has been denied; you will be banned from the server promptly."
verinvalid = "Sorry, your answer is invalid. Please use -verifyme to restart the verification"
verrules = "Please go read the rules, and do -verifyme again to restart verification."


def cont():
    import discord
    from discord.ext import commands
    import datetime

    from urllib import parse, request
    import re

    bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command()
    async def sum(ctx, numOne: int, numTwo: int):
        await ctx.send(numOne + numTwo)

    @bot.command()
    async def info(ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="This is the MCfriends Minecraft Java Edition official discord server.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
        embed.add_field(name="GingAle", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        # embed.set_thumbnail(url=f"{ctx.guild.icon}")
        embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

        await ctx.send(embed=embed)

    @bot.command()
    async def youtube(ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        # print(html_content.read().decode())
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
        print(search_results)
        # I will put just the first result, you can loop the response to show more results
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    # Events
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="MCfriends Verification", url="https://discord.gg/v8ttcw4qFm"))
        print('The verification bot is active')


    @bot.listen()
    async def on_message(message):
        if "-verifyme" in message.content.lower():
            await message.channel.send("Answer the following questions with -yes or -no")
            await bot.process_commands(message)
            await message.channel.send ("1. Did you read the rules? If not, go to the rules channel to read them.")
           	if ("-yes") in message.content.lower:
              await message.channel.send ("2. Do you treat everyone with respect, despite of race, ethnicity, culture, and any other differences?")
            	if ("-yes") in message.content.lower:
               await message.channel.send ("3. Do you support the LGBTQTA+ Community?")
               if ("-yes") in message.content.lower:
                 await message.channel.send ("4. Will you commit to reporting anyone who breaks any rules to the staff, including players you befriend?")
                 if ("-yes") in message.content.lower:
                    await message.channel.send (veraccepted)
                 elif ("-no") in message.content.lower:
                   	await message.channel.send (verdenied)
                 else:
                   	await message.channel.send (verinvalid)
                elif ("-no") in message.content.lower:
                  await message.channel.send (verdenied)
               	else:
                 await message.channel.send (verinvalid)
                  
              elif ("-no") in message.content.lower:
              	await message.channel.send (verdenied)
              else:
                await message.channel.send (verinvalid)
        	   elif ("-no") in message.content.lower:
             await message.channel.send (verrules)
             else:
              await message.channel.send (verinvalid)

              
    bot.run('') #insert token here

cont()
