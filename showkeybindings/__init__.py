from fman import DirectoryPaneCommand, load_json, show_alert

class ShowKeyBindings(DirectoryPaneCommand):
    def __call__(self):
        keybindings_json = load_json('Key Bindings.json')
        keybindings_output = ""
        
        for keybind in keybindings_json:
            keybindings_output += str(keybind['keys']) + "\t\t = " + str(keybind['command']) + "\n"

        show_alert(keybindings_output)
