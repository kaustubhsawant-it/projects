import tweepy as tw
import pandas as pd
import streamlit as st
import time

st.write("Starting app...")

# Twitter client
client = tw.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAMdx3QEAAAAAxWPHmeHgerw4kTsFJAkbjPJ1m1g%3DSqiAGUQyhM3hFxa5O0ykhMPNDy4H2JeYMdFOV2qz8ArWGzhtXw')

@st.cache_data
def get_tweets(query, limit=50):
    st.write(f"Running get_tweets with query='{query}', limit={limit}")
    tweets = []

    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=min(limit, 100),
            tweet_fields=['created_at', 'author_id', 'text'],
            expansions=['author_id'],
            user_fields=['username']
        )

        if response.data is None:
            st.warning("No tweets found.")
            return pd.DataFrame(columns=['Date', 'UserName', 'Tweet'])

        users = {u['id']: u for u in response.includes['users']}

        for tweet in response.data:
            user = users.get(tweet.author_id)
            tweets.append([
                tweet.created_at,
                user.username if user else "Unknown",
                tweet.text
            ])

        df = pd.DataFrame(tweets, columns=['Date', 'UserName', 'Tweet'])
        st.success(f"Pulled {len(df)} tweets.")
        return df
    
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame(columns=['Date', 'UserName', 'Tweet'])
    
# Show loading text
st.write("Running get_tweets...")
df = get_tweets("OpenAI", limit=20)
st.write("Done fetching.")
st.dataframe(df.head())
