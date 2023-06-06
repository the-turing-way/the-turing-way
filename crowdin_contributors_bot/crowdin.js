require('dotenv').config()
const axios = require('axios')

const CONFIG = process.env

const token = CONFIG.CROWDIN_TOKEN
const url = `https://turingway.api.crowdin.com/api/v2/projects/1/reports`
const auth = {
    headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    },
}

async function start() {
    const response = await axios.post(
        url,
        {
            name: "top-members",
            schema: {
                unit: 'words',
                format: 'xlsx',
                dateFrom: "2020-01-01T00:00:00Z",
                dateTo: "2023-06-06T00:00:00Z",
            }
        },
        auth,
    ).then(r => r).catch(e => e)

    console.log(response.data)
    // console.log(response.response.data)
    const reportId = response.data.data.identifier

    // Waiting for report to be generated
    setTimeout(async() => {
        const reportUrl = `https://turingway.api.crowdin.com/api/v2/projects/1/reports/${reportId}/download`
        // const reportUrl = `https://turingway.api.crowdin.com/api/v2/users`
        const reportResponse = await axios.get(
            reportUrl,
            auth,
        ).then(r => r).catch(e => e)
        
        console.log(reportResponse.response)
    }, 10000)
}

start()