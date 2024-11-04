from nbformat import read, NO_CONVERT

def count_words_in_markdown_cells(notebook_file):
    with open(notebook_file, 'r', encoding='utf-8') as f:
        nb = read(f, as_version=NO_CONVERT)
        text = ''
        for cell in nb.cells:
            if cell.cell_type == 'markdown':
                text += cell.source + ' '
        word_count = len(text.split())
        return word_count

notebook_file_path = 'documentation.ipynb'  # Update with your notebook path
print(f'Total word count in Markdown cells: {count_words_in_markdown_cells(notebook_file_path)}')
