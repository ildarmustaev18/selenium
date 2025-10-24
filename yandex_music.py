from yandex_music import Client

client = Client()
client.init()


client.users_likes_tracks()[0].fetch_track().download('example.mp3')
client = Client('e8616167-c466-41fb-b823-0996b2f72b2a').init()
