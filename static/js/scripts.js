$(function() {
  var formAnimatedInput = $('.form-animate-fields .form-input');

  formAnimatedInput.each(function() {
    var $this = $(this);

    $this.on('focus', function() {
      $this.addClass('is-filled');
    });

    $this.on('blur', function() {
      if($this.val().length == 0) {
        $this.removeClass('is-filled');
      }
    });
  });
});
