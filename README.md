# Dad Joke Twitter Bot

## Overview
Gets a dad joke from the *icanhazdadjoke* API and posts it on Twitter under [@DadJokesAlways](https://twitter.com/DadJokesAlways) using *Twitter* API

## Example Tweet
Dad Jokes
@DadJokesAlways
#1: My boss told me to attach two pieces of wood together... I totally nailed it!

## Logic Flow
1. Gets Twitter credentials (consumer key, consumer secret, api token, api token secret) from local text file.
2. Requests a dad joke from icanhazdadjoke API
3. Determines tweet number based on local storage file
4. Posts dad joke to [@DadJokesAlways](https://twitter.com/DadJokesAlways) Twitter account.

## Used
1. Python
2. Requests
3. Twitter API
4. icanhazdadjoke API
