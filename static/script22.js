// Type of comp selection code
document.querySelector('#type_comp').addEventListener("change", function(e){
    if (e.target.value === "a") {
        document.querySelector(".rib-field").style.display = "block";
        document.querySelector("#rib_pia").setAttribute("required", "required")
        document.querySelector(".spouse-field").style.display = "none";
        document.querySelector("#spouse_nh_pia").value = "";
        document.querySelector(".dnh-field").style.display = "none";
        document.querySelector(".dnh-field").value = "";
        document.querySelector(".rib-lim-ques").style.display = "none";
        document.querySelector("#rib_lim").selectedIndex = 0;
        document.querySelector(".rd-rib").style.display = "none";
        document.querySelector(".rd-rib").value = "";
        document.querySelector(".gp-ques").style.display = "none";
        document.querySelector("#spouse_nh_pia").removeAttribute("required")
        document.querySelector("#rib_lim").removeAttribute("required")

    } else if (e.target.value === "b") {
        document.querySelector(".spouse-field").style.display = "block";
        document.querySelector("#spouse_nh_pia").setAttribute("required", "required")
        document.querySelector("#rib_pia").removeAttribute("required")
        document.querySelector(".rib-field").style.display = "none";
        document.querySelector("#rib_pia").value = "";
        document.querySelector(".dnh-field").style.display = "none";
        document.querySelector(".dnh-field").value = "";
        document.querySelector(".rib-lim-ques").style.display = "none";
        document.querySelector("#rib_lim").selectedIndex = 0;
        document.querySelector(".rd-rib").style.display = "none";
        document.querySelector(".rd-rib").value = "";
        document.querySelector(".gp-ques").style.display = "none";
        document.querySelector("#rib_lim").removeAttribute("required")
    } else if (e.target.value === "d") {
        document.querySelector(".dnh-field").style.display = "block";
        document.querySelector("#rib_lim").setAttribute("required", "required")
        document.querySelector("#deceased_nh_pia").setAttribute("required", "required")
        document.querySelector("#gp_ques").setAttribute("required", "required")
        document.querySelector(".rib-lim-ques").style.display = "block";
        document.querySelector(".gp-ques").style.display = "block";
        document.querySelector(".spouse-field").style.display = "none";
        document.querySelector(".spouse-field").value = "";
        document.querySelector(".rib-field").style.display = "none";
        document.querySelector(".rib-field").value = "";
        document.querySelector("#spouse_nh_pia").removeAttribute("required")
        document.querySelector("#rib_pia").removeAttribute("required")

    } else if (e.target.value === "dual_ab") {
        document.querySelector(".rib-field").style.display = "block";
        document.querySelector(".spouse-field").style.display = "block";
        document.querySelector("#rib_pia").setAttribute("required", "required")
        document.querySelector("#spouse_nh_pia").setAttribute("required", "required")
        document.querySelector(".dnh-field").style.display = "none";
        document.querySelector("#deceased_nh_pia").value = "";
        document.querySelector(".rib-lim-ques").style.display = "none";
        document.querySelector("#rib_lim").selectedIndex = 0;
        document.querySelector(".rd-rib").style.display = "none";
        document.querySelector(".rd-rib").value = "";
        document.querySelector(".gp-ques").style.display = "none";
        document.querySelector("#rib_lim").removeAttribute("required")
        document.querySelector("#deceased_nh_pia").removeAttribute("required")

    }  else if (e.target.value === "w") {
        document.querySelector(".dnh-field").style.display = "block";
        document.querySelector(".gp-ques").style.display = "block";
        document.querySelector("#gp_ques").setAttribute("required", "required")
        document.querySelector(".spouse-field").style.display = "none";
        document.querySelector(".spouse-field").value = "";
        document.querySelector(".rib-field").style.display = "none";
        document.querySelector(".rib-field").value = "";
        document.querySelector("#rib_pia").removeAttribute("required")
        document.querySelector("#spouse_nh_pia").removeAttribute("required")
        document.querySelector("#rib_lim").removeAttribute("required")

    }

});

// Did deceased NH receive reduced rib question
document.querySelector('#rib_lim').addEventListener("change", function(e){
  if(e.target.value === "y") {
    document.querySelector(".rd-rib").style.display = "block";
    document.querySelector("#reduced_nh_mba").setAttribute("required", "required")
  } else {
    document.querySelector(".rd-rib").style.display = "none";
    document.querySelector("#reduced_nh_mba").value = "";
    document.querySelector("#reduced_nh_mba").removeAttribute("required")
  }

});


document.querySelector('#gp_ques').addEventListener("change", function(e){
  if(e.target.value === "y") {
    document.querySelector(".gp-amt").style.display = "block";
    document.querySelector("#gp_amt").setAttribute("required", "required")
  } else {
    document.querySelector(".gp-amt").style.display = "none";
    document.querySelector("#gp_amt").value = "";
    document.querySelector("#gp_amt").removeAttribute("required")
  }

});

// Protective filing question
document.querySelector('#prot_date').addEventListener("change", function(e){
    if(e.target.value === "y") {
      document.querySelector(".prot-month-field").style.display = "block";
      document.querySelector("#prot_month").setAttribute("required", "required")
    } else {
      document.querySelector(".prot-month-field").style.display = "none";
      document.querySelector("#prot_month").removeAttribute("required")
    }
});

// Reset Button
document.querySelector("#reset").addEventListener("click", function(){
    document.querySelector(".prot-month-field").style.display = "none";
    document.querySelector(".rd-rib").value = "";
    document.querySelector(".spouse-field").style.display = "none";
    document.querySelector(".spouse-field").value = "";
    document.querySelector(".rib-field").style.display = "none";
    document.querySelector(".rib-field").value = "";
    document.querySelector(".dnh-field").style.display = "none";
    document.querySelector(".dnh-field").value = "";
    document.querySelector(".rib-lim-ques").style.display = "none";
    document.querySelector("#rib_lim").selectedIndex = 0;
    document.querySelector(".rd-rib").style.display = "none";
    document.querySelector(".gp-ques").style.display = "none";
    document.querySelector(".gp-amt").style.display = "none";
    document.querySelector(".gp-amt").style.display = "none";
    document.querySelector("#gp_amt").value = "";
    document.querySelector("#prot_month").removeAttribute("required")
    document.querySelector("#reduced_nh_mba").removeAttribute("required")
    document.querySelector("#gp_ques").removeAttribute("required")

})

document.querySelector("#submit").addEventListener('click', function(e){



})

let notValid = function(){

document.querySelector("#prot_month").setAttribute("onInvalid")

}
