from interfaces.work_parser import WorkParser
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
            blocks = page.get_text('blocks')
            blocks.sort(key=lambda b: (b[1], b[0]))

            processed_tabs = set()

            for b in blocks:
                block_rect = pymupdf.Rect(b[:4])
                inside_table = False

                for i, tab_rect in enumerate(tab_rects):
                    if block_rect.intersects(tab_rect):
                        if i not in processed_tabs:
                            table_data = tables[i].extract()
                            result.append({'type':'table', 'data': table_data})
                            processed_tabs.add(i)
                        inside_table = True
                        break
                if not inside_table:
                    text = b[4].strip()
                    if text:
                        result.append({'type':'text', 'data': text}) 
            return result

    def get_all_tables(self):
        pass

    def get_parsed_data(self):
        pass
    