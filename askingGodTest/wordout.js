const { ComputerVisionClient } = require("@azure/cognitiveservices-computervision");
const { CognitiveServicesCredentials } = require("@azure/ms-rest-azure-js");

module.exports = async function (context, req) {
    const subscriptionKey = process.env["8d60aa67aa574b71a9e9abf72927af37"];
    const endpoint = process.env["https://daniel-azureopenai-20240519.openai.azure.com/"];
    const cognitiveServiceCredentials = new CognitiveServicesCredentials(subscriptionKey);
    const client = new ComputerVisionClient(cognitiveServiceCredentials, endpoint);

    const imageUrl = req.body.imageUrl;

    try {
        const result = await client.read(imageUrl);
        const operation = result.operationLocation.split('/').slice(-1)[0];

        let resultStatus = await client.getReadResult(operation);
        while (resultStatus.status === "notStarted" || resultStatus.status === "running") {
            resultStatus = await client.getReadResult(operation);
        }

        const recognizedText = resultStatus.analyzeResult.readResults.map(page => 
            page.lines.map(line => line.text).join('\n')
        ).join('\n');

        context.res = {
            status: 200,
            body: recognizedText
        };
    } catch (error) {
        context.res = {
            status: 500,
            body: error.message
        };
    }
};
