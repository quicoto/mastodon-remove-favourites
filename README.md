# Mastodon remove favourites

Periodically removes old favourites using the great [Mastodon.py](https://github.com/halcy/Mastodon.py)

It tries to queries 40 favourites, if you have 40 or more it will cut 10 off and unfavourite them. You will be always left with 30 favourited posts.

This is just an experiment to keep the user's account lean of favourites, just keep the most recent.

## How to setup

1. Create an application access token in Mastodon with `read:favourites` and `write:favourites` permissions
2. Create a repository secret called `ACCESS_TOKEN` with that value
3. Create a repository secret called `INSTANCE` with your Mastodon instance URL (eg. `https://ricard.social`)
