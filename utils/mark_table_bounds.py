from utils.format_as_markdown import format_as_markdown

def mark_table_bounds(file_content):
    marked_text = ''
    if not file_content:
        return ''
    for item in file_content:
        if item['type'] == 'text':
            marked_text += item['data'] + '\n\n'
        else:
            marked_text += '===TABLE START===\n' + format_as_markdown(item['data']) + '===TABLE END===\n\n'
    return marked_text
