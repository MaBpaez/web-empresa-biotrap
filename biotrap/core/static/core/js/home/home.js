$(document).ready(function () {

// Animación Header página Home
TweenMax.staggerFrom(".anim1", 1, { opacity: 0, y: -50 }, 0.2);

// init controller
var controller = new ScrollMagic.Controller();

// build tween
var tween = TweenMax.staggerFrom(".animate", 1, { opacity: 0, y: -250, ease: Linear.easeNone }, 0.2);

// build scene Parallax
// new ScrollMagic.Scene({
  // triggerElement: "#parallax1",
  // duration: "200%",
  // triggerHook: "onEnter"
// })
  // .setTween("#parallax1 > div", { y: "80%", ease: Linear.easeNone })
  // .addTo(controller);

// build scene
new ScrollMagic.Scene({
  triggerElement: ".bg-image",
  duration: 400,
  offset: 0
})
  .setTween(tween)
  //.setPin(".animate")
  .addTo(controller);

});
