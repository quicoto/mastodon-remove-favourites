#!/usr/bin/env python3
# encoding=utf8

import os
import argparse
from mastodon import Mastodon

# parse arguments
parser = argparse.ArgumentParser (description = 'Generate an HTML archive of a mastodon user.')
parser.add_argument ('--instance', required=True, help='url to your instance')
parser.add_argument ('--access-token', required=True, help='token providing access to your account')
args = parser.parse_args()

# connect to mastodon
mstdn = Mastodon(
		access_token = args.access_token,
		api_base_url = args.instance
		)

# collect favourites
posts = mstdn.favourites (limit = 40)

# Just keep the last 30 posts
if len(posts) >= 30:
  posts = posts[30:40]

  for post in posts:
    print(post["url"])
    mstdn.status_unfavourite(post["id"])
