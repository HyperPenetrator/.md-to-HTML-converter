# Markdown to HTML Converter (Basic)

A simple beginner-friendly Python script to convert Markdown files to HTML using only file I/O and manual string manipulation.

## Features

- Converts Markdown headings (`#`, `##`, `###`) to HTML headings.
- Converts unordered lists (`*`, `-`) to HTML lists.
- Converts blank lines to `<br/>`.
- Converts all other lines to paragraphs.
- No external libraries required.

## Usage

```bash
python markdown_to_html.py input.md output.html
```

- `input.md`: Path to your Markdown file.
- `output.html`: Path to save the generated HTML file.

## Example

**input.md:**
```
# Title

## Subtitle

This is a paragraph.

* Item 1
* Item 2

- Item 3

### Small heading
```

**output.html:**
```html
<h1>Title</h1>
<br/>
<h2>Subtitle</h2>
<br/>
<p>This is a paragraph.</p>
<br/>
<ul><li>Item 1</li></ul>
<ul><li>Item 2</li></ul>
<br/>
<ul><li>Item 3</li></ul>
<br/>
<h3>Small heading</h3>
```

## Notes

- Only basic Markdown features are supported.
- Lists are not grouped; each item is wrapped in its own `<ul>`.
