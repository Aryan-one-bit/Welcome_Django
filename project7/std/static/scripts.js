// scripts.js - AJAX loader + progress + save handling

function updateProgress(step) {
    const map = {1:25, 2:50, 3:75, 4:100};
    const pct = map[step] || 0;
    $("#progressBar").css("width", pct + "%");
    $("#progressStep").text(step);
}

function loadStep(step) {
    $.get(`/load-step/${step}/`, function(html) {
        $("#stepContent").html(html);
        updateProgress(step);
    }).fail(function(){ alert("Unable to load step " + step); });
}

// saveStep: save and optionally go to next or final
function saveStep(step, next) {
    const form = $(`#step${step}-form`);
    if (!form.length) { console.warn("form not found: step", step); return; }

    const data = form.serialize();

    $.post(`/save-step/${step}/`, data, function(resp) {
        if (resp.status === 'success') {
            if (next === 'final') {
                // after saving step 4 we go to final submission URL
                window.location.href = "/submit-final/";
            } else {
                loadStep(next);
            }
        } else {
            alert("Server returned error saving step " + step);
        }
    }).fail(function(){ alert("Server error while saving step " + step); });
}

// Intercept any form submit inside loaded step (optional safety)
$(document).on('submit', 'form[data-step]', function(e){
    e.preventDefault();
    const step = $(this).data('step');
    // default behavior: move to step+1
    // but buttons call saveStep explicitly so we keep this as fallback:
    saveStep(step, step + 1);
});
