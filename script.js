// Function to get customer input
function getCustomerInput(promptMessage) {
    return prompt(promptMessage);
  }
  
  // MotelCustomer object definition
  function MotelCustomer() {
    this.name = getCustomerInput("Enter customer name:");
    this.birthDate = getCustomerInput("Enter birth date (YYYY-MM-DD):");
    this.gender = getCustomerInput("Enter gender:");
    this.roomPreferences = getCustomerInput("Enter room preferences (comma-separated):").split(',').map(preference => preference.trim());
    this.paymentMethod = getCustomerInput("Enter payment method:");

    this.phoneNumber = getCustomerInput("Enter phone number:");
    this.checkInDate = getCustomerInput("Enter check-in date (YYYY-MM-DD):");
    this.checkOutDate = getCustomerInput("Enter check-out date (YYYY-MM-DD):");
  
    // Method to calculate age
    this.calculateAge = function() {
      const today = new Date();
      const birthDate = new Date(this.birthDate);
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDiff = today.getMonth() - birthDate.getMonth();
  
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
  
      return age;
    };
  
    // Method to calculate duration of stay in days
    this.calculateStayDuration = function() {
      const checkIn = new Date(this.checkInDate);
      const checkOut = new Date(this.checkOutDate);
      const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
  
      return Math.round(Math.abs((checkOut - checkIn) / oneDay));
    };
  
    // Method to generate customer description
    this.generateDescription = function() {
      const age = this.calculateAge();
      const stayDuration = this.calculateStayDuration();
  
      return `Name: ${this.name}\nAge: ${age}\nGender: ${this.gender}\nRoom Preferences: ${this.roomPreferences.join(', ')}\nPayment Method: ${this.paymentMethod}\nPhone Number: ${this.phoneNumber}\nCheck-In Date: ${this.checkInDate}\nCheck-Out Date: ${this.checkOutDate}\nDuration of Stay: ${stayDuration} days`;
    };
  }
  
  // Example usage:
  const customer = new MotelCustomer();
  
  // Display customer description
  console.log(customer.generateDescription());
  