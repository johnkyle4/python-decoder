# python-decoder
The fetch_grid.py script is designed to fetch and decode a secret message from a Google Document. The script performs the following steps:

1. Import Required Libraries:
- requests: To make HTTP requests to fetch the document content.
- re: For regular expression operations.
- BeautifulSoup from bs4: To parse the HTML content of the document.

2. Define fetch_and_print_grid Function:
- Fetch Content: The function takes a URL as input and uses requests.get to fetch the content of the Google Document. It raises an error if the request fails.
- Parse HTML: The fetched HTML content is parsed using BeautifulSoup to extract visible text with line breaks.
- Debugging Output: Prints a preview of the fetched content for debugging purposes.
- Extract Coordinates and Characters: Uses a regular expression to find patterns in the text that match (x, char, y) where x and y are coordinates and char is a character.
- Build Grid: Constructs a grid (2D list) based on the extracted coordinates and characters.
- Print Grid: Prints the grid row by row to display the decoded message.

3. Example Usage:
- The script includes an example URL of a Google Document and calls the fetch_and_print_grid function with this URL to demonstrate its functionality.

Example Usage
```
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
fetch_and_print_grid(url)
```

This script is useful for decoding messages embedded in Google Documents where characters are associated with specific coordinates, forming a grid that reveals the message when printed.
