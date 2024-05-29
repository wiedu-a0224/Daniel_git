import logging
import azure.functions as func
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://daniel-azureopenai-20240519.openai.azure.com/"
key = "8d60aa67aa574b71a9e9abf72927af37"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        file_url = req.params.get('file_url')
        if not file_url:
            return func.HttpResponse("Please pass a file URL in the query string", status_code=400)

        document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
        
        poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-read", file_url)
        result = poller.result()

        lines = []
        for page in result.pages:
            for line in page.lines:
                lines.append(line.content)

        return func.HttpResponse("\n".join(lines))
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
