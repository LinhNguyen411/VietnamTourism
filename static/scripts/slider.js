document.querySelectorAll('.box').forEach((container) => {
    console.log(container);
    let slide = container.querySelector('.slide')
    let lists = slide.querySelectorAll('.item');
    slide.prepend(lists[lists.length - 1]);
    let buttons = container.querySelector('.buttons')
    buttons.querySelector('.next').onclick = function(){
        let lists = slide.querySelectorAll('.item');
        slide.appendChild(lists[0]);
    }
    buttons.querySelector('.prev').onclick = function(){
        let lists = slide.querySelectorAll('.item');
        slide.prepend(lists[lists.length - 1]);
    }
})
