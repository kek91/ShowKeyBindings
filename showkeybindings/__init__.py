from fman import DirectoryPaneCommand, load_json, show_alert

class ShowKeyBindings(DirectoryPaneCommand):
    def __call__(self):
        keybindings_json = load_json('Key Bindings.json')
        keybindings_output = ""

        for keybind in keybindings_json:
            command = str(keybind['command'].capitalize().replace('_', ' '))
            key = str(keybind['keys']).replace('[\'', '').replace('\']', '')
            tab = "\t"
            tab_num = 1
            keybindings_output += key + (tab * tab_num) + " = " + command + "\n"

        show_alert(keybindings_output)
