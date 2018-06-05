import interpret
import frames
import os

# Main Calls
for json_file in os.listdir('json_data'):
    html_name = json_file.split('.')[0] + '.html'
    frames.create_frame(html_name)
    interpret.interpret(html_name, 'json_data/' + json_file)
    frames.close_frame(html_name)
