import instaloader
from urllib.parse import urlparse

##################### inputs ####################################
url = input("Enter instagram URL: ")
################### END #########################################

def extract_shortcode(instagram_url):
    """
    Extracts the shortcode from an Instagram post/reel/IGTV URL.
    """
    try:
        parts = instagram_url.strip('/').split('/')
        if 'p' in parts or 'reel' in parts or 'tv' in parts:
            index = next(i for i, part in enumerate(parts) if part in ['p', 'reel', 'tv'])
            return parts[index + 1]
        else:
            print("Unsupported or invalid Instagram URL format.")
            return None
    except Exception as e:
        print(f"Error extracting shortcode: {e}")
        return None

def download_instagram_content(instagram_url):
    """
    Downloads content (post, reel, IGTV) from an Instagram URL.
    """
    shortcode = extract_shortcode(instagram_url)
    if not shortcode:
        print("Failed to extract shortcode.")
        return

    print(f"\nShortcode: {shortcode}")
    loader = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target='downloaded_content')
        print(f"Downloaded content from shortcode: {shortcode}")
    except Exception as e:
        print(f"Error downloading content: {e}")

# Example usage
download_instagram_content(url)