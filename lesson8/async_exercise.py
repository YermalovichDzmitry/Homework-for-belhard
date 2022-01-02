import requests
import json
import time
import asyncio
import aiohttp


async def make_request(resource):
    async with aiohttp.ClientSession() as sess:
        async with sess.request('GET', f'https://jsonplaceholder.typicode.com/{resource}/') as req:
            return await req.text()


def merge_albums_photos(albums: dict, photos: dict):
    new_albums = []
    for album in albums:
        album.update({'list of photos': []})
        for photo in photos:
            if photo.get('albumId') == album.get('id'):
                album['list of photos'].append(photo)
        new_albums.append(album)

    return new_albums


def merge_posts_comments(posts: dict, comments: dict):
    new_posts = []
    for post in posts:
        post.update({'list of comments': []})
        for comment in comments:
            if comment.get('postId') == post.get('id'):
                post['list of comments'].append(comment)
        new_posts.append(post)
    return new_posts


def merge_users_all(users: dict, albums: dict, todos: dict, posts: dict):
    new_users = []
    for user in users:
        user.update({'list of albums': []})
        user.update({'list of todos': []})
        user.update({'list of posts': []})
        for album in albums:
            if album.get('userId') == user.get('id'):
                user['list of albums'].append(album)
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                user['list of todos'].append(todo)
        for post in posts:
            if post.get('userId') == user.get('id'):
                user['list of posts'].append(post)
        new_users.append(user)
    return new_users


async def get_data():
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


start = time.time()
users, albums, photos, comments, todos, posts = asyncio.run(get_data())
print(time.time() - start)

albums_with_photos = merge_albums_photos(albums, photos)
posts_with_comments = merge_posts_comments(posts, comments)
update_users = merge_users_all(users, albums_with_photos, todos, posts_with_comments)