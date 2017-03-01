import soundcloud

client = soundcloud.Client(access_token="a valid access token")
track = client.get('/tracks/293/stream', allow_redirects=False)
print track.location
