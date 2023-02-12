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
user = mstdn.account_verify_credentials()

# collect favourites
posts = mstdn.favourites (limit = 40)

# if posts lenght equals or is greated than 40, remove the last 20
if len(posts) >= 40:
  posts = posts[20:40]

  for post in posts:
    print(post["url"])
    mstdn.status_unfavourite(post["id"])