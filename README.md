# Slash Twitter: a Twitter bot for reposting Reddit

The run the bot is run on Heroku, and you needs Developer API keys from [Twitter](https://developer.twitter.com/en/portal/dashboard) and [Reddit](https://www.reddit.com/prefs/apps).

## Deploy from Github
The project can be deployed straight from Github to Heroku. After linking the repo [here](https://dashboard.heroku.com/apps/slash-succulents/deploy/github), deploy it manually on the 'Manual deploy' section.

## Set up Heroku Config Vars
On the project page, go to Settings tab, and click on 'Reveal Config Vars'. After that, you have to set the following fields

1. REDDIT_KEY
2. REDDIT_SECRET
3. REDDIT_SUBREDDIT
4. TWITTER_KEY
5. TWITTER_SECRET
6. TWITTER_ACCESS_TOKEN
7. TWITTER_TOKEN_SECRET
8. TWITTER_USERNAME

## Set up Scheduler
On the main page of the Heroku project, click on 'Configure Add-ons', and add 'Heroku Scheduler' to the project. Configure the scheduler by clicking 'Add job', and choose how often do you want the bot to run, the 'Run command' should be set to `python main.py`.
