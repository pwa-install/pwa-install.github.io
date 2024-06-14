const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// Function to retrieve the manifest URL from a website with a 5-second timeout
async function fetchManifestUrl(url) {
  try {
    // Fetch the HTML content of the website with a timeout
    const response = await axios.get(url, { timeout: 5000 }); // 5000 milliseconds timeout
    const html = response.data;

    // Load HTML into cheerio
    const $ = cheerio.load(html);

    // Find the <link> element with rel="manifest"
    const manifestLink = $('link[rel="manifest"]').attr('href');

    return manifestLink;
  } catch (error) {
    if (error.code === 'ECONNABORTED') {
      console.error(`Timeout occurred fetching URL: ${url}`);
    } else {
      console.error(`Error fetching the URL ${url}: ${error.message}`);
    }
    return false;
  }
}

// Function to read URLs from file and fetch their manifest URLs
async function fetchManifestsForUrls(filePath) {
  try {
    const data = fs.readFileSync(path.resolve(__dirname, filePath), 'utf8');
    const lines = data.split('\n');
    const outputfile = fs.createWriteStream('result.txt', { flags: 'a' });
    const errorfile = fs.createWriteStream('error.txt', { flags: 'a' });
    const noManifestfile = fs.createWriteStream('noManifest.txt', {
      flags: 'a',
    });

    for (let line of lines) {
      if (line.trim()) {
        const parts = line.split(',');
        const id = parts[0].trim();
        const url = parts[1].trim();
        let manifestUrl = await fetchManifestUrl(url);
        if (manifestUrl === false) {
          errorfile.write(`${url}\n`);
        } else if (manifestUrl) {
          manifestUrl = `${url}${manifestUrl}`;
          outputfile.write(`${url}, ${manifestUrl}\n`);
        } else {
          noManifestfile.write(`${url}\n`);
        }
        console.log(`ID: ${id}, URL: ${url}, Manifest URL: ${manifestUrl}`);
      }
    }
  } catch (error) {
    console.log(`$`);
  }
}

// Path to the text file with URLs
const filePath = 'example.txt'; // Ensure this path is correct

fetchManifestsForUrls(filePath);
