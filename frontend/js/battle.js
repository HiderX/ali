document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const matchId = urlParams.get('match_id');
    const apiUrl = `http://122.51.185.92/api/battle?match_id=${matchId}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const battles = data.battle;
            const battleContainer = document.querySelector('#battleContainer');

            function groupBattlesBySeq(battles) {
                const grouped = {};
                battles.forEach(battle => {
                    if (!grouped[battle.battle_seq]) {
                        grouped[battle.battle_seq] = [];
                    }
                    grouped[battle.battle_seq].push(battle);
                });
                return grouped;
            }

            function displayBattles(groupedBattles) {
                battleContainer.innerHTML = '';
                for (const seq in groupedBattles) {
                    const battles = groupedBattles[seq];
                    const card = document.createElement('div');
                    card.className = 'battle-card';
                    let battleHtml = `<div class="battle-seq">第${seq}局</div>`;
                    battleHtml += `
                        <div class="team-section">
                            <table class="battle-table">
                                <thead>
                                    <tr>
                                        <th>阵营</th>
                                        <th>队伍</th>
                                        <th>是否获胜</th>
                                        <th>击杀数</th>
                                        <th>助攻数</th>
                                        <th>死亡数</th>
                                        <th>KDA</th>
                                        <th>金币数</th>
                                        <th>推塔数</th>
                                        <th>大龙数</th>
                                        <th>暴君数</th>
                                        <th>黑暗暴君数</th>
                                        <th>预言龙数</th>
                                        <th>暗影暴君数</th>
                                        <th>风暴龙王数</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    ${battles.map(battle => `
                                    <tr>
                                        <td>${battle.camp === 1 ? '红' : '蓝'}</td>
                                        <td>${battle.team_name}</td>
                                        <td>${battle.is_win ? '是' : '否'}</td>
                                        <td>${battle.kill_num}</td>
                                        <td>${battle.assist_num}</td>
                                        <td>${battle.death_num}</td>
                                        <td>${battle.kda}</td>
                                        <td>${battle.gold}</td>
                                        <td>${battle.push_tower_num}</td>
                                        <td>${battle.kill_big_dragon_num}</td>
                                        <td>${battle.kill_tyrant_num}</td>
                                        <td>${battle.kill_dark_tyrant_num}</td>
                                        <td>${battle.kill_prophet_dragon_num}</td>
                                        <td>${battle.kill_shadow_dragon_num}</td>
                                        <td>${battle.kill_storm_dragon_king_num}</td>
                                    </tr>
                                    `).join('')}
                                </tbody>
                            </table>
                        </div>
                    `;
                    card.innerHTML = battleHtml;
                    card.addEventListener('click', function() {
                        window.location.href = `battle_player.html?battle_id=${battles[0].battle_id}`;
                    });
                    battleContainer.appendChild(card);
                }
            }

            const groupedBattles = groupBattlesBySeq(battles);
            displayBattles(groupedBattles);
        })
        .catch(error => console.error('Error fetching battle data:', error));
});