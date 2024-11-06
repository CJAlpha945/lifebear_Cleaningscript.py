
# CSV Chunking Script

This project provides a Python script to split a large CSV file into smaller chunks based on a specified number of chunks and lines to extract. The script can be customized to read only the desired parts of each chunk (e.g., headers, first few lines, last few lines) and to store the data in separate CSV files.

## Features
- Splits a CSV file into a specified number of chunks.
- Extracts the first few and last few lines from each chunk for easy inspection.
- Saves each chunk to a separate CSV file with the option to include only selected headers.

## Prerequisites
- Python 3.7+
- pandas library
- Ensure that your input CSV file uses a consistent separator (e.g., `;`).

## Usage

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/csv-chunking-script.git
   cd csv-chunking-script
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas
   ```

3. Run the script with your CSV file in the desired directory. Update the parameters as needed:
   ```python
   import pandas as pd

   # Define your desired settings
   num_chunks = 4
   num_lines_to_extract = 5
   sep = ';'  # Adjust if necessary

   # Modify the file path and run the script
   ```
   
   **Parameters:**
   - `num_chunks`: The number of chunks to divide the file into.
   - `num_lines_to_extract`: The number of header and footer lines extracted per chunk.
   - `sep`: The separator used in the CSV file (e.g., `;`).

4. Processed files will be saved in the `content` folder as `chunk_<i>.csv`.

5. **Additional Output:** A separate file (`chunk_<i>_headers.csv`) is created for each chunk's headers.

## Example Code

```python
import pandas as pd

# Your script goes here...
```

## Output
After running the script, you should see output files like:
- `chunk_0.csv`, `chunk_1.csv`, etc. for each chunk
- `chunk_0_headers.csv`, `chunk_1_headers.csv`, etc. for each chunk's headers

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests for improvements or fixes. Your contributions are welcome!

---

Replace `https://github.com/yourusername/csv-chunking-script.git` with the actual link to your repository once uploaded. 

