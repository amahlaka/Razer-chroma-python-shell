import requests
import threading, time
api_endpoint = "http://localhost:54235/razer/chromasdk"



init_obj = {
    "title": "Razer Chroma SDK RESTful Test Application",
    "description": "This is a REST interface test application",
    "author": {
        "name": "Chroma Developer",
        "contact": "www.razerzone.com"
    },
    "device_supported": [
        "keyboard",
        "mouse",
        "headset",
        "mousepad",
        "keypad",
        "chromalink"],
    "category": "application"
}

resp = requests.post(api_endpoint, json=init_obj)
resp.json()['uri']

class Razer_api_session():
    keepalive = True
    session_id = None
    session = None
    beat_count = None
    api_uri= None
    def __init__(self):
        init_api_response = requests.post(api_endpoint, json=init_obj)
        self.session_id = init_api_response.json()['sessionid']
        self.api_uri = init_api_response.json()['uri']
        self.session = requests.Session()
        self.session.post(self.api_uri)
        self.keepalive = True

    
    def heartbeat(self):
        self.heartbeat_uri = self.api_uri+"/heartbeat"
        print(self.heartbeat_uri)
        while self.keepalive is True:
            resp = requests.put(self.heartbeat_uri)
            self.beat_count = resp.json()['tick']
            time.sleep(5)
        print("keepalive is false, loop stopped")
        return




color_test = {
    "effect": "CHROMA_STATIC",
    "param": {
        "color": 0
    }
}

color_test2 = {
    "effect":"CHROMA_CUSTOM_KEY",
    "param":{
        "color":[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "key":[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    }
}

test = {'ESC': [0, 1], 'F1': [0, 3], 'F2': [0, 4], 'F3': [0, 5], 'F4': [0, 6], 'F5': [0, 7], 'F6': [0, 8], 'F7': [0, 9], 'F8': [0, 10], 'F9': [0, 11], 'F10': [0, 12], 'F11': [0, 13], 'F12': [0, 14], 'PRT_SC': [0, 15], 'SCR_LK': [0, 16], 'PAUSE': [0, 17], 'UNUSED': [0, 18], 'UNSD': [0, 19], 'LOGO': [0, 20], 'MACRO_1': [1, 0], 'SECTION': [1, 1], '1': [1, 2], '2': [1, 3], '3': [1, 4], '4': [1, 5], '5': [1, 6], '6': [1, 7], '7': [1, 8], '8': [1, 9], '9': [1, 10], '0': [1, 11], '+': [1, 12], 'TILDA': [1, 13], 'BACKSPACE': [1, 14], 'INSERT': [1, 15], 'HOME': [1, 16], 'PAGE_UP': [1, 17], 'NUM_LK': [1, 18], 'DIVIDE': [1, 19], 'MULTIPLY': [1, 20], 'MINUS': [1, 21], 'MACRO_2': [2, 0], 'TAB': [2, 1], 'Q': [2, 2], 'W': [2, 3], 'E': [2, 4], 'R': [2, 5], 'T': [2, 6], 'Y': [2, 7], 'U': [2, 8], 'I': [2, 9], 'O': [2, 10], 'P': [2, 11], 'Å': [2, 12], '^': [2, 13], "'": [2, 14], 'DEL': [2, 15], 'END': [2, 16], 'PAGE_DOWN': [2, 17], 'NUM_7': [2, 18], 'NUM_8': [2, 19], 'NUM_9': [2, 20], 'NUM_PLUS': [2, 21], 'MACRO_3': [3, 0], 'CAPS_LOCK': [3, 1], 'A': [3, 2], 'S': [3, 3], 'D': [3, 4],
        'F': [3, 5], 'G': [3, 6], 'H': [3, 7], 'J': [3, 8], 'K': [3, 9], 'L': [3, 10], 'Ö': [3, 11], 'Ä': [3, 12], 'MYSTERY': [3, 13], 'ENTER': [3, 14], 'UNKWN': [3, 15], 'BLANK': [3, 16], 'EMPTY': [3, 17], 'NUM_4': [3, 18], 'NUM_5': [3, 19], 'NUM_6': [3, 20], 'NUM_UNKWN': [3, 21], 'MACRO_4': [4, 0], 'L_SHIFT': [4, 1], '<': [4, 2], 'Z': [4, 3], 'X': [4, 4], 'C': [4, 5], 'V': [4, 6], 'B': [4, 7], 'N': [4, 8], 'M': [4, 9], ',': [4, 10], '.': [4, 11], '_': [4, 12], 'UNKWN_s': [4, 13], 'R_SHIFT': [4, 14], 'EMPTY_2': [4, 15], 'UP': [4, 16], 'BLANK_2': [4, 17], 'NUM_1': [4, 18], 'NUM_2': [4, 19], 'NUM_3': [4, 20], 'NUM_ENTER': [4, 21], 'MACRO_5': [5, 0], 'L_CTRL': [5, 1], 'WINDOWS': [5, 2], 'L_ALT': [5, 3], 'SPACE_UNKWN': [5, 4], 'SPACE_UNKWN2': [5, 5], 'SPACE_UNKWN3': [5, 6], 'SPACEBAR': [5, 7], 'SPACE_UNKWN4': [5, 8], 'SPACE_UNKWN5': [5, 9], 'SPACE_UNKWN6': [5, 10], 'ALT_GR': [5, 11], 'FN': [5, 12], 'LIST': [5, 13], 'R_CTRL': [5, 14], 'LEFT': [5, 15], 'DOWN': [5, 16], 'RIGHT': [5, 17], 'RIGHT_2': [5, 18], 'NUM_0': [5, 19], 'NUM_DEL': [5, 20], 'NUM_UNK3': [5, 21]}
from cmd import Cmd


def set_WASD(color_scheme):
    scheme = color_scheme
    wasd=['W','A','S','D']
    color=getIfromRGBReverse([255,0,0])
    for key in wasd:
        scheme = set_color(key,color,scheme)
    return scheme


def get_colors(ind):
    index=test[ind]
    keys=color_test2['param']['key']
    value=keys[index[0]][index[1]]
    print(value)


def find_key(row, column):
    new_color = color_test2
    new_color['param']['key'][int(row)][int(column)] = ~16776960
    return new_color

def set_color(key, color_rgb, original_color):
    print(color_rgb)
    index=test[key]
    new_color = original_color
    new_color['param']['key'][index[0]][index[1]] = ~color_rgb
    return new_color

def getIfromRGB(rgb):
    print(rgb)
    red = rgb[2]
    green = rgb[1]
    blue = rgb[0]
    RGBint = (red<<16) + (green<<8) + blue
    print(RGBint)
    return RGBint

def getIfromRGBReverse(rgb):
    print(rgb)
    red = -rgb[2] - 255
    green = -rgb[1] - 255
    blue = -rgb[0] - 255
    RGBint = (red<<16) + (green<<8) + blue
    print(RGBint)
    return RGBint



class MyPrompt(Cmd):
    api_session = None
    thread = None
    global new_color
    def do_init(self, inp):
        '''Initialize connection to Razer Synapse API.'''
        print("Initializing connection to api...")
        self.api_session = Razer_api_session()
        self.thread = threading.Thread(target=self.api_session.heartbeat)
        self.thread.start()

    def do_quit(self,inp):
        '''Disconnect and quit'''
        print("Stopping keepalive loop.")
        self.api_session.keepalive = False
        response = requests.delete(self.api_session.api_uri)
        print(response.json())
        return True

    def do_check(self,inp):
        '''Check Current heartbeat status.'''
        print("Current heartbeat count is:")
        print(self.api_session.beat_count)
    
    def do_effect(self,inp):
        resp = requests.put(self.api_session.api_uri+"/keyboard", json=color_test2)
        print(resp.json())

    def do_color(self,inp):
        rgb=list(map(int, inp.split(',')))
        print(rgb)
        color_test['param']['color'] = (getIfromRGB(rgb))
        resp = requests.put(self.api_session.api_uri+"/keyboard", json=color_test)
        print(resp.json())

    def do_wasd(self,inp):
        data = set_WASD(color_test2)
        resp = requests.put(self.api_session.api_uri+"/keyboard", json=data)
        print(resp.json())

    def do_write(self,inp):
        global test
        File_object = open("key_map.json","a+")
        File_object.write(str(test))
        File_object.close()

    def do_set(self,inp):
        global new_color
        args = inp.split(' ')
        new_color = color_test2
        rgb = list(map(int, args[1].split(',')))
        new_rgb = getIfromRGBReverse(rgb)
        print(args)
        print(rgb)
        data = set_color(args[0],new_rgb, color_test2)
        print(data)
        resp = requests.put(self.api_session.api_uri+"/keyboard", json=data)
        print(resp.json())

    def do_test(self,inp):
        print(inp)

    def do_map(self,inp):
        i=-1
        for row in color_test2['param']['key']:
            i = i+1
            if i >= 2:
                y=0
                for column in row:
                    if i ==2 and y >=7 or i > 2:
                            print("new key")
                            data=find_key(i,y)
                            resp = requests.put(self.api_session.api_uri+"/keyboard", json=data)
                            print(resp.json())
                            print("Key at " + str(i) + ',' + str(y) + " turned on")
                            print("What is this key called?")
                            key_name = input('Key name: ')
                            test[key_name] = [i,y]
                    print(str(i)+ ','+ str(y))
                    y=y+1

    def do_find(self, inp):
        global test
        location = list(map(int, inp.split(',')))
        data = find_key(location[0], location[1])
        resp = requests.put(self.api_session.api_uri+"/keyboard", json=data)
        print(resp.json())
        print("Key at " + str(location) + "turned on")
        print("What is this key called?")
        key_name = input('Key name: ')
        test[key_name] = location
    
    def do_print(self,inp):
        global test
        print(test)


def menu():
    MyPrompt().cmdloop()

if __name__ == '__main__':
    menu()



