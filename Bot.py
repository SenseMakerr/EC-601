import botometer

rapidapi_key = "293e7643edmsh06c442315e9cf67p1e5ccfjsn714636e880a6"
twitter_app_auth = {
    'consumer_key': 'XwK3IS0ldbT4FZ5fYLbZ3wDnU',
    'consumer_secret': 'ytl8OhWaR1xGyO43JC0nfHkOD3e6SjghgKq7t5FVebYaee1zaM',
    'access_token': '1579831536119156741',
    'access_token_secret': 'lnLf5QuTKqZp7PktjzRHlpOqdYTdQsiRO9VVT4QZ80Vt6',
}

blt_twitter = botometer.BotometerLite(rapidapi_key=rapidapi_key, **twitter_app_auth)

# Prepare a list of screen_names you want to check.
screen_name_list = ['yang3kc', 'onurvarol', 'clayadavis']
blt_scores = blt_twitter.check_accounts_from_screen_names(screen_name_list)

# Prepare a list of user_ids you want to check.
user_id_list = [ 353534334, 34535343566, 3457764563]
blt_scores = blt_twitter.check_accounts_from_user_ids(user_id_list)