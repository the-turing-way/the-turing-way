require('dotenv').config()
const axios = require('axios')
const fs = require('fs');
const { get } = require('http');
const https = require('https');

const CONFIG = process.env
const FILE_FORMAT = 'csv'
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

async function downloadFileFromUrl(url) {
    const file = fs.createWriteStream('file' + '.' + FILE_FORMAT);

    https.get(url, response => {
        response.pipe(file);
    });

    console.log('File downloaded and saved successfully.');
}

async function start() {
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
    ).then(r => r).catch(e => e)

    console.log(response.status)
    // const report_id = "fb93cf04-486a-4f88-a254-c73d6d520efa"
    const report_id = response.data.data.identifier

    // Report takes less than 10 seconds to generate
    setTimeout(async () => {
        const get_report_endpoint = TTW_CROWDIN_API_DOMAIN + `/projects/1/reports/${report_id}/download`
        const report_response = await axios.get(
            get_report_endpoint,
            auth,
        ).then(r => r).catch(e => e)

        console.log(report_response.data)
        const file_download_url = report_response.data.data.url
        await downloadFileFromUrl(file_download_url)
        await updateReadme()

    }, 10000)
}

start()