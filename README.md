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
As the sun began to set behind the mountain range, the injured soldier continued his weary journey back home. He had been fighting for months, and his body was scarred from head to toe. But he was determined to make it back to his loved ones, even if it meant dragging himself across the terrain.

The soldier's thoughts turned to his family as he trudged on. He imagined the look on his young daughter's face when she saw him return, and he vowed to make it back to her no matter what. He would endure the pain in his knees and his shoulders, he would deal with the nightmares and the flashbacks. He would do it all to get back home.

But as the soldier's mind wandered, he began to doubt himself. What if he couldn't make it back in time for his daughter's birthday, which was a week away? What if his injuries were too severe, and he couldn't move quickly enough? The soldier paused for a moment, catching his breath and taking in his surroundings, which seemed so quiet and peaceful despite the violence that had occurred there.

The horizon glowed pink and orange, a reminder that even in the darkest of times, there was still beauty to be found.
```

#### Generated Images:
![Sunset Scene](examples/sunset.jpg)
![Soldiers Journey](examples/soldiers.jpg)
![Challenging Path](examples/path.jpg)
![Hope](examples/hope.jpg)

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
