import sys
import os

def convert_markdown_to_html(markdown_text):
    html = ""
    lines = markdown_text.splitlines()
    for line in lines:
        if line.startswith("# "):
            html += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith("## "):
            html += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("### "):
            html += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("* "):
            html += f"<ul><li>{line[2:]}</li></ul>\n"
        elif line.startswith("- "):
            html += f"<ul><li>{line[2:]}</li></ul>\n"
        elif line.strip() == "":
            html += "<br/>\n"
        else:
            html += f"<p>{line}</p>\n"
    return html

def main():
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_html.py input.md output.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' does not exist.")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    html_text = convert_markdown_to_html(markdown_text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_text)

    print(f"Converted '{input_file}' to '{output_file}'.")

if __name__ == "__main__":
    main()