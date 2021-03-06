from discord.ext import commands
import os
import traceback

# インストールした discord.py を読み込む
#import discord
import random
import string
import datetime

# 接続に必要なオブジェクトを生成
client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
# ランダムな英数字を取得する関数
def GetRandomStr(num = 4):
     # 英数字をすべて取得
     dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
     # 英数字からランダムに取得
     return ''.join([random.choice(dat) for i in range(num)])

# メッセージ受信時に動作する処理
@client.event
async def on_message(message, number = 1):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # 「project」と発言したらprojectのナンバーを発行する。
    if message.content == 'project' or message.content == 'Project' or message.content == 'PROJECT':
        # 日付取得
        y = 0
        today = datetime.date.today()
        y = today.strftime("%Y%m%d")
        # ランダムな英数字取得
        z = 0
        num = 4
        z = GetRandomStr(num)
        await message.channel.send('あなたのプロジェクトのプロジェクトIDは%s%sです。' % (y,z))
        await message.channel.send('下記URLにアクセスしてOKRのフォームを埋めてください。')
        await message.channel.send('https://forms.gle/D1RHXmdNaZwbXhsP7')
        print('あなたのプロジェクトのプロジェクトIDは%s%sです。' % (y,z))
        print('下記URLにアクセスしてOKRのフォームを埋めてください。')
        print('https://forms.gle/D1RHXmdNaZwbXhsP7')
        # print('%d' % number)
        # number = number + 1
        # return number


bot.run(token)
