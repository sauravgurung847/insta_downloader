import instaloader
import os

def download_post(url):
    print("Downloading:", url)

    loader = instaloader.Instaloader(download_comments=False, save_metadata=False)
    shortcode = url.split("/")[-2]  # extract shortcode like Cz8wzX3tCjN

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target="downloads")
        print("Download successful!")
        return True, f"{post.owner_username}_{post.date_utc}"
    except Exception as e:
        print("Error during download:", e)
        return False, str(e)
