targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment that can be used as part of naming resource convention')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

@description('Name of the resource group to create')
param resourceGroupName string = 'rg-${environmentName}'

@description('Environment variables for the container app')
param streamlitServerPort string = '8520'
param streamlitServerAddress string = '0.0.0.0'
param pythonUnbuffered string = '1'

// Resource token for unique naming
var resourceToken = uniqueString(subscription().id, location, environmentName)
var resourcePrefix = 'cks' // cokesales

// Create resource group
resource rg 'Microsoft.Resources/resourceGroups@2022-09-01' = {
  name: resourceGroupName
  location: location
  tags: {
    'azd-env-name': environmentName
  }
}

// Deploy main resources to the resource group
module main 'main-resources.bicep' = {
  name: 'main-resources'
  scope: rg
  params: {
    location: location
    resourceToken: resourceToken
    resourcePrefix: resourcePrefix
    streamlitServerPort: streamlitServerPort
    streamlitServerAddress: streamlitServerAddress
    pythonUnbuffered: pythonUnbuffered
  }
}

// Outputs
output RESOURCE_GROUP_ID string = rg.id
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = main.outputs.AZURE_CONTAINER_REGISTRY_ENDPOINT
output AZURE_CONTAINER_REGISTRY_NAME string = main.outputs.AZURE_CONTAINER_REGISTRY_NAME
output APPLICATIONINSIGHTS_CONNECTION_STRING string = main.outputs.APPLICATIONINSIGHTS_CONNECTION_STRING
output AZURE_OPENAI_ENDPOINT string = main.outputs.AZURE_OPENAI_ENDPOINT
output CONTAINER_APP_ENDPOINT string = main.outputs.CONTAINER_APP_ENDPOINT
