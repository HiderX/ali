document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const battleId = urlParams.get('battle_id');
    const apiUrl = `http://122.51.185.92/api/playerbattleinfo?battle_id=${battleId}`;

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const battleInfo = data.battleInfo;
        const playerContainer = document.querySelector('#playerContainer');

        function displayPlayers(team, teamName) {
            const table = document.createElement('table');
            table.className = 'player-table';

            const thead = document.createElement('thead');
            thead.innerHTML = `
                <tr>
                    <th>选手</th>
                    <th>队伍</th>
                    <th>英雄</th>
                    <th>召唤师技能</th>
                    <th>阵营</th>
                    <th>参团率</th>
                    <th>MVP</th>
                    <th>MVP评分</th>
                    <th>击杀数</th>
                    <th>助攻数</th>
                    <th>死亡数</th>
                    <th>KDA</th>
                    <th>金币数</th>
                    <th>总伤害</th>
                    <th>总承伤</th>
                    <th>英雄伤害</th>
                    <th>英雄承伤</th>
                </tr>
            `;
            table.appendChild(thead);

            const tbody = document.createElement('tbody');

            team.forEach(player => {
                const playerIcon = player.player_icon ? player.player_icon : 'media/player_icon.jpg';
                const row = document.createElement('tr');
                row.className = 'player-row';
                row.innerHTML = `
                    <td><img src="${playerIcon}" alt="${player.player_name}" width="50" height="50" /><p>${player.team_player_name.split('.')[1]}</p></td>
                    <td class="player-team">${player.team_player_name.split('.')[0]}</td>
                    <td>${player.hero_name}</td>
                    <td>${player.summoner_name}</td>
                    <td>${player.camp_color}</td>
                    <td>${player.participation_rate}%</td>
                    <td>${player.is_mvp ? '是' : '否'}</td>
                    <td>${player.mvp_score}</td>
                    <td>${player.kill_num}</td>
                    <td>${player.assist_num}</td>
                    <td>${player.death_num}</td>
                    <td>${player.kda}</td>
                    <td>${player.gold}</td>
                    <td>${player.hurt_total}</td>
                    <td>${player.be_hurt_total}</td>
                    <td>${player.hurt_to_hero_total}</td>
                    <td>${player.be_hurt_by_hero_total}</td>
                `;
                row.addEventListener('click', function() {
                    window.location.href = `player_status.html?name=${encodeURIComponent(player.player_name)}`;
                });
                const teamNameElement = row.querySelector('.player-team');
                teamNameElement.addEventListener('click', function(event) {
                    event.stopPropagation();
                    window.location.href = `team_status.html?name=${encodeURIComponent(player.team_player_name.split('.')[0])}`;
                });
                tbody.appendChild(row);
            });

            table.appendChild(tbody);
            const title = document.createElement('h2');
            title.textContent = teamName;
            playerContainer.appendChild(title);
            playerContainer.appendChild(table);
        }

        displayPlayers(battleInfo.WinTeam, '获胜队伍');
        displayPlayers(battleInfo.LoseTeam, '失败队伍');
    })
    .catch(error => console.error('Error fetching player data:', error));
});