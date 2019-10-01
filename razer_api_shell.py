import webcolors
import threading
import requests
import time


def RGBtoBRG(rgb):
    '''Changes the color from RGB format to BRG format. '''
    print(rgb)
    for indx, color in enumerate(rgb):
        
        if color == 0:
            rgb[indx] = rgb[indx] + 1
            
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    RGBint = (blue<<16) + (green<<8) + red
    return RGBint


class KeyGroups():
    wasd = ['W', 'A', 'S', 'D']
    arrow = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    macro = ['MACRO_1', 'MACRO_2', 'MACRO_3', 'MACRO_4', 'MACRO_5']
    f_keys = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

class Razer_api():
    static_uri = "http://localhost:54235/razer/chromasdk"
    effect_static = {
        "effect": "CHROMA_STATIC",
        "param": {
            "color": 0
        }
    }
    original_palette = {
        "effect": "CHROMA_CUSTOM_KEY",
        "param": {
            "color": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            "key": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        }
    }
    sdk_information = {
        "title": "Razer Chroma SDK Python shell",
        "description": "Example usage of Chroma API thru Python",
        "author": {
            "name": "Arttu M.",
            "contact": "https://github.com/amahlaka/Razer-chroma-python-shell/issues"
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
    key_names = {'ESC': [0, 1], 'F1': [0, 3], 'F2': [0, 4], 'F3': [0, 5], 'F4': [0, 6], 'F5': [0, 7], 'F6': [0, 8], 'F7': [0, 9], 'F8': [0, 10], 'F9': [0, 11], 'F10': [0, 12], 'F11': [0, 13], 'F12': [0, 14], 'PRT_SC': [0, 15], 'SCR_LK': [0, 16], 'PAUSE': [0, 17], 'UNKNOWN_1': [0, 18], 'UNKNOWN_2': [0, 19], 'LOGO': [0, 20], 'MACRO_1': [1, 0], 'SECTION': [1, 1], '1': [1, 2], '2': [1, 3], '3': [1, 4], '4': [1, 5], '5': [1, 6], '6': [1, 7], '7': [1, 8], '8': [1, 9], '9': [1, 10], '0': [1, 11], '+': [1, 12], 'TILDA': [1, 13], 'BACKSPACE': [1, 14], 'INSERT': [1, 15], 'HOME': [1, 16], 'PAGE_UP': [1, 17], 'NUM_LK': [1, 18], 'DIVIDE': [1, 19], 'MULTIPLY': [1, 20], 'MINUS': [1, 21], 'MACRO_2': [2, 0], 'TAB': [2, 1], 'Q': [2, 2], 'W': [2, 3], 'E': [2, 4], 'R': [2, 5], 'T': [2, 6], 'Y': [2, 7], 'U': [2, 8], 'I': [2, 9], 'O': [2, 10], 'P': [2, 11], 'Å': [2, 12], '^': [2, 13], "'": [2, 14], 'DEL': [2, 15], 'END': [2, 16], 'PAGE_DOWN': [2, 17], 'NUM_7': [2, 18], 'NUM_8': [2, 19], 'NUM_9': [2, 20], 'NUM_PLUS': [2, 21], 'MACRO_3': [3, 0], 'CAPS_LOCK': [3, 1], 'A': [3, 2], 'S': [3, 3], 'D': [
        3, 4], 'F': [3, 5], 'G': [3, 6], 'H': [3, 7], 'J': [3, 8], 'K': [3, 9], 'L': [3, 10], 'Ö': [3, 11], 'Ä': [3, 12], 'UNKNOWN_3': [3, 13], 'ENTER': [3, 14], 'UNKNOWN_4': [3, 15], 'UNKNOWN_5': [3, 16], 'UNKNOWN_6': [3, 17], 'NUM_4': [3, 18], 'NUM_5': [3, 19], 'NUM_6': [3, 20], 'UNKNOWN_7': [3, 21], 'MACRO_4': [4, 0], 'L_SHIFT': [4, 1], '<': [4, 2], 'Z': [4, 3], 'X': [4, 4], 'C': [4, 5], 'V': [4, 6], 'B': [4, 7], 'N': [4, 8], 'M': [4, 9], ',': [4, 10], '.': [4, 11], '_': [4, 12], 'UNKNOWN_8': [4, 13], 'R_SHIFT': [4, 14], 'UNKNOWN_9': [4, 15], 'UP': [4, 16], 'UNKNOWN_10': [4, 17], 'NUM_1': [4, 18], 'NUM_2': [4, 19], 'NUM_3': [4, 20], 'NUM_ENTER': [4, 21], 'MACRO_5': [5, 0], 'L_CTRL': [5, 1], 'WINDOWS': [5, 2], 'L_ALT': [5, 3], 'UNKNOWN_11': [5, 4], 'UNKNOWN_12': [5, 5], 'UNKNOWN_13': [5, 6], 'SPACEBAR': [5, 7], 'UNKNOWN_14': [5, 8], 'UNKNOWN_15': [5, 9], 'UNKNOWN_16': [5, 10], 'ALT_GR': [5, 11], 'FN': [5, 12], 'LIST': [5, 13], 'R_CTRL': [5, 14], 'LEFT': [5, 15], 'DOWN': [5, 16], 'RIGHT': [5, 17], 'RIGHT_2': [5, 18], 'NUM_0': [5, 19], 'NUM_DEL': [5, 20], 'NUM_UNK3': [5, 21]}
    def __init__(self, sdk_config=sdk_information, palette=original_palette, debug=False):
        init_api_response = requests.post(self.static_uri, json=sdk_config)
        self.session_id = init_api_response.json()['sessionid']
        self.api_uri = init_api_response.json()['uri']
        self.color_palette=palette
        self.debug = debug
    
    def heartbeat(self):
        self.heartbeat_uri = self.api_uri+"/heartbeat"
        print("Starting keepalive loop...")
        self.keepalive = True
        while self.keepalive is True:
            try:
                heartbeat_response = requests.put(self.heartbeat_uri)
                self.heartbeat_count = heartbeat_response.json()['tick']
                time.sleep(10)
            except Exception as e:
                print(e)
                print("Error in heartbeat loop, stopping...")
                self.keepalive = False

    def send_palette(self, palette):
        api_response = requests.put(self.api_uri+"/keyboard", json=palette)
        if self.debug is True:
            print(api_response.json())

    def set_single_key(self,key_name,rgb_color):
        try:
            key_index = self.key_names[key_name]
        except KeyError:
            print("Sorry, that key is not in the list, please try again!")
            return
        brg_color = RGBtoBRG(rgb_color)
        if self.debug is True:
            print(brg_color)
        self.color_palette['param']['color'][key_index[0]][key_index[1]] = brg_color
        self.send_palette(self.color_palette)

    def set_all(self, color_rgb):
        color = RGBtoBRG(color_rgb)
        local_palette = self.color_palette
        for indx,row in enumerate(local_palette['param']['color']):
            for index,column in enumerate(row):
                local_palette['param']['color'][indx][index] = color
                print(column)
        self.color_palette = local_palette
        self.send_palette(self.color_palette)


    def set_multiple_keys(self,keys_list, color_rgb):
        local_palette = self.color_palette
        color = RGBtoBRG(color_rgb)
        for key in keys_list:
            if key not in self.key_names:
                print('ERROR: Invalid key name: '+ str(key))
                return
            key_index = self.key_names[key]
            local_palette['param']['color'][key_index[0]][key_index[1]] = color
        self.color_palette = local_palette
        self.send_palette(self.color_palette)


    def send_raw_color(self,color_int):
        self.effect_static['param']['color'] = int(color_int)
        api_response = requests.put(self.api_uri+"/keyboard", json=self.effect_static)
        if self.debug is True:
            print(api_response.json())

from cmd import Cmd

class CommandPrompt(Cmd):
    initialized = False
    prompt = 'RΛZΞR> '
    def do_init(self,inp):
        '''Initialize Razer Chroma API connection.'''
        self.initialized = True
        self.api_instance = Razer_api(debug=True)
        self.keepalive_thread = threading.Thread(target=self.api_instance.heartbeat)
        self.keepalive_thread.start()
    
    def do_quit(self,inp):
        '''Disconnect from the API and quit the shell.'''
        if self.initialized:
            self.api_instance.keepalive = False
            quit_response = requests.delete(self.api_instance.api_uri)
            print(quit_response.json())
        return True

    def do_colorname(self,inp):
        '''Set entire keyboard to the specified color.
        Usage example: colorname red'''
        try:
            color_rgb = list(webcolors.name_to_rgb(inp))
        except:
            print("Invalid colorname")
            return
        self.api_instance.set_all(color_rgb)

    def do_check(self,inp):
        '''Show the current heartbeat count.'''
        print("Current heartbeat count: " + str(self.api_instance.heartbeat_count))

    def do_controls(self,inp):
        '''Set color on mots used gaming keys.'''
        self.api_instance.set_multiple_keys(KeyGroups.wasd,[255,0,0])
        self.api_instance.set_multiple_keys(KeyGroups.numbers, [50,255,125])
        self.api_instance.set_multiple_keys(KeyGroups.arrow, [255,255,255])
        self.api_instance.set_multiple_keys(KeyGroups.f_keys, [0,255,0])
        self.api_instance.set_multiple_keys(KeyGroups.macro, [0,0,255])
        self.api_instance.set_multiple_keys(['ENTER', 'LOGO', 'WINDOWS'], list(webcolors.name_to_rgb('purple')))


if __name__ == '__main__':
    asciiart = open('art.txt','r')
    print(asciiart.read())
    print('Created by: Arttu Mahlakaarto - ©2019 ')
    print("Welcome to RΛZΞR Chroma API python shell, type 'help' for list of commands")
    CommandPrompt().cmdloop()