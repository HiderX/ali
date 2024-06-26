document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://122.51.185.92/api/hero';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const heroes = data.data;
            const heroContainer = document.querySelector('#heroContainer');

            function displayHeroes(filteredHeroes) {
                heroContainer.innerHTML = '';
                filteredHeroes.forEach(hero => {
                    const card = `
                        <div class="hero-card" data-id="${hero.hero_id}">
                        <div class="hero-info">
                        <div class="hero-title">${hero.hero_name}</div>
                        <div class="hero-pos">称号: ${hero.title}</div>
                        <div class="hero-pos">位置: ${hero.pos}</div>
                        </div>
                            <div class="hero-avatar">
                                <img src="https://game.gtimg.cn/images/yxzj/img201606/heroimg/${hero.hero_id}/${hero.hero_id}.jpg" alt="${hero.hero_name}">
                            </div>
                        </div>`;
                    heroContainer.insertAdjacentHTML('beforeend', card);
                });

                document.querySelectorAll('.hero-card').forEach(card => {
                    card.addEventListener('click', function () {
                        const heroId = this.getAttribute('data-id');
                        window.location.href = `hero_detail.html?id=${heroId}`;
                    });
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filteredHeroes = heroes.filter(hero =>
                    hero.hero_name.toLowerCase().includes(searchTerm) ||
                    hero.pos.toLowerCase().includes(searchTerm)
                );
                displayHeroes(filteredHeroes);
            });

            displayHeroes(heroes);
        })
        .catch(error => console.error('Error fetching hero data:', error));
});