# AI Story & Image Generator

A creative application that generates stories and matching AI-generated images using the power of Cohere for story generation and ClipDrop for image creation.

## Features

- 🖋 AI-powered story generation
- 🎨 Automatic image generation based on story context
- 🖼 Multiple image suggestions for each story
- 💫 Interactive Streamlit interface

## Demo

Here's how the application works:

1. Enter a story prompt (e.g., "An injured soldier tries to make his way back home")
2. The AI generates a compelling story in 5 paragraphs
3. The system extracts key scenes from the story
4. AI generates matching images for each scene
5. View your story alongside beautiful AI-generated artwork

### Example Output

For the prompt "An injured soldier tries to make his way back home":

#### Story:
```
 The sun dipped behind the mountains casting a golden glow on the rocky terrain. The injured man struggled onwards, limping from the pain that wracked his body. He had heard stories as a child of the miraculous healings that occurred at the holy site, and he prayed that he would be so blessed. He had no food or water and had gone three days without sustenance. 

Thirst and hunger were not his only struggles, however. He had been attacked a few nights ago by a roaming group of bandits that had left him with these injuries and fled with his coin and clothes. He had nothing to steal now, but he was afraid of what they might do if they found him again. 

So he pressed on, focusing on the craggy outline of the mountain range that marked his destination. He imagined the cool water he would taste from the fountain and the soft bread that would sustain him. Most of all he imagined the healing touch that would enable him to press on past his injuries and continue to live his life. 
```

#### Generated Images:
![Golden Glow](https://raw.githubusercontent.com/gideonsuttle/story_with_image/main/examples/image_1.jpg)
![Survival of the Weak](https://raw.githubusercontent.com/gideonsuttle/story_with_image/main/examples/image_2.jpg)
![Blessings of the Sacred Site](https://raw.githubusercontent.com/gideonsuttle/story_with_image/main/examples/image_3.jpg)
![Hope in the Face of Adversity](https://raw.githubusercontent.com/gideonsuttle/story_with_image/main/examples/image_4.jpg)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd story_with_image

# Install required packages
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with your API keys:
COHERE_API_KEY=your_cohere_api_key
CLIPDROP_API_KEY=your_clipdrop_api_key
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run code.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter your story prompt in the text input field

4. Click the "Generate" button to create your story and images

## Dependencies

- Python 3.8+
- Streamlit
- Langchain
- Cohere
- ClipDrop API
- python-dotenv
- Pillow
- requests

## Environment Variables

The application requires two API keys:

- `COHERE_API_KEY`: For story generation (Get it from [Cohere](https://cohere.ai))
- `CLIPDROP_API_KEY`: For image generation (Get it from [ClipDrop](https://clipdrop.co))

## License

MIT License

## Contributing

Feel free to open issues and pull requests to improve the application.
