document.addEventListener("scroll", () => {
    if (window.scrollY > 0) {
      document.querySelector(".topBar").classList.add("active");
      document.querySelector(".navbar").classList.add("active");
      // document.querySelector(".social-nav").classList.add("hide")

    } else {
      document.querySelector(".topBar").classList.remove("active");
      document.querySelector(".navbar").classList.remove("active");
      // document.querySelector(".social-nav").classList.remove("hide");



    }
  });
  
  document.addEventListener("load", () => {
    if (window.scrollY > 0) {
      document.querySelector(".topBar").classList.add("active");
      document.querySelector(".navbar").classList.add("active");
      // document.querySelector(".social-nav").classList.add("hide")

    } else {
      document.querySelector(".topBar").classList.remove("active");
      document.querySelector(".navbar").classList.remove("active");
      // document.querySelector(".social-nav").classList.remove("hide");


    }
  });

  