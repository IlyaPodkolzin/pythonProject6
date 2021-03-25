import vk_api
from vk_api import VkUpload


def main():
    vk_session = vk_api.VkApi(Login=LOGIN, password=PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()

    upload = VkUpload(vk)
    upload.photo(['static/image.jpg'], album_id=ALBUM_ID, group_id=GROUP_ID)


if __name__ == '__main__':
    main()
