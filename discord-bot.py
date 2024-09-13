# bot.py
import os
from datetime import datetime
from discord.ext import tasks
import discord
import aiocron
import asyncio
from sleeper.sleeper import get_nfl_state
from slothstats.slothstats import SlothstatsDownloader
import random

jabs = ["Let's Go Steelers!",
"Ravens Suck!",
"Jeremy is the greatest fantasy player of all-time.",
"Justin Herbert is overrated.",
"Y'all don't know shit about football.",
"Jamar Chase isn't rosterable, you should probably drop him.",
"The Bills really went into the season with Curis Samuel as their top reciever.",
"Daniel Jones is worse at his job than you.",
"There are no players in the NFL that are better than TJ Watt.",
"The Clevland Browns. LOL."
]

@tasks.loop(hours = 1)  
async def cronjob():
    '''Asyncio task that runs once an hour, checks if the hour is 8 am and it's a weekday m-f, then sends
      a 'good morning' message to the configured channel'''

    def run_job():
        now = datetime.now()
        weekday = now.weekday()
        hour = now.time().hour
        return weekday == 1 and hour == 8  
  
    if run_job():
        nfl_state = get_nfl_state()
        # NFL season has started and there have been scores recorded
        if nfl_state['season_has_scores'] and nfl_state['week'] >= 2 and nfl_state['week'] <= 17  and nfl_state['seson_type'] == 'regular':
            downloader = SlothstatsDownloader(league_id=1074391942395428864, start_week=1, end_week=nfl_state['week'])
            c = bot.get_channel(CHANNEL_ID)
            embed = discord.Embed()
            embed.description = f'''
            Well, well, well, it looks like week {nfl_state['week'] - 1} is in the books.

            Please bear with me, I may not be very smart now, but 
            I am looking to get smarter over the course of the season.

            In the meantime, I've comiled a custom report for you, and remember:
            {random.choice(jabs)}
            
            [Slothstats Report]({downloader.url}).
            '''
            await c.send(embed=embed)



cronjob.start()
bot.run(TOKEN)