document.addEventListener('DOMContentLoaded', function() {
    // Add any JavaScript functionality you need
    console.log('Medical Auth System loaded');
    
    // Example: Password match validation
    const password1 = document.querySelector('#id_password1');
    const password2 = document.querySelector('#id_password2');
    
    if (password1 && password2) {
        function validatePassword() {
            if (password1.value !== password2.value) {
                password2.setCustomValidity("Passwords Don't Match");
            } else {
                password2.setCustomValidity('');
            }
        }
        
        password1.onchange = validatePassword;
        password2.onkeyup = validatePassword;
    }
});


// hero section js file 
<script>
document.addEventListener("DOMContentLoaded", function() {
    let slideIndex = 0;
    const slides = document.querySelectorAll(".slide");

    function showSlides() {
        slides.forEach((slide) => {
            slide.style.display = "none";
        });

        slideIndex++;
        if (slideIndex > slides.length) slideIndex = 1;

        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 3000);
    }

    showSlides();
});
</script>
