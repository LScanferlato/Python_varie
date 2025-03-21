from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', '', 12)
        self.cell(0, 10, 'Titolo del Documento', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Helvetica', '', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf(txt_file, pdf_file):
    pdf = PDF()
    pdf.add_page()
    pdf.add_font('Helvetica', '', 'Helvetica.ttf', uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)

    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()

    pdf.chapter_title('Capitolo 1')
    pdf.chapter_body(content)
    pdf.output(pdf_file)

create_pdf('tuo_file.txt', 'output.pdf')
