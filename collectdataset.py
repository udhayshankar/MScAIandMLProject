
import tweepy
import os
from datetime import datetime, timedelta


API_KEY = 'xbSV9lslklEJL0WgKCLry9Moe'
API_KEY_SECRET = 'EKtJxEMeayuAPwGUdJvgslS4ChkrtHqvAsGpGbfmRyzj9ARTK1'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAAPrcwEAAAAATFz6hzNYHoLC8eZwXTfpfg6b91g%3DWFo7w5XAhKraUHMjVcpZFn5myhecOaUVdk2OO4ZsfKKmAFBRiY'
ACCESS_TOKEN = '1529447481024688129-yfjTQQLTchLruZ3gwL378LUq30aPW7'
ACCESS_TOKEN_SECRET = 'qtLThwT81Yacbi6LMXr0FjLRP9XfS1SWkY0LTwDGeEBR8'

screen_name = 'facebook'

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
#print(client)
user = client.get_user(username=screen_name)
#Retrieved the user id using the username(twitteraccountname)
print("username:",screen_name)
print(user.data.id)
user_id = user.data.id
#place_fields = ['United States']
#contained_within,country,country_code,full_name,geo,id,name,place_type
#obj = client.get_users_mentions(user_id,max_results=100,tweet_fields=['context_annotations','created_at','geo'],expansions='geo.place_id',place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'])
#obj = client.get_users_mentions(user_id,tweet_fields=['context_annotations','created_at','geo'],expansions='geo.place_id',place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'])
#print(obj)


# tweets = None # initial case
# mentions_list = []
# next_token = None

# dtformat = '%Y-%m-%dT%H:%M:%SZ'
# time = datetime.utcnow()
# start_time = time - timedelta(6*30)
# end_time = time - timedelta(seconds=15)

# start_time, end_time = start_time.strftime(dtformat), end_time.strftime(dtformat)

# print(start_time)
# print(end_time)
# tweets = client.get_users_mentions(user_id,start_time=start_time,end_time=end_time,
#     tweet_fields = ['attachments','author_id','context_annotations','conversation_id','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source','text','withheld'],
#     expansions=['attachments.media_keys','attachments.poll_ids','author_id','entities.mentions.username','geo.place_id,''in_reply_to_user_id','referenced_tweets.id','referenced_tweets.id.author_id'],
#     media_fields=['alt_text','duration_ms','height','media_key','preview_image_url','public_metrics','type','url','variants','width'],
#     poll_fields=['duration_minutes','end_datetime','id','options','voting_status'],
#     user_fields=['created_at','description','entities','id','location','name','pinned_tweet_id','profile_image_url','protected','public_metrics','url','username','verified','withheld'],
#     place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'])

# print(tweets[0])







