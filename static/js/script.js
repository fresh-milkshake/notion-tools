function copyText() {
    let text = document.querySelector('.document pre').innerText;
    let temp = document.createElement('textarea');
    temp.value = text;
    document.body.appendChild(temp);
    temp.select();
    // document.execCommand('copy'); deprecated - use navigator.clipboard.writeText() instead
    navigator.clipboard.writeText(text);
    document.body.removeChild(temp);
    let button = document.querySelector('.copy-button');
    button.innerText = 'Text Copied!';
    button.classList.add('copied');
    setTimeout(function () {
        button.innerText = 'Copy to Clipboard';
        button.classList.remove('copied');
    }, 3000);
}

function closeDocument() {
    var cleanedText = document.querySelector(".cleaned-text");
    cleanedText.parentNode.removeChild(cleanedText);
    var copyButton = document.querySelector(".copy-button");
    copyButton.parentNode.removeChild(copyButton);
    var closeButton = document.querySelector(".close-button");
    closeButton.parentNode.removeChild(closeButton);
}
