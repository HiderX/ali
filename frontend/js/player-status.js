document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const playerName = urlParams.get('name');
    const apiUrl = `http://122.51.185.92/api/player?name=${playerName}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const playerInfo = data.playerInfo;
            const playerStatContainer = document.querySelector('#playerStatContainer');
            const playerStatTableBody = document.querySelector('#playerStatTableBody');

            // 显示选手名
            const playerNameDiv = document.createElement('div');
            playerNameDiv.className = 'player-name';
            playerNameDiv.innerHTML = `<h2>${playerInfo[0].team_player_name}</h2>`;
            playerStatContainer.appendChild(playerNameDiv);

            // 插入比赛信息表格行
            playerInfo.forEach(match => {
                const matchRow = document.createElement('tr');
                matchRow.innerHTML = `
                    <td>${new Date(match.start_time).toLocaleString()}</td>
                    <td>${match.is_win ? '胜利' : '失败'}</td>
                    <td>${match.hero_name}</td>
                    <td>${match.summoner_name}</td>
                    <td>${match.camp_color}</td>
                    <td>${match.participation_rate}%</td>
                    <td>${match.is_mvp ? '是' : '否'}</td>
                    <td>${match.mvp_score}</td>
                    <td>${match.kill_num}</td>
                    <td>${match.assist_num}</td>
                    <td>${match.death_num}</td>
                    <td>${match.kda}</td>
                    <td>${match.gold}</td>
                    <td>${match.hurt_total}</td>
                    <td>${match.be_hurt_total}</td>
                    <td>${match.hurt_to_hero_total}</td>
                    <td>${match.be_hurt_by_hero_total}</td>`;
                playerStatTableBody.appendChild(matchRow);
            });
        })
        .catch(error => console.error('Error fetching player data:', error));
});