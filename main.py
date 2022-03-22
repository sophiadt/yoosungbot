import discord
import os
import random

#lets bot run offline from replit for an hour
from stay_alive import stay_alive # or whatever you named your file and function
stay_alive() # call the function

intents=intents=discord.Intents.all()
client = discord.Client(intents=intents)

#shows if bot is connected
@client.event
async def on_ready():
  print("Connected\n")
  print(client.user)

#generates greeting if new member joins server
@client.event
async def on_member_join(member):
  #yoosung dms welcome server message
  await member.create_dm()
  await member.dm_channel.send(
    f'I was waiting for you to log on, {member.name}.')

#bot outputs random quote if user inputs assigned message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  yoosung_quotes = [
    'Rank #2 Superman Yoosung is currently playing LOLOL!',
    'I hope the event shines bright enough for Rika to notice from up there.',
    'I want to go see a romance movie with my girlfriend too ;_;',
    (
    '5 more mins... '
    'let me sleep more... '
    'professor...'
    ),
    'Would I seem more mature if I drink three cups of coffee a day?',
    'Don\'t tell me•••. u haven\'t slept because u were also playing LOLOL?',
    'Rika, I miss you.',
    'Rika, I’m sure you’re watching us from up there, right?',
    'Good deed of the day: wasn’t late for class!',
    'I wish I could just start all over again in real life… Life is sometimes too cruel for me.',
    'I feel guilty about not getting the temperature right for my spaghetti yesterday :(',
    'I’m lonely. When will my girlfriend come to me?',
    'Gonna make sure the planting\’s perfect today! I wanna be a sensitive man.',
    'I miss him… the boss monster.',
    'LOLOL L…..o….l…ol….',
    'Chocolate milk is the tastiest milk of all!',
    'S;ecret bossss monsterrere cgeeettt himmm',
    'z…zz…so….sleep…y……',
    'What in the world is the secret ingredient for the cafeteria\’s kimchi fried rice? Such a mystery…',
    'Bobby pins for my bangs should always go W/W this first and then WWWW this.',
    'I heard your wishes come true if you blow on a dandelion!',
    'I\’ll make sure my girlfriend never gets her hands wet! Hmm, but how will she wash her face then?',
    'LOLOL! I! WILL! BREAK! THE! QUEST!',
    'Everyday was so fun when I was little. When did I grow up so much?',
    'This beef stew only has onions :( Whyyyyy',
    'I totally ruled over that round just now. I should have recorded it… ;_;',
    'I like candy better than cigarettes. And what\’s better than candy is LOLOL! LOLOL!',
    'Our savior, defender of Justice, Red!...Huh…? This isn’t it…',
    'Se…ven…. Sofa… Honey Buddha…chi…ps… Smell….zzz',
    'Should I tie my hair like Zen? Man bun?',
    '…I honestly think I\’m handsome too.',
    'The bridge of love? Oh! A super fun event is opening today where I have to cross the LOLOL bridge!',
    'If someone suggest that I go pro playing LOLOL, I\’ll pretend to consider it!',
    'Romance like those in movies. That doesn’t sound too bad, does it?',
    'Should I make bento boxes for the body guards',
    'Ooh, some guy in a tv show is getting slapped with kimchi!! I wonder how that feels like.',
    'I know how to brew coffee too…',
    'If I think about it, the professor’s just giving out quests. Then why do I hate assignments so much?',
    'Next time I go home, I should bring gifts for mom and dad. I should call my sister.',
    'Should I make some snacks for fun?',
    'Schedule check, textbooks check, face check, messenger check! Hehe!',
    'I think spring is finally here in my heart!',
    'I feel like my cloudy vision\'s been cleared.',
    'Should I make a bento box with rice shaped like Elizabeth 3rd? Alright, a challenge it is!',
    'Ugh... my head. hurts... :(',
    'I can do it. I can do it. No, I must do it.',
    'I\'m always ready to do whatever for you.',
    'I\’m going to protect you in the real world, not in LOLOL.',
    'There is only one person I want to see right now.',
    'I don’t regret my choices.',
    'Smile for me the day we meet.',
    'It\'s so yummy to dip thin crusted pizza in honey! So delish!',
    'When my rank drops in LOLOL, I feel angry at first, then sad...',
    'Got an A on PE! Now I can tell people gaming doesn\'t affect my strength.',
    'God the champion skin is so expensive!!! But of course I\'m buying it!! Gotta go purchase more coins...',
    'Who made my sche...dule... this way....? Oh... me.',
    'I tried on a police uniform in a career convention before, and honestly I looked good. I should have taken a photo.',
    'I need to make kimbap for the picnic, but I don\'t have any of the ingredients!',
    'Seven\'s hoodie seems kind of cool for some reason... Maybe I should ask for one.',
    'The king has donkey ears!!! God, so out of control....',
    'One must be very careful when getting a pet... Very, very careful!!!',
    'Elizabeth 3rd\'s tail is amazing... It expanded like a peacock when I got close to her!',
    'I feel like I\'ll end up dying if Elizabeth runs away again.',
    'Elizabeth 3rd is so fluffy. Jumin must take really good care of her.',
    'Where did I put my bobby pin?!! Today\'s an important day!!',
    'I have to stretch my fingers before going to bed! So that I can play LOLOL as soon as I wake up tomorrow!',
    'Maybe I should try folding origami cranes again. I don\'t want to be single! A thousand cranes will get me a girlfriend!',
    'Does blood type really have nothing to do with personality? Even for compatibility?',
    'I don\'t want just the results to belittle my efforts.',
    'You must show your sense of responsibility with actions not words.',
    'I heard you can only give no-sodium cottage cheese to dogs.',
    'If the RFA leader changes... would I feel better?',
    'Anger doesn\'t help with battles in LOLOL. I must remain collected.',
    'LOLOL always gives me an answer if I solve the quest...',
    'Men can cry when their sad. We can cry too ;_;',
    'Everything seemed bright when I was little... I feel like the sky and ground are colliding.',
    'We should all talk to each other more. We have to be honest.',
    'Ugh.... God... My stomach... my guts... are spinning....',
    'I am going to be a more reliable person!',
    'I hear someone uses the recordings of philosophy classes a s a lullaby... what a smart guy.',
    'I\'ll sincerely do all my assignments for classes starting... tomorrow!',
    'When shall I dye my hair roots?',
    'Ahem!! Ahem!! AAAAAAAAA!! Throat clearing...,',
    'When is the application for clubs due?',
    'The hairpin sold on the streets just now... looked pretty good...',
    'There\'s an assignment due till this week... which class was it?',
    'Should I buy a new gaming keyboard...',
    'I\'ll give up this semester and try better in the next. This cycle!!',
    'Can I trust this self-diagnosis of depression?',
    'Zen looks so cool on his bike... but I probably can never ride one TT.',
    'There\'s a workout schedule stuck on Zen\'s fridge.',
    'Still, better to be with Zen than being alone... OMG stop nagging!',
    'I should let the world know about LOLOL.',
    'I can\'t touch my toes...I should work to regain flexibility...',
    'I don\'t think I\'ll grow taller...will I?',
    'I\'m thirsty... want to drink milk...',
    'I want to cry out so hard that I blank out...',
    'If I could rewind time... I think I thought about this like a few thousand times now...',
    'What could I have done?',
    'Should I start LOLOL over with a new account...?',
    'My hair pin keeps falling off..I should by new one but exactly the same.',
    'I want to write poems when my melancholy emotions are its peak.',
    'I want to live by only eating, sleeping and gaming...',
    'Professors who give out group assignments are evil!',
    'Darkness... deep... emptiness... solitude... LOLOL...',
    'Someone just now said my hair looked like a star...',
    'Think it\'s time to change my phone',
    'I want to do more but I think I\'m not competent enough...',
    'Is there an evil group out there trying to take out RFA? Like in the animations?',
    'I dry-cleaned this to wear at the party...',
    'I need time a time out to heal my mind...',
    'Thought Zen was a celebrity',
    'My hands are cold... I want hot chocolate...',
    'Just how many subordinates does the agency have? The comments sections for articles are horrible...',
    'Am I really a grown-up...? I should\'ve been humble. I\'d thought I\'m more mature than Zen...',
    'Did you sleep well?',
    'Come and chat with us! Pretty plz?',
    'Cooking Breakfast: Success!',
    'To go to class or to play LOLOL, that is the question.',
    'I hope the cafeteria serves only the good stuff today!',
    'I\'m so curious about what u r doing right now!',
    'Are you feeding yourself at the right times? Starving isn\'t good for you...',
    'Let\'s go shop for cooking ingredients!',
    'Gonna play LOLOL as soon as I finish this assignment!',
    'I\'ll do my assignment after playing a game for an hour.',
    'Wow! A meteor just fell from the sky!',
    'Yawn•••sleepy•••',
    'You\'ve come, the lonesome party coordinator. My day was spent circling around the swamp of emptiness.',
    'Did u look at the time? Time slipped by without me realizing',
    'Don\'t stay up too late.',
    'Don\'t tell me•••. u haven\'t slept because u were also playing LOLOL?',
    'OMG. Did you log in behind the hacker\'s back?',
  ]

  if message.content == 'yoosung~' or message.content == 'Yoosung~' or message.content == 'YOOSUNG~':
    response = random.choice(yoosung_quotes)
    await message.channel.send(response)

my_secret = os.environ['DISCORD_BOT_SECRET']
client.run(my_secret)
