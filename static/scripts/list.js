let active = 3;
function loadShow(){
    let items = document.querySelectorAll('.slider .item');
    if(items.length < 7){
        let slider = document.querySelector('.slider');
        items.forEach(item => {
            let clone = item.cloneNode(true)
            slider.appendChild(clone)
        })
    }
    items = document.querySelectorAll('.slider .item');
    let stt = 0;
    items[active].style.transform = 'none';
    items[active].style.zIndex = 1;
    items[active].style.filter = 'none';
    items[active].style.opacity = 1;
    for(var i = active + 1;  i < items.length; i++){
        stt++;
        items[i].style.transform = `translateX(${200*stt}px) scale(${1 - 0.2 *stt}) perspective(32px) rotateY(-1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
    stt = 0;
    for(var i = active - 1;  i >= 0; i--){
        stt++;
        items[i].style.transform = `translateX(${-200*stt}px) scale(${1 - 0.2 *stt}) perspective(32px) rotateY(1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
}
loadShow();

document.getElementById('next').onclick = function(){
    let list = document.querySelectorAll('.slider .item');
    document.querySelector('.slider').appendChild(list[0])
    loadShow();
}

document.getElementById('prev').onclick = function(){
    let list = document.querySelectorAll('.slider .item');
    console.log(list.length)
    document.querySelector('.slider').prepend(list[list.length-1])
    loadShow();
}