import tweepy
import time

CK = 'lYmOgnfRS2ywnzfxe0fsZuq9T'
CS = 'eygpWTseCd5tAJW5myrLqhkWLQF91Bf8aMx5pKMVUNbjv9f0ct'
AC = '1237118674177347584-CZrQRedZ1CK1LsEUIPTdOBK5FpbIyA'
AS = 'GAwFqXIF1Y7s4weZaIHStnzfU3UZO1Gh6AqyglDnWdokp'
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AC, AS)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search='Insira aqui a palavra que deseja que o bot procure'
numero = 10000000

for tweet in tweepy.Cursor(api.search,search).items(numero):
    try:
        if((tweet.text)=='Insira aqui a palavra que deseja que o bot procure'):
            print("Nome do usuário: @" + tweet.user.screen_name)
            api.update_status("@" + tweet.user.screen_name + " Insira aqui a mensagem que o bot vai enviar", in_reply_to_status_id=tweet.id)
            print("Tweet enviado corretamente")
            time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        