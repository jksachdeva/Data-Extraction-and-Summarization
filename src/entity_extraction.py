from google.cloud import language_v1

# Initialize Google Cloud Natural Language API client
client = language_v1.LanguageServiceClient()

def extract_entities(text):
    """
    Extracts named entities from the given text using Google Cloud Natural Language API.

    Args:
        text (str): Input text.

    Returns:
        list of tuples: Each tuple contains (entity name, entity type).
    """
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)
    entities = [
        (entity.name, language_v1.Entity.Type(entity.type_).name)
        for entity in response.entities
    ]
    return entities

def extract_sentiment(text):
    """
    Analyzes sentiment of the given text using Google Cloud Natural Language API.

    Args:
        text (str): Input text.

    Returns:
        float: Sentiment score of the document.
    """
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document=document)
    return response.document_sentiment.score