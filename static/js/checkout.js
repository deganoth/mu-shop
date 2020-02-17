

// Create a Stripe client.
var stripe = Stripe('pk_test_eiyG5GQV9N5gDT4SGZyTsQCz00w9hz14DU');

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

// Create an instance of the card Element.
//var card = elements.create('card', {style: style});
var cardNumber = elements.create('cardNumber', {style: style});
var cardExpiry = elements.create('cardExpiry', {style: style});
var cardCvc = elements.create('cardCvc', {style: style});
var postalCode = elements.create('postalCode', {style: style});

// IMPORTANT! target the bootstrap and django created id names and chnage them to the stripe accepted div id names.
// Stripe id names for card elements must be in a <div> html element.  
cardNumber.mount('#card-number');
cardExpiry.mount('#card-expiry');
cardCvc.mount('#card-cvc');
postalCode.mount('#card-post-code');

// Handle real-time validation errors from the card Element.
cardNumber && cardExpiry && cardCvc && postalCode.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});


// Handle form submission.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();

  stripe.createToken(cardNumber).then(function(result) {
    if (result.error) {
      // Inform the user if there was an error.
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(result.token);
    }
  });
});

// Submit the form with the token ID. In our case, we called it "stripe_id"
function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('payment-form');
  var stripeInput = document.createElement('input');
  stripeInput.setAttribute('type', 'hidden');
  stripeInput.setAttribute('name', 'stripe_id');
  stripeInput.setAttribute('value', token.id);
  form.appendChild(stripeInput);

  // Submit the form
  form.submit();
}


