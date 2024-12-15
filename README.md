# Receipt Parser Using OCR and GPT

## Project Overview

This project demonstrates a pipeline for extracting structured data from store receipts using OCR (Optical Character Recognition) and AI. The program combines Python libraries such as OpenCV and Tesseract for image preprocessing and text extraction, with OpenAI's GPT models for advanced text parsing and structuring. The final output is a JSON object containing key information such as total cost, business name, item details, and transaction timestamp.

## Features

- 🖼️ **Image Preprocessing**: Converts the receipt image to a binary format using grayscale conversion and OTSU thresholding for optimal OCR performance.
- 🔍 **OCR with Tesseract**: Extracts raw text from the preprocessed receipt image.
- 🤖 **AI-Powered Text Parsing**: Leverages OpenAI's GPT model to transform the extracted text into a structured JSON object.
- 📂 **Output in JSON Format**: Stores parsed receipt data in an easy-to-use JSON format.

## Requirements

### Libraries

The following Python libraries are required to run the project:

- 📦 `opencv-python`: For image processing.
- 📦 `pytesseract`: For OCR.
- 📦 `openai`: For accessing OpenAI's GPT models.

You can install the required libraries with the following command:

```bash
pip install opencv-python pytesseract openai
```

### External Dependencies

- ⚙️ **Tesseract OCR**: Ensure Tesseract OCR is installed on your system. You can follow the installation guide for your OS [here](https://github.com/tesseract-ocr/tesseract).

## Usage

1. 📂 Clone the repository:

   ```bash
   git clone https://github.com/username/receipt-parser.git
   cd receipt-parser
   ```

2. 🔑 Replace the placeholder `MY_API_KEY` in the script with your OpenAI API key.

3. 🖼️ Prepare the receipt image:
   - Save the receipt image in the root directory as `receipt.jpg`, or modify the `image_path` variable in the script with the correct path.

4. ▶️ Run the script:

   ```bash
   python receipt_parser.py
   ```

5. 💾 The output JSON will be saved as `receipt.json` in the same directory.

## Script Breakdown

### 1. Preprocess the Image

The `pre_process_image` function reads the image and applies grayscale conversion and binary thresholding to enhance the OCR process.

```python
def pre_process_image(image):
    image = cv2.imread(image)       #reading image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #setting grayscale
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold        #returning the binary image
```

### 2. Extract Text with OCR

The `extract_text` function uses Tesseract OCR to convert the preprocessed image into raw text.

```python
def extract_text(image):
    return pytesseract.image_to_string(image)
```

### 3. Parse Text with GPT

The `ai_extract` function constructs a prompt for GPT to parse the receipt text and return a structured JSON object.

```python
def ai_extract(text_content):
    prompt = """You are a receipt parser AI..."""
    response = aiclient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

### 4. Save Output as JSON

The parsed JSON is saved to a file for further use.

```python
with open("receipt.json", "w") as file:
    file.write(json_data)
```

## Example

### Input
A receipt image saved as `receipt.jpg`.

### Output
The resulting JSON structure:

```json
{
    "total": 8,
    "business": "Supermarket X",
    "items": [
        {"title": "Milk", "quantity": 2, "price": 3},
        {"title": "Bread", "quantity": 1, "price": 2}
    ],
    "transaction_timestamp": "2024-12-15T10:34:00Z"
}
```

## Limitations

- ⚠️ The accuracy of OCR and text parsing depends heavily on the quality of the receipt image.
- ⚠️ GPT-based parsing may require fine-tuning or adjustments for different receipt formats.

## Future Improvements

- 🌍 Add support for additional receipt formats and languages.
- 🔧 Include error handling for missing or inconsistent data.
- ⚡ Optimize the preprocessing pipeline for better OCR accuracy.

## License

This project is licensed under the MIT License.

