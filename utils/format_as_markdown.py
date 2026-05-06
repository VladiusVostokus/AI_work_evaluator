def format_as_markdown(file_table):
    if not file_table:
        return ''
    markdown = ''
    for i, row in enumerate(file_table):
        markdown += '| ' + ' | '.join(row) + ' |\n'
        if i == 0:
            markdown += '| ' + ' | '.join(['---'] * len(row)) + ' |\n'
    return markdown
