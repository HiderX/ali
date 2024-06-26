document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://122.51.185.92/api/ming';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const mings = data.data;
            const mingContainer = document.querySelector('#mingContainer');

            function displaymings(filteredmings) {
                mingContainer.innerHTML = '';
                filteredmings.forEach(ming => {
                    const card = `
                        <div class="ming-card">
                            <div class="ming-info">
                                <div class="ming-name">${ming.ming_name}</div>
                                <div class="ming-type">种类: ${ming.ming_type}</div>
                                <div class="ming-grade">等级: ${ming.ming_grade}</div>
                                <div class="ming-des">效用: ${ming.ming_des}</div>
                            </div>
                            <div class="ming-img-container">
                                <img src="https://tgatvdown.qq.com/tgatv/smobahelper/real_time_data/mingwen/${ming.ming_id}.png" alt="${ming.ming_name}" class="ming-img">
                            </div>
                        </div>`;
                    mingContainer.insertAdjacentHTML('beforeend', card);
                });
            }

            document.getElementById('searchInput').addEventListener('input', function () {
                const searchTerm = this.value.toLowerCase();
                const filteredmings = mings.filter(ming => 
                    ming.ming_name.toLowerCase().includes(searchTerm) || 
                    ming.ming_type.toLowerCase().includes(searchTerm) ||
                    ming.ming_grade==searchTerm
                );
                displaymings(filteredmings);
            });

            displaymings(mings);
        })
        .catch(error => console.error('Error fetching ming data:', error));
});