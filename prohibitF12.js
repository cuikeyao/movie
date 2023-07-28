//禁用键盘快捷方式
document.addEventListener('keydown', function(event){
    if (event.key == 'F12' || (event.ctrlKey && event.shiftKey && event.key === 'I') || (event.ctrlKey && event.shiftKey && event.key === 73)) {
        event.preventDefault();
    }
});

//禁用右键菜单
document.addEventListener('contextmenu', function(event){
    event.preventDefault();
})

// 监听控制台打开事件并重定向
window.addEventListener('devtoolschange', function (event) {
    window.location.href = 'https://video.cuikeyao.com';
})

//检测是否有打开的控制台
setInterval(function () {
    if (window.devtools) {
        window.location.href = 'https://video.cuikeyao.com';
    }
}, 100);