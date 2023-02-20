from quarto import render

out_filename = "generic_qa_report.html"

render(
    input = "qa_report.qmd", 
    output_format = "html",
    output_file = out_filename, 
    )