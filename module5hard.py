class Database:
    def __init__(self):
        self.users = {}
        self.videos = {}

    def add_user(self, username, password, age):
        self.users[username] = password
        self.users[username + '_age'] = age

    def add_video(self, title, duration, time_now, adult_mode):
            self.videos[title] = duration
            self.videos['time_now_' + title] = time_now
            self.videos['adult_mode_' + title] = adult_mode







class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user


    def log_in(self, nickname, password):
        if  self.users[nickname] == hash(str(password)):
            self.current_user = nickname
            print(f'Текущий пользователь - {self.current_user}')
        else:
            print(f'Текущий пользователь не изменилось - {self.current_user}')

    def register(self, nickname, password, age):
        if self.users.get(nickname) is None:
            database.add_user(nickname, password, age)
            print(f'Пользователь с именим {nickname} добавлено!')
        else:
            print(f'Пользователь с именим {nickname} существует!')

    def log_out(self):
        self.current_user = None
        print(self.current_user)

    def add(self, title, duration, time_now = 0, adult_mode = False ):
        if self.videos.get(title) is None:
            database.add_video(title, duration, time_now, adult_mode)
        else:
            print('Видео с таким именем существеут')

    def get_videos(self, title):
        title1 = list(self.videos.keys())
        for i  in range(0, len(title1)):
            if title.lower() in title1[i].lower():
                print(f'полученный фильм {title}')






database = Database()

user1 = User('gafurjan', 123, 40)
user2 = User('gulguncha', 123, 30)
user3 = User('muslima', 123456, 6)
user4 = User('muhammadsadyk', 123, 4)

database.add_user(user1.nickname, user1.password, user1.age)
database.add_user(user2.nickname, user2.password, user2.age)
database.add_user(user3.nickname, user3.password, user3.age)
database.add_user(user4.nickname, user4.password, user4.age)


video1 = Video('1+1', 36000)
video2 = Video('Spartac', 36000)
video3 = Video('Побег', 36000)

database.add_video(video1.title, video1.duration, video1.time_now, video1.adult_mode)
database.add_video(video2.title, video2.duration, video2.time_now, video2.adult_mode)
database.add_video(video3.title, video3.duration, video3.time_now, video3.adult_mode)

urtube = UrTube(database.users, database.videos, 'gafurjan')

urtube.log_in('gafurjan', 123)

# urtube.register('Gaffur', 1245, 41)

urtube.log_out()

urtube.add('Спрут', 3600)
print(database.videos)

urtube.get_videos('Спрут')









