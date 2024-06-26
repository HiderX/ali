document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const teamName = urlParams.get('name');
    const apiUrl = `http://122.51.185.92/api/teaminfo?name=${teamName}`;

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const teamInfo = data.teamInfo[0];
        const teamStatContainer = document.querySelector('#teamStatContainer');
        const teamStatTableBody = document.querySelector('#teamStatTableBody');

        // 在最上方显示战队名
        const teamNameDiv = document.createElement('div');
        teamNameDiv.className = 'team-name';
        teamNameDiv.innerHTML = `<h2>战队名称: ${teamInfo.team_name}</h2>`;
        teamStatContainer.appendChild(teamNameDiv);

        // 创建表格行
        const teamRow = document.createElement('tr');
        teamRow.innerHTML = `
            <td>${teamInfo.total_games}</td>
            <td>${(teamInfo.average_win_rate * 100).toFixed(2)}%</td>
            <td>${teamInfo.average_kda}</td>
            <td>${teamInfo.average_kills}</td>
            <td>${teamInfo.average_deaths}</td>
            <td>${teamInfo.average_assists}</td>
            <td>${teamInfo.average_gold}</td>
            <td>${teamInfo.average_push_tower}</td>
            <td>${teamInfo.average_kill_big_dragon}</td>
            <td>${teamInfo.average_kill_tyrant}</td>
            <td>${teamInfo.average_kill_dark_tyrant}</td>
            <td>${teamInfo.average_kill_prophet_dragon}</td>
            <td>${teamInfo.average_kill_shadow_dragon}</td>
            <td>${teamInfo.average_kill_storm_dragon_king}</td>`;
        teamStatTableBody.appendChild(teamRow);
    })
    .catch(error => console.error('Error fetching team data:', error));
});
