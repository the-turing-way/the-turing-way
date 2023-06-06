require('dotenv').config()
const axios = require('axios')
const fs = require('fs');
const https = require('https');
const project_file = require('./crowdin_contributors_report.json')
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
    const contributors_data = project_file.data
    let table = `<table>
    <thead>
      <tr>
        <th>S/N</th>
        <th>Full Name</th>
        <th>Crowdin Username</th>
        <th>Picture</th>
        <th>Words Translated</th>
        <th>Languages</th>
      </tr>
    </thead>
    <tbody>`;

    contributors_data.forEach((contributor_info, index) => {
        const { fullName: fullname, username, avatarUrl } = contributor_info.user
        const { languages, translated: no_of_words_translated } = contributor_info

        const languages_translated = languages.map((lang) => lang.name).join(', ');

        table += `<tr>
      <td>${index + 1}</td>
      <td>${fullname}</td>
      <td>${username}</td>
      <td><img src="${avatarUrl}" alt="Profile Picture" /></td>
      <td>${no_of_words_translated}</td>
      <td>${languages_translated}</td>
    </tr>`;
    });

    table += `</tbody></table>`;

    const filename = 'CROWDIN_CONTRIBUTORS.md';
    fs.writeFile(filename, table, (err) => {
        if (err) {
            console.error(`Error writing file: ${err}`);
        } else {
            console.log(`Markdown file "${filename}" created successfully.`);
        }
    });
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
    // const generate_report_endpoint = TTW_CROWDIN_API_DOMAIN + '/projects/1/reports'
    // const response = await axios.post(
    //     generate_report_endpoint,
    //     {
    //         name: "top-members",
    //         schema: {
    //             unit: 'words',
    //             format: FILE_FORMAT,
    //             dateFrom: "2020-01-01T00:00:00Z",
    //             dateTo: "2023-06-06T00:00:00Z",
    //         }
    //     },
    //     auth,
    // ).then(r => r)

    // const report_id = response.data.data.identifier

    // Report takes less than 10 seconds to generate
    setTimeout(() => {
        // Get project report
        async function processProjectReport() {
            // const get_report_endpoint = TTW_CROWDIN_API_DOMAIN + `/projects/1/reports/${report_id}/download`
            // const report_response = await axios.get(
            //     get_report_endpoint,
            //     auth,
            // ).then(r => r).catch(e => e)

            // const file_download_url = report_response.data.data.url

            // await downloadProjectReport(file_download_url)
            await updateReadme()
        }

        processProjectReport().catch((error) => {
            console.log(error)
            process.exit(1)
        })
    }, WAIT_TIME || 1)
}

start()
    .catch((error) => {
        console.log(error)
        process.exit(1)
    })
