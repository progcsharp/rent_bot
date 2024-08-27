$(document).ready(function(){


    $('.users__list-item').click(function(){
        $('.overlay').css('display', 'block');
        $('.edit__popup').css('display', 'block');

        let currnetUser = $(this);

        let currnetUserName = currnetUser.find('.user_name').text();
        let currnetUserPhone = currnetUser.find('.user_phone').text();
        let currnetUserPass = currnetUser.find('.user_pass').text();
        let currnetUserCard = currnetUser.find('.user_card').text();
        let currnetUserValue = currnetUser.find('.user_value').text();
        let currnetUserStock = currnetUser.find('.user_stock').text();
        let currnetUserBonuses = currnetUser.find('.user_bonuses').text();
        let currnetUserId = currnetUser.find('.user_id').text();

        $('#editUserName').val(currnetUserName);
        $('#editUserPhone').val(currnetUserPhone);
        $('#editUserPass').val(currnetUserPass);
        $('#editUserCard').val(currnetUserCard);
        $('#editUserValue').val(currnetUserValue);
        $('#editUserStock').val(currnetUserStock);
        $('#editUserBonuses').val(currnetUserBonuses);
        $('#editUserId').val(currnetUserId);
    });

    $('.popup__close').click(function(){
        $('.overlay').css('display', 'none');
        $('.popup').css('display', 'none');
    });





    $('#addUser').click(function(){
        $('.overlay').css('display', 'block');
        $('.add__popup').css('display', 'block');
    });

   $(document).ready(function() {
        $('#dice').on('click', function() {
            $('.dice__img').toggleClass('animate');

            let password = generatePassword(15);
            console.log($('#editUserPass'));
            $('#AddUserPass').val(password);
        });

    });




    function generatePassword(length) {
        var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var password = '';
        for (var i = 0; i < length; i++) {
          password += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return password;
      }


});