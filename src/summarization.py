from vertexai.preview.generative_models import GenerativeModel

# Initialize Vertex AI Gemini model
model = GenerativeModel('gemini-2.5-pro')

def summarize_text(text):
    """
    Summarizes the given news description into a single sentence

    Args:
        text (str): Input news description.

    Returns:
        str: Summarized sentence.
    """
    prompt = f"Summarize the following news description in one sentence:\n{text}"
    response = model.generate_content(prompt)
    return response.text