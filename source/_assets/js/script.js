$(document).ready(function () {
    var menuToggle = $('#js-navigation-menu-button').unbind();
    $('#js-navigation-list').removeClass('navigation__list--show');

    menuToggle.on('click', function (e) {
        e.preventDefault();

        $('#js-navigation-list').slideToggle(function () {
            if ($('#js-navigation-list').is(':hidden')) {
                $('#js-navigation-list').removeAttr('style');
            }
        });
    });

    var subjectSelectField = $('#js-subject select');

    subjectSelectField.on('change', function () {
        $('#js-deadline').hide();
        $('#js-budget').hide();
        $('#js-company-test').hide();

        if (subjectSelectField.val() == "I'm interested in hiring you for a project") {
            $('#js-deadline').show();
            $('#js-budget').show();
        } else if (subjectSelectField.val() == "I'm interested in hiring you full-time") {
            // $('#js-company-test').show();
        }
    }).trigger('change');

    var deadlineOutput = $('#js-deadline output'),
        deadlineInputField = $('#js-deadline input');

    deadlineInputField.on('change mousemove', function () {
        var months = parseInt($(this).val());

        if (months == 0) {
            deadlineOutput.text('Unknown');
        } else if (months == 1) {
            deadlineOutput.text('1 month');
        } else {
            deadlineOutput.text(months + ' month');
        }
    }).trigger('change');

    var form = $('#js-contact-form'),
        form_error_alert = $('#js-contact-form-error'),
        form_sucess_alert = $('#js-contact-form-sucess');

    form.on('submit', function (e) {
        e.preventDefault();

        if (form.validate()) {
            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                data: form.serialize(),
                success: function(data) {
                    if (data.sent === 'ok') {
                        form.hide();
                        form_sucess_alert.show();
                    } else {
                        form.hide();
                        form_error_alert.show();
                    }
                },
                error: function(data) {
                    form.hide();
                    form_error_alert.show();
                }
            });
        }
    })
});
