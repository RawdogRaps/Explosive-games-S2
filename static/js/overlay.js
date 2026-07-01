/**
 * Shared overlay utilities.
 *
 * Every level page that uses a fullscreen overlay can call these helpers
 * instead of reimplementing show/hide logic from scratch.
 */

/**
 * Show a fullscreen overlay element.
 *
 * @param {string} overlayId   - id of the overlay <div>
 * @param {Object} opts
 * @param {string} [opts.message]       - text to display
 * @param {string} [opts.messageColor]  - CSS colour for the text
 * @param {string} [opts.textId]        - id of the <p>/<span> for the message
 * @param {string} [opts.imgSrc]        - if set, show this image
 * @param {string} [opts.imgId]         - id of the <img> element
 * @param {string} [opts.hideGameId]    - id of a game container to hide
 */
function showOverlay(overlayId, opts) {
    opts = opts || {};

    if (opts.hideGameId) {
        document.getElementById(opts.hideGameId).style.visibility = "hidden";
    }

    var overlay = document.getElementById(overlayId);
    overlay.style.display = "flex";

    if (opts.textId && opts.message !== undefined) {
        var textEl = document.getElementById(opts.textId);
        textEl.innerText = opts.message;
        if (opts.messageColor) {
            textEl.style.color = opts.messageColor;
        }
    }

    if (opts.imgId && opts.imgSrc) {
        var img = document.getElementById(opts.imgId);
        img.src = opts.imgSrc;
        img.style.display = "block";
    }
}

/**
 * Hide a fullscreen overlay and optionally restore a game container.
 *
 * @param {string} overlayId    - id of the overlay <div>
 * @param {Object} opts
 * @param {string} [opts.showGameId]  - id of a game container to make visible again
 * @param {string} [opts.videoId]     - id of a <video> to pause
 */
function hideOverlay(overlayId, opts) {
    opts = opts || {};

    document.getElementById(overlayId).style.display = "none";

    if (opts.showGameId) {
        document.getElementById(opts.showGameId).style.visibility = "visible";
    }

    if (opts.videoId) {
        var video = document.getElementById(opts.videoId);
        video.pause();
    }
}
