document.addEventListener('DOMContentLoaded', () => {
    // Load the menu when the page is fully loaded
    loadMenu();
    document.getElementById('apply-filters').addEventListener('click', applyFilters);
});

function showSection(sectionId) {
    document.getElementById('home').style.display = 'none';
    document.getElementById('menu').style.display = 'none';
    document.getElementById(sectionId).style.display = 'block';
}



function loadMenu() {
    fetch('/menu/menu.json')
        .then(response => response.json())
        .then(data => {
            const menuContainer = document.getElementById('menu-categories');
            menuContainer.innerHTML = ''; // Очищаем контейнер перед загрузкой новых элементов

            // Проходимся по каждой категории и создаем элементы блюд
            data.categories.forEach(category => {
                const categoryDiv = document.createElement('div');
                categoryDiv.classList.add('menu-category');

                const categoryTitle = document.createElement('h3');
                categoryTitle.textContent = category.name;
                categoryDiv.appendChild(categoryTitle);

                const dishesDiv = document.createElement('div');
                dishesDiv.classList.add('menu-items');

                // Проходим по каждому блюду и добавляем его в DOM
                category.dishes.forEach(dish => {
                    const dishCard = document.createElement('div');
                    dishCard.classList.add('menu-item');
                    
                    // Здесь мы передаем параметры цены и новизны через data-* атрибуты
                    dishCard.setAttribute('data-price', dish.price);
                    dishCard.setAttribute('data-new', dish.isNew);

                    dishCard.innerHTML = `
                        <img src="${dish.imageUrl}" alt="${dish.name}" class="dish-image">
                        <h4>${dish.name}</h4>
                        <p>${dish.description}</p>
                        <p class="price">Цена: ${dish.price} руб.</p>
                    `;

                    dishesDiv.appendChild(dishCard);
                });

                categoryDiv.appendChild(dishesDiv);
                menuContainer.appendChild(categoryDiv);
            });
        })
        .catch(error => console.error('Ошибка загрузки меню:', error));
}

function applyFilters() {
    const minPrice = parseFloat(document.getElementById('min-price').value) || 0;
    const maxPrice = parseFloat(document.getElementById('max-price').value) || Infinity;
    const newDishesOnly = document.getElementById('new-dishes').checked;

    // Получаем все элементы блюд
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach(item => {
        const itemPrice = parseFloat(item.getAttribute('data-price')); // Правильный атрибут data-price
        const isNewDish = item.getAttribute('data-new') === 'true';    // Правильный атрибут data-new

        // Проверяем условия фильтрации
        let showItem = true;

        if (itemPrice < minPrice || itemPrice > maxPrice) {
            showItem = false;
        }

        if (newDishesOnly && !isNewDish) {
            showItem = false;
        }

        // Показываем или скрываем блюдо в зависимости от условий
        item.style.display = showItem ? 'block' : 'none';
    });
}

document.addEventListener('DOMContentLoaded', () => {
    let currentAdIndex = 0;
    const ads = document.querySelectorAll('.ad-image');
    const totalAds = ads.length;

    function showAd(index) {
        ads.forEach((ad, i) => {
            ad.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextAd() {
        currentAdIndex = (currentAdIndex + 1) % totalAds;
        showAd(currentAdIndex);
    }

    function prevAd() {
        currentAdIndex = (currentAdIndex - 1 + totalAds) % totalAds;
        showAd(currentAdIndex);
    }

    // Event listeners for buttons
    document.getElementById('next-ad').addEventListener('click', nextAd);
    document.getElementById('prev-ad').addEventListener('click', prevAd);

    // Automatically switch ads every 10 seconds
    setInterval(nextAd, 10000);

    // Show the first ad on page load
    showAd(currentAdIndex);
});
