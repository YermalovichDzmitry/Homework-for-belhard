import requests
import json
import time
import asyncio
import aiohttp
import argparse


async def make_request(resource):
    async with aiohttp.ClientSession() as sess:
        async with sess.request('GET', f'https://jsonplaceholder.typicode.com/{resource}/') as req:
            return await req.text()


def merge_albums_photos(albums: dict, photos: dict):
    new_albums = []
    for album in albums:
        album.update({'photos': []})
        for photo in photos:
            if photo.get('albumId') == album.get('id'):
                album['photos'].append(photo)
        new_albums.append(album)

    return new_albums


def merge_posts_comments(posts: dict, comments: dict):
    new_posts = []
    for post in posts:
        post.update({'comments': []})
        for comment in comments:
            if comment.get('postId') == post.get('id'):
                post['comments'].append(comment)
        new_posts.append(post)
    return new_posts


def merge_users_all(users: dict, albums: dict, todos: dict, posts: dict):
    new_users = []
    for user in users:
        user.update({'albums': []})
        user.update({'todos': []})
        user.update({'posts': []})
        for album in albums:
            if album.get('userId') == user.get('id'):
                user['albums'].append(album)
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                user['todos'].append(todo)
        for post in posts:
            if post.get('userId') == user.get('id'):
                user['posts'].append(post)
        new_users.append(user)
    return new_users


# Асинхронная выгрузка
async def get_data_not_sync():
    data = await asyncio.gather(
        make_request("users"),
        make_request("albums"),
        make_request("photos"),
        make_request("comments"),
        make_request("todos"),
        make_request("posts")
    )
    json_data = [json.loads(item) for item in data]
    users, albums, photos, comments, todos, posts = json_data
    return users, albums, photos, comments, todos, posts


# Синхронная выгрузка
async def get_data_sync():
    users = await make_request("users")
    albums = await make_request("albums")
    photos = await make_request("photos")
    comments = await make_request("comments")
    todos = await make_request("todos")
    posts = await make_request("posts")
    json_data = [json.loads(item) for item in [users, albums, photos, comments, todos, posts]]
    users, albums, photos, comments, todos, posts = json_data
    return users, albums, photos, comments, todos, posts


def get_data(request, data):
    request = request.split("/")
    request = request[1:]
    if len(request) == 1 and request[0] == "users":
        print(data)
        return 0
    elif request[0] == "users":
        data = data[int(request[1]) - 1]
        print(data[request[2]])
        return 0
    else:
        for user in data:
            for item in user[request[0]]:
                if item['id'] == int(request[1]):
                    print(item[request[2]])

        return 0


start = time.time()
users, albums, photos, comments, todos, posts = asyncio.run(get_data_not_sync())
print(time.time() - start)

# start = time.time()
# users, albums, photos, comments, todos, posts = asyncio.run(get_data_sync())
# print(time.time() - start)

'''
Асинхронная выгрузка выгружает данные быстрее чем синхронная.
'''
parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
args = parser.parse_args()

albums_with_photos = merge_albums_photos(albums, photos)
posts_with_comments = merge_posts_comments(posts, comments)
update_users = merge_users_all(users, albums_with_photos, todos, posts_with_comments)
get_data(args.path, update_users)
