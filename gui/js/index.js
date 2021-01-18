function update_profiles(profiles) {
  var cont = document.querySelector("div.container");
  cont.innerHTML = ""; // Clears the profiles so all new can be added.

  profiles.forEach(profile => {
    var pro = document.createElement("div");
    pro.innerHTML = profile;
    pro.classList.add("profile-tile");
    pro.setAttribute("profile-name", profile);
    pro.addEventListener("click", function(e) {
      pywebview.api.set_profile(profile);
      var navgroup = document.getElementsByClassName("profile-tile");
      for (var i = 0; i < navgroup.length; i++) {
        navgroup[i].classList.remove("active");
      }
      pro.classList.add("active");
    });
    cont.append(pro);
  });

  pywebview.api.get_active_profile().then(function(name) {
    var div = document.querySelector("[profile-name='" + name + "']");
    div.classList.add("active");
  });
}

domready(function() {
  window.addEventListener('pywebviewready', function() {
    pywebview.api.get_profiles().then(update_profiles);

    var ref = document.querySelector("div.profile-refresh");
    ref.addEventListener("click", function(e) {
      pywebview.api.get_profiles().then(update_profiles);
    });
  });

  LazyLoad.css([
    "css/theme.css",
    "css/index.css",
  ]);
});
