document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://122.51.185.92/api/summoner';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const summoners = data.data;
            const summonerContainer = document.querySelector('#summonerContainer');

            function displaysummoners(filteredsummoners) {
                summonerContainer.innerHTML = '';
                filteredsummoners.forEach(summoner => {
                    const card = `
                        <div class="summoner-card">
                            <div class="summoner-info">
                                <div class="summoner-title">${summoner.summoner_name}</div>
                                <div class="summoner-pos">解锁时间: ${summoner.summoner_rank}</div>
                                <div class="summoner-desc">描述: ${summoner.summoner_description}</div>
                            </div>
                            <div class="summoner-img-container">
                                <img src="https://game.gtimg.cn/images/yxzj/img201606/summoner/${summoner.summoner_id}.jpg" alt="${summoner.summoner_name}" class="summoner-img">
                            </div>
                        </div>`;
                        summonerContainer.insertAdjacentHTML('beforeend', card);
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filteredsummoners = summoners.filter(summoner => summoner.summoner_name.toLowerCase().includes(searchTerm));
                displaysummoners(filteredsummoners);
            });

            
            displaysummoners(summoners);
        })
        .catch(error => console.error('Error fetching summoner data:', error));
});