const allImg = ['20260119_104622.jpg','IMG_20250206_144440.jpg','Profile.png']
let index = 0
const img = document.querySelector('.img-profile')
setInterval(() => {
    img.style.opacity = 0
    setTimeout(() =>{
        index = (index + 1) % allImg.length
        img.src = '/static/images/imgProfile/'+ allImg[index]
        img.style.opacity = 1
    }, 1000)
}, 3000)

const year = new Date().getFullYear()
document.querySelector('#footer-year').innerText =`© ${year}`

let linkedin = document.querySelector('.linkedin-logo')
linkedin.setAttribute('href','https://www.linkedin.com/in/%C4%91%E1%BA%B7ng-ph%C3%BAc-315329372/' +
    '\n')

let github = document.querySelector('.github-logo')
github.setAttribute('href','https://github.com/mphuc454')
let youtube = document.querySelector('.youtube-logo')
youtube.setAttribute('href','https://www.youtube.com/@phucang5265')
