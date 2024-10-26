function validatePhoneNumber() {
    const phoneInput = document.querySelector('input[name="phone_number"]');
    const phoneNumber = phoneInput.value;
    const phonePattern = /^(07|01)\d{8}$/;

    if (!phonePattern.test(phoneNumber)) {
        alert("Invalid phone number. Use '07' or '01' and 10 digits.");
        return false;
    }
    return true;
}