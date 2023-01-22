function validateForm() {
  var fName = document.forms['contactForm']['fName'].value;
  var lName = document.forms['contactForm']['lName'].value;
  var email = document.forms['contactForm']['email'].value;
  var phone = document.forms['contactForm']['phone'].value;
  if (fName == '') {
    alert('First name must be filled out');
    return false;
  }
  if (lName == '') {
    alert('Last name must be filled out');
    return false;
  }
  if (email == '') {
    alert('Email must be filled out');
    return false;
  }
  if (phone == '') {
    alert('Phone must be filled out');
    return false;
  }
}

// Hamburger menu function
function hamburger() {
  var menu = document.getElementById('menu-links');
  var logo = document.getElementById('ffc-logo');
  if (menu.style.display === 'block' && logo.style.display === 'none') {
    menu.style.display = 'none';
    logo.style.display = 'block';
  } else {
    menu.style.display = 'block';
    logo.style.display = 'none';
  }
}
