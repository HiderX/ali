document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const leagueId = urlParams.get('league_id');
    const apiUrl = `http://122.51.185.92/api/match?league_id=${leagueId}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const matches = data.match;
            const matchContainer = document.querySelector('#matchContainer');

            function displayMatches(matches) {
                matchContainer.innerHTML = '';
                matches.forEach(match => {
                    const card = `
                        <div class="match-card" onclick="window.location.href='battle.html?match_id=${match.match_id}'">
                            <div class="match-content">
                                <div class="team">
                                    <div class="team-name">${match.winning_team_name}</div>
                                </div>
                                <div class="match-info">
                                    <div class="match-title">比赛ID: ${match.match_id}</div>
                                    <div class="match-score">
                                        <span class="team-score">${match.winning_score}</span> : <span class="team-score">${match.losing_score}</span>
                                    </div>
                                    <div class="match-details">BO: ${match.bo}
                                        <div>开始时间: ${new Date(match.start_time).toLocaleString()}</div>
                                        <div>结束时间: ${new Date(match.end_time).toLocaleString()}</div>
                                    </div>
                                </div>
                                <div class="team">
                                    <div class="team-name">${match.losing_team_name}</div>
                                </div>
                            </div>
                        </div>`;
                    matchContainer.insertAdjacentHTML('beforeend', card);
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filteredMatches = matches.filter(match =>
                    match.match_id.toString().includes(searchTerm)||
                    match.winning_team_name.toLowerCase().includes(searchTerm) ||
                    match.losing_team_name.toLowerCase().includes(searchTerm)
                );
                displayMatches(filteredMatches);
            });

            displayMatches(matches);
        })
        .catch(error => console.error('Error fetching match data:', error));
});