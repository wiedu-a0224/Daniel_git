mongoimport --file DeviceTemperature.json --type json --db IoTDatabase1 --collection IoTCollection1 --ssl --uri mongodb+srv://MongoAdmin:1Password!@mycosmosdbvcore.mongocluster.cosmos.azure.com/?tls=true --writeConcern {w:0} --jsonArray