import markdown


markdown_string = '# Hello World'


html_string = markdown.markdown(markdown_string)
print(html_string)