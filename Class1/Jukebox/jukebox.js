const player = document.getElementById('player');
const playlist = document.getElementById('playlist');
let mediaFiles = [];
let currentIndex = 0;

const mediaRegex = /\.(m4a|mp3|wav|ogg|flac|mp4|webm|mov|m4v)$/i;

async function loadDirectoryMedia() {
  try {
    let filesFound = [];

    // Method 1: Try reading static manifest (playlist.json)
    try {
      const manifestRes = await fetch('./playlist.json');
      if (manifestRes.ok) {
        filesFound = await manifestRes.json();
      }
    } catch (e) {
      console.log('playlist.json not found, falling back to directory scrape...');
    }

    // Method 2: Fallback to HTML directory scraping
    if (filesFound.length === 0) {
      const response = await fetch('./');
      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'text/html');
      const links = Array.from(doc.querySelectorAll('a[href]'));

      filesFound = links
        .map(a => a.getAttribute('href'))
        .filter(href => {
          if (!href || href.startsWith('http') || href.includes('?filename=')) return false;
          if (href.endsWith('.html') || href.endsWith('.js') || href.endsWith('.json')) return false;
          return mediaRegex.test(href);
        });
    }

    if (filesFound.length === 0) {
      playlist.innerHTML = '<li>No audio or video files found in directory.</li>';
      return;
    }

    mediaFiles = filesFound.map(f => decodeURIComponent(f));
    renderPlaylist();
    loadMedia(0, false);
  } catch (err) {
    console.error('Error reading IPFS directory:', err);
    playlist.innerHTML = '<li>Failed to load media list.</li>';
  }
}

function renderPlaylist() {
  playlist.innerHTML = '';
  mediaFiles.forEach((file, index) => {
    const li = document.createElement('li');
    const fileName = file.split('/').pop();
    const ext = fileName.split('.').pop().toLowerCase();
    
    li.innerHTML = `<span>${index + 1}. ${fileName}</span> <span class="badge">${ext}</span>`;
    li.onclick = () => loadMedia(index, true);
    playlist.appendChild(li);
  });
}

function loadMedia(index, shouldPlay = true) {
  currentIndex = index;
  player.src = mediaFiles[index];

  Array.from(playlist.children).forEach((li, i) => {
    li.classList.toggle('active', i === index);
  });

  if (shouldPlay) {
    player.play().catch(e => console.log('Autoplay blocked:', e));
  }
}

player.addEventListener('ended', () => {
  let nextIndex = currentIndex + 1;
  if (nextIndex < mediaFiles.length) {
    loadMedia(nextIndex, true);
  }
});

loadDirectoryMedia();
