import os
import sys
import shutil

# open a text file ending with .md and append a paragraph to it
def reformat_plugin(dirpath, plugin_name):
    plugins_dir = '/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins'
    index_file = os.path.join(plugins_dir, 'index.md')
    shutil.copyfile(os.path.join(dirpath, 'README.md'), index_file)
    with open(index_file) as f:
        text = f.read()
        append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
---
'''.format(plugin_name=plugin_name)
        text = append_text + text
        with open(index_file, 'w') as out:
            out.write(text)

# open a text file ending with .md and append a paragraph to it
# Usage: python test.py <filename>.md
def append_to_file(filepath, filename, parent, output_file):
    with open(filepath) as f:
        text = f.read()
        append_text = '''---
layout: default
title: {filename}
long_title: {filename}
parent: {parent}
grand_parent: Plugins
---
'''.format(filename=filename, parent=parent)
        text = append_text + text
    with open(output_file, 'w') as out:
        out.write(text)

def reformat_plugin_dir(plugin_input_dir, plugin_name, plugin_type='wiki'):
    # plugins_output_dir = '/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins'
    plugin_output_dir = os.path.join('/Users/dtyoung/Documents/EEGLAB/sccn.github.io/plugins', plugin_name)
    if not os.path.exists(plugin_output_dir):
        os.makedirs(plugin_output_dir)
    # copy image directory from input to output dir
    if os.path.exists(os.path.join(plugin_input_dir, 'images')):
        shutil.copytree(os.path.join(plugin_input_dir, 'images'), os.path.join(plugin_output_dir, 'images'), dirs_exist_ok=True)

    index_file = os.path.join(plugin_output_dir, 'index.md')
    if plugin_type == 'wiki':
        shutil.copyfile(os.path.join(plugin_input_dir, 'Home.md'), index_file)
        with open(index_file) as f:
            text = f.read()
            append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
categories: plugins
has_children: true
---
'''.format(plugin_name=plugin_name)
            text = append_text + text
            with open(index_file, 'w') as out:
                out.write(text)

        for root, dirs, files in os.walk(plugin_input_dir):
            for file in files:
                if file.endswith('.md') and not file.startswith('index') and not file.startswith('Home'):
                    append_to_file(os.path.join(plugin_input_dir, file), file.strip('.md'), plugin_name, os.path.join(plugin_output_dir, file))
    else:
        shutil.copyfile(os.path.join(plugin_input_dir, 'README.md'), index_file)
        with open(index_file) as f:
            text = f.read()
            append_text = '''---
layout: default
title: {plugin_name}
long_title: {plugin_name}
parent: Plugins
---
'''.format(plugin_name=plugin_name)
            text = append_text + text
            with open(index_file, 'w') as out:
                out.write(text)

# main
def main():
    if len(sys.argv) != 4:
        print('Usage: python test.py <plugin_dir_path> <plugin_name> <plugin_type>')
        sys.exit(1)
    dirpath = sys.argv[1]
    plugin_name = sys.argv[2]
    plugin_type = sys.argv[3]
    reformat_plugin_dir(dirpath, plugin_name, plugin_type)

if __name__ == "__main__":
    main()