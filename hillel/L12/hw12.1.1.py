import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    lst = []
    with codecs.open(html_file, 'r', 'utf-8') as file:
        for text in file:
            if not '</' in text:
                continue
            elif text.count('>') == 2 and text.count('<') == 1:
                end = text.find('<')
                start = text.find('>')
                new_text = text[start + 1:end]
                lst.append(new_text)
            else:
                c = text.find('<')
                end = text.find('<', c + 1)
                start = text.find('>')
                new_text = text[start + 1:end]
                if new_text.strip():
                    lst.append(new_text.strip())


    with codecs.open(result_file, 'w', 'utf-8') as file:
        for line in lst:
            file.write(line + '\n')

delete_html_tags('draft')
