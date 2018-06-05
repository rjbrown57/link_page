import os


def create_frame(html_name):
    try:
        os.remove('html/' + html_name)
    except OSError:
        pass

    with open('html/' + html_name, 'w+') as index:
        with open('html/frame/1.html', 'r') as frame:
            index.writelines(frame.readlines())
            frame.close()

        with open('html/frame/nav_links.html', 'r') as frame:
            index.writelines(frame.readlines())

            # Fill Nav
            for json_files in os.listdir('json_data'):
                link_name = json_files.split('.')[0]
                if link_name != 'index':
                    index.write('<a class="navbar-item" href="' + link_name + '.html">' + link_name + '</a>\n')

        with open('html/frame/2.html', 'r') as frame:
            index.writelines(frame.readlines())
            frame.close()

        index.close()


def close_frame(html_name):
    with open('html/' + html_name, 'a') as index:
        with open('html/frame/3.html', 'r') as frame:
            index.writelines(frame.readlines())
    index.close()
