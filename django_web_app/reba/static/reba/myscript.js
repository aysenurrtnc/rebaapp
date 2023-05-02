function disp_prompt() {
  var youtubeUrl = prompt(
    "Please enter the YouTube URL:",
    "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
  );
  var videoId = extractVideoId(youtubeUrl);
  var iframeSrc = "https://www.youtube.com/embed/" + videoId;

  document.getElementById("video").src = iframeSrc;
}

function extractVideoId(url) {
  var videoId = url.split("v=")[1];
  var ampersandPos = videoId.indexOf("&");
  if (ampersandPos !== -1) {
    videoId = videoId.substring(0, ampersandPos);
  }
  return videoId;
}
function video() {
  var defaultVideoId = "cbQ50EAbEJQ"; // Replace with the actual default video ID
  var defaultIframeSrc = "https://www.youtube.com/embed/" + defaultVideoId;
  document.getElementById("video").src = defaultIframeSrc;
}
