var swiper = new Swiper('.home-swiper', {
  spaceBetween: 30,
  centeredSlides: true,
  loop : true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

var swiper2   = new Swiper('.swiper-container-2', {
  slidesPerView: 5,
  navigation: {
    nextEl: '.swiper-button-next-2',
    prevEl: '.swiper-button-prev-2',
  },
  breakpoints: {
    0:{
      slidesPerView: 3
    },
    640: {
      slidesPerView: 3
    },
    768: {
      slidesPerView: 4
    },
    1024: {
      slidesPerView: 5
    }
  }
});

document.querySelector('nav .hamburger').addEventListener('click', ()=>{
  document.querySelector('nav .hamburger').classList.toggle('active');
  document.querySelector('.sidenav').classList.toggle('active');
})

if(window.innerWidth < 1255){
  window.onscroll = function () {
    if (document.body.scrollTop >= 150 || document.documentElement.scrollTop >= 150) {
      document.querySelector('.search').classList.add('active');
    }
    else{
      document.querySelector('.search').classList.remove('active');
    }
  }
}

var galleryThumbs = new Swiper('.gallery-thumbs', {
  spaceBetween: 10,
  slidesPerView: 4,
  loop: true,
  freeMode: true,
  loopedSlides: 4, //looped slides should be the same
  watchSlidesVisibility: true,
  watchSlidesProgress: true,
});
var galleryTop = new Swiper('.gallery-top', {
  spaceBetween: 10,
  loop: true,
  loopedSlides: 4, //looped slides should be the same
  thumbs: {
    swiper: galleryThumbs,
  },
});