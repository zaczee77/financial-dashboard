async function fetchMarketData() {
    const response = await fetch('/api/market-data');
    const data = await response.json();
    const marketDataDiv = document.getElementById('market-data');
    marketDataDiv.innerHTML = '<h2>Market Data (Last 30 Days)</h2><pre>' + JSON.stringify(data, null, 2) + '</pre>';
}

async function fetchNews() {
    const response = await fetch('/api/news');
    const newsData = await response.json();
    const newsDiv = document.getElementById('news');
    newsDiv.innerHTML = '<h2>Latest News</h2><ul>' + newsData.map(item => `<li><a href="${item.link}" target="_blank">${item.title}</a></li>`).join('') + '</ul>';
}

fetchMarketData();
fetchNews();
