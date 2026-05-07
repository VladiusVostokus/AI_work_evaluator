from interfaces.work_parser import WorkParser
from utils.mark_table_bounds import mark_table_bounds
import pymupdf

class PdfParser(WorkParser):
    def __init__(self, filename):
        self.file = filename

    def get_all_content(self):
        data = pymupdf.open(self.file)
        result = []
        for page in data:
            tables = page.find_tables()
            tab_rects = [t.bbox for t in tables]
            page_dict = page.get_text('dict')
            blocks = sorted(page_dict['blocks'], key=lambda b: (b['bbox'][1]))
            processed_tabs_indecies = set()
            text_type = 0
            for b in blocks:
                if b['type'] != text_type:
                    continue
                
                for line in b['lines']:
                    line_rect = pymupdf.Rect(line["bbox"])
                    line_in_table = False
                    for i, tab_rect in enumerate(tab_rects):
                        if line_rect.intersects(tab_rect):
                            if i not in processed_tabs_indecies:
                                table_data = tables[i].extract()
                                result.append({'type':'table', 'data': table_data})
                                processed_tabs_indecies.add(i)
                            line_in_table = True
                            break
                            
                    if not line_in_table:
                        text = ''.join([span["text"] for span in line['spans']]).strip()
                        if text:
                            if result and result[-1]['type'] == 'text':
                                result[-1]['data'] += '\n' + text
                            else:
                                result.append({'type':'text', 'data': text}) 
            return result

    def get_all_tables(self):
        pass

    def get_parsed_data(self):
        file_content = self.get_all_content()
        parsed_data = mark_table_bounds(file_content)
        return parsed_data

    