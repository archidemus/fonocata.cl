import Swiper from "swiper";
import { EffectFade, Autoplay } from "swiper/modules";

// Inicializar Swiper cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", function () {
  // Inicializar Swiper para el carrusel de videos
  const swiperVideos = new Swiper(".swiper-container", {
    modules: [EffectFade],
    loop: true,
    effect: "fade",
    fadeEffect: {
      crossFade: true,
    },
  });

  // Control de reproducción de videos
  const videos = document.querySelectorAll(".swiper-container video");
  let currentVideoIndex = 0;

  function playCurrentVideo() {
    videos.forEach((video, index) => {
      const videoElement = video;
      if (index === currentVideoIndex) {
        videoElement.play();
      } else {
        videoElement.pause();
        videoElement.currentTime = 0;
      }
    });
  }

  videos.forEach((video, index) => {
    video.addEventListener("ended", () => {
      currentVideoIndex = (index + 1) % videos.length;
      swiperVideos.slideTo(currentVideoIndex);
      playCurrentVideo();
    });
  });

  swiperVideos.on("slideChange", () => {
    currentVideoIndex = swiperVideos.activeIndex;
    playCurrentVideo();
  });

  // Inicializar Swiper para el carrusel de clientes
  const swiperClients = new Swiper(".swiper-container-clients", {
    modules: [Autoplay],
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    slidesPerView: 1,
    spaceBetween: 30,
    breakpoints: {
      640: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      1024: {
        slidesPerView: 4,
      },
    },
  });
});
