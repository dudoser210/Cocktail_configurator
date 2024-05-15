const likeButton = document.querySelector('.list__likes-button');
const likeCount = document.querySelector('.list__likes-count');

likeButton.addEventListener('click', () => {
    // Получаем текущее значение счетчика лайков и увеличиваем на 1
    const currentCount = parseInt(likeCount.textContent, 10);
    likeCount.textContent = currentCount + 1;
});
