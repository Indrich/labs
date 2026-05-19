window.onload = function() {
    var foldBtns = document.getElementsByClassName("fold-button");

    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(e) {
            // Ищем ближайший div с классом one-post
            var post = e.target.closest(".one-post");
            
            if (post) {
                // Переключаем класс
                post.classList.toggle("folded");
                
                // Меняем текст кнопки
                if (post.classList.contains("folded")) {
                    e.target.innerHTML = "развернуть";
                } else {
                    e.target.innerHTML = "свернуть";
                }
            } else {
                console.log("Контейнер .one-post не найден!");
            }
        });
    }
};