require('dotenv').config()
const axios = require('axios')
const fs = require('fs');
const https = require('https');

const CONFIG = process.env
const WAIT_TIME = parseInt(CONFIG.WAIT_TIME)
const FILE_FORMAT = 'json'
const CROWDIN_AUTH_TOKEN = CONFIG.CROWDIN_TOKEN
const TTW_CROWDIN_API_DOMAIN = `https://turingway.api.crowdin.com/api/v2`
const auth = {
    headers: {
        'Authorization': 'Bearer ' + CROWDIN_AUTH_TOKEN,
        'Content-Type': 'application/json',
    },
}

async function updateReadme() {
    // should update the readme file with the report
}

async function downloadProjectReport(url) {
    const file = fs.createWriteStream('crowdin_contributors_report' + '.' + FILE_FORMAT);
    https.get(url, response => {
        response.pipe(file);
    });

    console.log('Project report downloaded and saved successfully.');
}

async function start() {
    // Generate project report
    const generate_report_endpoint = TTW_CROWDIN_API_DOMAIN + '/projects/1/reports'
    const response = await axios.post(
        generate_report_endpoint,
        {
            name: "top-members",
            schema: {
                unit: 'words',
                format: FILE_FORMAT,
                dateFrom: "2020-01-01T00:00:00Z",
                dateTo: "2023-06-06T00:00:00Z",
            }
        },
        auth,
    ).then(r => r)

    const report_id = response.data.data.identifier

    // Report takes less than 10 seconds to generate
    setTimeout(() => {
        // Get project report
        async function processProjectReport() {
            const get_report_endpoint = TTW_CROWDIN_API_DOMAIN + `/projects/1/reports/${report_id}/download`
            const report_response = await axios.get(
                get_report_endpoint,
                auth,
            ).then(r => r).catch(e => e)

            const file_download_url = report_response.data.data.url
            
            await downloadProjectReport(file_download_url)
            await updateReadme()
        }

        processProjectReport().catch((error) => {
            console.log(error)
            process.exit(1)
        })
    }, WAIT_TIME || 10000)
}

start()
    .catch((error) => {
        console.log(error)
        process.exit(1)
    })
