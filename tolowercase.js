const fs = require("fs");
const path = require("path");

// Replace with the path to your JSON file
const filePath = path.join(__dirname, "rst.json");

// Read the JSON file
fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }

  // Parse the JSON data
  let books = JSON.parse(data);

  // Update the book names to lowercase
  books = books.map((book) => {
    if (book.book) {
      book.book = book.book.toLowerCase();
    }
    return book;
  });

  // Convert the updated object back to JSON string
  const updatedData = JSON.stringify(books, null, 2);

  // Write the updated JSON string back to the file
  fs.writeFile(filePath, updatedData, "utf8", (err) => {
    if (err) {
      console.error("Error writing to the file:", err);
    } else {
      console.log("Book names have been updated to lowercase.");
    }
  });
});
