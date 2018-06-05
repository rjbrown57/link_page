import json


def interpret(html_name, json_name):
    with open('html/' + html_name, 'a') as index:

        with open(json_name, 'r') as file_data:
            json_data = json.load(file_data)

            for heading in sorted(json_data):
                # Create Column
                index.write('<div class ="column is-size-7 is-narrow">' + "\n")
                # Create left part of media object
                index.write(
                    '<div class="box"><article class="media"><span class="tag is-danger">'
                    + heading
                    + "</span>\n")

                # Create center
                index.write('<div class="media-content"><div class="content">')

                for sub_heading in sorted(json_data[heading]):

                    # Fill Center
                    if type(json_data[heading][sub_heading]["links"]) is dict:
                        iterator = 1

                        index.write('<div class="navbar-item has-dropdown is-hoverable"><a class="navbar-link">' +
                                    json_data[heading][sub_heading]["text"] + '</a>' +
                                    '<div class="navbar-dropdown is-boxed">\n')

                        for link in sorted(json_data[heading][sub_heading]["links"],key=int):
                            index.write(
                                '<a class="navbar-item" href="' +
                                json_data[heading][sub_heading]["links"][link] + '">' +
                                str(iterator) + "</a>\n")
                            iterator = iterator + 1

                        index.write('</div></div>')
                    elif "info" in json_data[heading][sub_heading]:
                        index.write('<a class="navbar-item" title="' + json_data[heading][sub_heading]["info"]
                                    + '" href="' +
                                    json_data[heading][sub_heading]["links"] + '">' +
                                    json_data[heading][sub_heading]["text"] + "</a>\n")
                    else:
                        index.write(
                            '<a class="navbar-item" href="' +
                            json_data[heading][sub_heading]["links"] + '">' +
                            json_data[heading][sub_heading]["text"] + "</a>\n")

                index.write('</div></div></article></div></div>')
            file_data.close()
            index.close()
