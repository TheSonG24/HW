const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;


// Middleware для обработки JSON
app.use(express.json());

// Подключение папки с статическими файлами
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'menu'))); // Добавили папку 'menu' для статических файлов

// Главная страница
app.get('/', (req, res) => {
  res.send('Добро пожаловать на сайт ресторана!');
});

// Маршрут для загрузки меню
app.get('/load-menu', (req, res) => {
  res.sendFile(path.join(__dirname, 'menu', 'menu.json'));
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`Сервер запущен на http://localhost:${PORT}`);
});

