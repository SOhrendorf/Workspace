//<script type="text/javascript" src="https://code.jquery.com/jquery-1.7.1.min.js"></script>
setInterval(function() {
    var lastSeen = $('.pane-header .chat-body .emojitext').last().text();
    console.log(Math.floor(Date.now() / 1000) + ", " + lastSeen);
  }, 1000);