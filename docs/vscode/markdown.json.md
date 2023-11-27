# markdown.json

```json
{
	// Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	"Print to console": {
		"prefix": "code",
		"body": [
			"---",
			"title: $TM_FILENAME_BASE",
			"output:",
			"  pdf_document:",
			"    latex_engine: xelatex",
			"    toc: true",
			"    template: C:/Huaxv/Huaxv-Tool/markdown-preview=enhanced/template.tex",
			"    highlight: tango",
			"    path: C:/Users/huaxv/Desktop/$TM_FILENAME_BASE.pdf",
			"---",
			
		],
		"description": "Log output to console"
	}
}
```
