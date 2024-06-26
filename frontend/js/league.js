document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://122.51.185.92/api/league?year=';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const leagues = data.league;
            const leagueContainer = document.querySelector('#leagueContainer');

            function displayLeagues(filteredLeagues) {
                leagueContainer.innerHTML = '';
                filteredLeagues.forEach(league => {
                    const card = `
                        <div class="league-card" onclick="window.location.href='match.html?league_id=${league.league_id}'">
                            <img src="${league.league_icon}" alt="${league.league_name}">
                            <div class="league-title">${league.league_name}</div>
                            <div class="league-pos">开始时间: ${new Date(league.start_time).toLocaleDateString()}</div>
                            <div class="league-pos">结束时间: ${new Date(league.end_time).toLocaleDateString()}</div>
                        </div>`;
                    leagueContainer.insertAdjacentHTML('beforeend', card);
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filteredLeagues = leagues.filter(league => league.league_name.toLowerCase().includes(searchTerm) ||
                    league.league_type_name.toLowerCase().includes(searchTerm) ||
                    league.year.toString().includes(searchTerm));
                displayLeagues(filteredLeagues);
            });

            displayLeagues(leagues);
        })
        .catch(error => console.error('Error fetching league data:', error));
});