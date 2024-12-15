import cv2              #Image process library
import pytesseract      #OCR library
from openai import OpenAI

aiclient = OpenAI(
    api_key = "MY_API_KEY"
)

def pre_process_image(image):
    image = cv2.imread(image)       #reading image
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #setting grayscale

    # creating a binary version of the image, using OTSU to automatically find the optimal threshold value
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 

    return threshold        #returning the binary image

def extract_text(image):
    return pytesseract.image_to_string(image)   #converting the image into text


def ai_extract(text_content):
    prompt = """You are a receipt parser AI. You are given a receipt to parse via an image of a store receipt.
    I need you to return a JSON object with the following fields:
    {"total", "business", "items": [{"title", "quantity", "price}], "transaction_timestamp"}.
    Return the prices as integers that represents the number of cents (1€ = 100 cents). Only return the JSON object.
    Do not return anything else. Here is the text extracted from the receipt: """ + text_content

    response = aiclient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user", #this input comes from the user
                "content": prompt   #this is the prompt
            }
        ]
    )
        
    #extracting the JSON object from the response
    return response.choices[0].message.content[response.choices[0].message.content.find("{"):response.choices[0].message.content.rfind("}")+1]
    
if __name__ == "__main__":
    image_path = "receipt.jpg"

    preprocessedImage = pre_process_image(image_path)
    
    textContent = extract_text(preprocessedImage)

    json_data = ai_extract(textContent)

    with open("receipt.json", "w") as file:
        file.write(json_data)
