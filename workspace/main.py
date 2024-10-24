import PyPDF2

def main():
    book_path = "workspace/books/Computer Networks.pdf"  # PDF file
    word_to_search = input("Enter word: ").lower()  # Convert to lowercase for case-insensitive search
    page_numbers = find_word_in_pdf(book_path, word_to_search)  # Find the word in the PDF
    
    if page_numbers:
        print(f"The word '{word_to_search}' was found on the following pages: {page_numbers}")
    else:
        print(f"The word '{word_to_search}' was not found in the document.")


def find_word_in_pdf(path, word):
    """Search for a word in a PDF and return the page numbers where it appears."""
    page_numbers = []  # List to store the page numbers where the word is found
    with open(path, "rb") as file:  # Open the PDF file in binary mode
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):  # Loop through all the pages
            page = reader.pages[page_num]
            page_text = page.extract_text().lower()  # Extract the text and convert to lowercase
            if word in page_text:  # Check if the word exists on the current page
                page_numbers.append(page_num + 1)  # Store the page number (starting from 1)
    return page_numbers


main()
