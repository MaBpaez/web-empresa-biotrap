// init controller
var controller = new ScrollMagic.Controller();

// build scenes
new ScrollMagic.Scene({
  triggerElement: "#parallax1",
  duration: "200%",
  triggerHook: "onEnter"
})
  .setTween("#parallax1 > div", { y: "80%", ease: Linear.easeNone })
  //.setPin("#parallax1")
  .addTo(controller);
