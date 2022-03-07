#bearer_token = "AAAAAAAAAAAAAAAAAAAAAFZNXAEAAAAAtMxzwTqdmLPBE2maLziI%2BMZFyqc%3DPf8IraaOUhkjkLHzaUjiPgVgKKNHswY4bVEdWW67mBB6NKR9Te"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIRAWgEAAAAAjatIMs5ekMmgTxkWgzh2A5fq3xc%3DhNVEAe5pjUyEYRs37maD5Uui5aexMzWZIdVscEOQxB943IO4fb"

headers = {"Authorization": "Bearer {}".format(bearer_token)}

search_url = "https://api.twitter.com/2/tweets/search/all"