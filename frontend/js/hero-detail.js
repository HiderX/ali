document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const heroId = urlParams.get('id');
    const apiUrl = `http://122.51.185.92/api/heroinfo?id=${heroId}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const hero = data.data;
            const heroInfoContainer = document.querySelector('#heroInfo');
            const heroDetails = `
                <div class="hero-title">${hero.hero_name} - ${hero.title}</div>
                <div class="hero-img-container"><img src="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/${heroId}/${heroId}-bigskin-1.jpg"></div>
                <div class="hero-pos">位置: ${hero.pos}</div>
                <div class="skill-container">
                    <h3 class="hero-skill">技能</h3>
                    ${hero.Skills.map(skill => `
                        <div class="skill">
                            <img src="${skill.img_url}" alt="${skill.skill_name}" class="skill-img">
                            <div class="skill-info">
                                <div><strong>${skill.skill_name}</strong></div>
                                <div class="skill-description">${skill.description}</div>
                                <div>冷却时间: ${skill.cool_down}</div>
                                <div>消耗: ${skill.cost}</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div class="skin-container">
                    <h3 class="hero-skin">皮肤</h3>
                    ${hero.Skin.map(skin => `
                        <div class="skin">
                            <div class="skin-name">${skin.skin_name}</div>
                            <div class="skin-img-container">
                                <img src="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/${heroId}/${heroId}-bigskin-${skin.skin_id}.jpg" alt="${skin.skin_name}" class="skin-img">
                            </div>
                        </div>
                    `).join('')}
                </div>
                `;
            heroInfoContainer.innerHTML = heroDetails;
        })
        .catch(error => console.error('Error fetching hero details:', error));
});