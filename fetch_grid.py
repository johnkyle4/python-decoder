import requests
import re
from bs4 import BeautifulSoup

def fetch_and_print_grid(url):
    # Fetch the content of the Google Doc
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.get_text(separator="\n")  # Extract visible text with line breaks

    print("Fetched content preview:\n", content[:500])  # Debugging: Print a snippet of the content

    # Regular expression to find (x, y) coordinates and characters in table format
    pattern = r"(\d+)\s*([^\d\s])\s*(\d+)"
    matches = re.findall(pattern, content)

    # Extract the character and its coordinates
    grid = {}
    for x, char, y in matches:
        x, y = int(x), int(y)
        grid[(x, y)] = char.strip()

    if not grid:
        print("No valid data found in the document.")
        return

    # Determine the dimensions of the grid
    max_x = max(pos[0] for pos in grid.keys())
    max_y = max(pos[1] for pos in grid.keys())

    # Create the grid
    output = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y), char in grid.items():
        output[y][x] = char

    # Print the grid
    for row in output:
        print("".join(row))

# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
fetch_and_print_grid(url)
