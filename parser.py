import opendataloader_pdf

def parse_pdf(input_path, output_dir):
    print("Parseando PDF...")

    opendataloader_pdf.convert(
        input_path=input_path,
        output_dir=output_dir,
        format="markdown,json"
    )

    print("PDF convertido")