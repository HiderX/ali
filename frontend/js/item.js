document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://122.51.185.92/api/item';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const items = data.data;
            const itemContainer = document.querySelector('#itemContainer');

            function displayitems(filtereditems) {
                itemContainer.innerHTML = '';
                filtereditems.forEach(item => {
                    const card = `
                        <div class="item-card">
                            <div class="item-info">
                                <div class="item-title">${item.item_name}</div>
                                <div class="item-price">价格: ${item.total_price}</div>
                                <div class="item-pos">类型: ${item.pos}</div>
                            </div>
                            <div class="item-img-container">
                                <img src="https://game.gtimg.cn/images/yxzj/img201606/itemimg/${item.item_id}.jpg" alt="${item.item_name}" class="item-img">
                            </div>
                        </div>`;
                        itemContainer.insertAdjacentHTML('beforeend', card);
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filtereditems = items.filter(item => item.item_name.toLowerCase().includes(searchTerm)|| item.pos.toLowerCase().includes(searchTerm) );
                displayitems(filtereditems);
            });

            
            displayitems(items);
        })
        .catch(error => console.error('Error fetching item data:', error));
});