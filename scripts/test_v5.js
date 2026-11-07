
// ========================================================
// DATA MENU MINGGUAN & NOTE RESMI CHEF LUTFI (5 HARI KERJA)
// ========================================================
const weeklyMenuData = {
  senin: {
    title: "Nasi Putih + Daging Ayam Semur Kecap + Tahu Goreng Gurih + Tumis Buncis Jagung Manis + Pisang Cavendish",
    nutrition: "Energi: 685 kkal • Protein: 28 gr • Serat: 5.2 gr",
    notePersiapan: "Kupas bersih wortel dan buncis, potong dadu 2.5 cm seragam untuk ayam fillet, bilas air mengalir 3x.",
    notePengolahan: "Tumis bumbu semur hingga harum tanak berminyak. Suhu inti ayam semur wajib minimal 75°C sebelum angkat.",
    notePemorsian: "Ompreng diisi nasi 150 gr di sekat utama, semur ayam 70 gr di sekat lauk. Pisang diperiksa kematangan & disajikan di sekat buah.",
    items: [
      {
        name: "Daging Ayam Fillet",
        category: "Protein Hewani",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 2.5 cm seragam, bilas air mengalir 3x, tiriskan sempurna sebelum ditimbang.",
        pengolahan: "Tumis bumbu semur sampai tanak, rebus sampai bumbu meresap. Pastikan suhu inti masakan daging minimal 75°C.",
        pemorsian: "Tata pada sekat lauk utama ompreng dengan kuah kental sedang, suhu saji dipertahankan minimal 60°C."
      },
      {
        name: "Tahu Putih Segar",
        category: "Protein Nabati",
        portion: "50 gr / porsi (Total 150 kg)",
        tare: "0.85",
        persiapan: "Potong kotak 3x3 cm, rendam dalam larutan garam & bawang putih 10 menit.",
        pengolahan: "Goreng dalam minyak panas 160°C hingga berkulit keemasan, tiriskan dari minyak berlebih.",
        pemorsian: "Letakkan 1 potong tahu di samping sekat lauk utama berdampingan dengan ayam."
      },
      {
        name: "Buncis & Jagung Manis",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Siangi serat buncis, potong serong 2 cm, pipil jagung manis, cuci bersih dengan air mengalir.",
        pengolahan: "Tumis cepat (stir fry) api besar agar tekstur sayur tetap renyah (crunchy) dan warna hijau segar terjaga.",
        pemorsian: "Porsi sayur ditakar 2 sendok sayur standar (60 gr) pada sekat sayur ompreng."
      },
      {
        name: "Pisang Cavendish",
        category: "Buah Segar",
        portion: "1 pcs (100 gr) / porsi (Total 3.000 pcs)",
        tare: "0.00",
        persiapan: "TIM PERSIAPAN TIDAK MENANGANI BUAH. Langsung diserahkan utuh ke Tim Pemorsian.",
        pengolahan: "TIM PENGOLAHAN TIDAK MENANGANI BUAH. Buah segar dilarang terkena panas dapur.",
        pemorsian: "SOP KHUSUS BUAH SEGAR: Gunakan sarung tangan steril baru, sortir kulit mulus tanpa memar, letakkan di sekat buah paling kering."
      }
    ]
  },
  selasa: {
    title: "Nasi Putih + Daging Sapi Teriyaki Lada Hitam + Tempe Goreng Tepung + Capcay Sayur Segar + Jeruk Manis",
    nutrition: "Energi 710 kkal • Protein 29 gr • Tinggi Zat Besi & Seng",
    notePersiapan: "Iris daging sapi slice tipis melawan serat (slice 2 mm). Rendam saus teriyaki 20 menit.",
    notePengolahan: "Tumis daging api besar cepat agar empuk (tidak alot). Suhu inti daging minimal 75°C.",
    notePemorsian: "Suhu saji 60°C. Jeruk dilap bersih kering dengan kain sanitasi food grade sebelum masuk sekat buah.",
    items: [
      {
        name: "Daging Sapi Slice",
        category: "Protein Hewani",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.85",
        persiapan: "Iris slice tipis melawan serat ketebalan 2 mm, marinasi saus teriyaki 20 menit.",
        pengolahan: "Tumis dengan api besar cepat agar daging empuk dan saus mengental gurih. Suhu minimal 75°C.",
        pemorsian: "Takar 60 gr daging beserta saus teriyaki di sekat lauk utama ompreng."
      },
      {
        name: "Tempe Kedelai Murni",
        category: "Protein Nabati",
        portion: "45 gr / porsi (Total 135 kg)",
        tare: "0.50",
        persiapan: "Potong segitiga tebal 1 cm, celup adonan tepung bumbu ketumbar tipis.",
        pengolahan: "Goreng hingga krispi gurih keemasan, tiriskan minyak secara vertikal.",
        pemorsian: "Letakkan 1 potong tempe krispi berdampingan dengan daging sapi teriyaki."
      },
      {
        name: "Capcay Sayur Segar (Wortel, Kembang Kol, Sawi)",
        category: "Sayuran Segar",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.50",
        persiapan: "Potong kembang kol per kuntum kecil, wortel koin tipis, rendam air garam 5 menit untuk sterilisasi ulat.",
        pengolahan: "Masak kuah kaldu gurih sedikit kental, masukkan kembang kol terakhir agar tidak lembek.",
        pemorsian: "Isi sekat sayur ompreng dengan 1 sendok kuah sayur hangat."
      },
      {
        name: "Jeruk Manis Medan",
        category: "Buah Segar",
        portion: "1 pcs (Total 3.000 pcs)",
        tare: "0.00",
        persiapan: "Khusus Tim Pemorsian. Tim Persiapan tidak mengupas jeruk.",
        pengolahan: "Dilarang dimasak atau dipanaskan.",
        pemorsian: "SOP KHUSUS BUAH: Lap permukaan kulit jeruk dengan lap food-grade steril. Letakkan di sekat buah ompreng."
      }
    ]
  },
  rabu: {
    title: "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam Jagung Bening + Semangka Merah",
    nutrition: "Energi 660 kkal • Protein 26 gr • Tinggi Asam Lemak Omega-3",
    notePersiapan: "QC raba pastikan ikan kembung fillet bebas duri. Sayur bayam dipetik daun muda saja.",
    notePengolahan: "Goreng ikan kembung suhu 170°C hingga renyah. Bayam dimasukkan setelah air mendidih lalu langsung matikan kompor.",
    notePemorsian: "Semangka dipotong segitiga tebal 2 cm di ruang dingin beralas talenan khusus buah, sajikan di sekat buah.",
    items: [
      {
        name: "Ikan Kembung Fillet",
        category: "Protein Hewani",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 menit bilas tiris.",
        pengolahan: "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas sesaat sebelum saji.",
        pemorsian: "Tata 1 potong fillet ikan siram saus asam manis di sekat lauk utama."
      },
      {
        name: "Sayur Bayam Jagung Bening",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Petik daun bayam segar, pipil jagung manis, bilas 3x dengan air dingin.",
        pengolahan: "Masak kuah bening temu kunci, masukkan bayam 1 menit sebelum api dimatikan agar tetap hijau cerah.",
        pemorsian: "Tuang sayur bayam dan jagung di sekat sayur ompreng sesaat sebelum distribusi."
      },
      {
        name: "Semangka Merah Potong",
        category: "Buah Segar",
        portion: "80 gr (1 slice) / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian. Gunakan talenan kuning khusus buah.",
        pengolahan: "Dilarang terkena area kompor/panas.",
        pemorsian: "SOP BUAH SEGAR: Potong bentuk juring/segitiga tebal 2 cm, pastikan biji hitam dibersihkan, letakkan di sekat buah."
      }
    ]
  },
  kamis: {
    title: "Nasi Putih + Ayam Panggang Bumbu Madu + Rolade Tahu Telur + Sayur Labu Siam Wortel Gurih + Melon Cantaloupe",
    nutrition: "Energi 695 kkal • Protein 28 gr • Kaya Vitamin A & Mineral",
    notePersiapan: "Ayam dibelah paha/dada fillet seragam. Labu siam dipotong korek api tebal.",
    notePengolahan: "Panggang oven atau wajan datar suhu 180°C oles madu. Suhu inti ayam wajib minimal 75°C.",
    notePemorsian: "Melon dipotong dadu besar beralas talenan steril. Letakkan rapi di sekat buah ompreng.",
    items: [
      {
        name: "Ayam Panggang Madu",
        category: "Protein Hewani",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Tusuk-tusuk daging ayam agar bumbu madu meresap ke serat terdalam.",
        pengolahan: "Panggang hingga karamelisasi keemasan merata. Suhu inti wajib di atas 75°C.",
        pemorsian: "Tata 1 potong ayam panggang di sekat lauk ompreng."
      },
      {
        name: "Sayur Labu Siam & Wortel",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Kupas labu siam buang getah dengan digosok garam, potong korek api tebal 5 mm.",
        pengolahan: "Tumis dengan kuah santan sangat encer atau kaldu ayam gurih.",
        pemorsian: "Takar 60 gr di sekat sayur ompreng."
      },
      {
        name: "Melon Cantaloupe Segar",
        category: "Buah Segar",
        portion: "80 gr / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian.",
        pengolahan: "Dilarang dipanaskan.",
        pemorsian: "Kupas kulit melon, potong ketebalan 1.5 cm rapi, simpan di wadah sejuk tertutup sebelum masuk ompreng."
      }
    ]
  },
  jumat: {
    title: "Nasi Putih + Telur Balado Pedas Manis + Perkedel Kentang Daging + Sayur Lodeh Labu + Pepaya California",
    nutrition: "Energi 670 kkal • Protein 25 gr • Serat & Enzim Pencernaan Alami",
    notePersiapan: "Kupas telur rebus mulus tanpa cacat putih telur. Kupas kentang dan labu siam bersih.",
    notePengolahan: "Goreng telur hingga berkulit tipis, lumuri sambal balado manis gurih. Suhu inti telur 75°C.",
    notePemorsian: "Pepaya dipotong dadu 3 cm higienis. Ompreng ditutup rapat dan dicek sebelum diantar ke sekolah.",
    items: [
      {
        name: "Telur Ayam Balado",
        category: "Protein Hewani",
        portion: "1 butir (55 gr) (Total 3.000 butir)",
        tare: "0.85",
        persiapan: "Rebus telur 11 menit, rendam air es, kupas mulus tanpa merusak putih telur.",
        pengolahan: "Goreng cepat agar berkulit, aduk rata bersama saus balado bumbu tomat masak tanak.",
        pemorsian: "Letakkan 1 butir telur balado utuh di sekat lauk ompreng."
      },
      {
        name: "Perkedel Kentang Gurih",
        category: "Protein Nabati",
        portion: "40 gr / porsi (Total 120 kg)",
        tare: "0.50",
        persiapan: "Kupas kentang, goreng matang, haluskan selagi hangat dengan bumbu seledri dan bawang goreng.",
        pengolahan: "Bentuk bulat pipih, balur kocokan putih telur, goreng api sedang sampai keemasan.",
        pemorsian: "Letakkan perkedel mendampingi telur balado di sekat ompreng."
      },
      {
        name: "Pepaya California Manis",
        category: "Buah Segar",
        portion: "80 gr / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian.",
        pengolahan: "Dilarang dipanaskan.",
        pemorsian: "SOP BUAH SEGAR: Buang biji hitam, potong dadu 3 cm rapi, sajikan dingin di sekat buah ompreng."
      }
    ]
  }
};

let currentDay = 'senin';
let currentActiveStation = 'persiapan';

// INITIAL STAGING ITEMS
let stagingItems = [
  {
    id: "cart_1",
    timestamp: "11:20:15",
    team: "TIM PERSIAPAN",
    category: "Protein Hewani",
    name: "Daging Ayam Fillet (Batch 1)",
    bruto: 25.85,
    tara: 0.85,
    netto: 25.00,
    catatan: "Sesuai Note Chef: Dadu 2.5 cm, bilas 3x",
    synced: false
  },
  {
    id: "cart_2",
    timestamp: "11:28:40",
    team: "TIM PERSIAPAN",
    category: "Sayuran Segar",
    name: "Wortel Brastagi Potong Koin",
    bruto: 15.50,
    tara: 0.50,
    netto: 15.00,
    catatan: "Sesuai Note Chef: Tebal 4 mm seragam",
    synced: false
  },
  {
    id: "cart_3",
    timestamp: "11:35:10",
    team: "TIM PEMORSIAN",
    category: "Buah Segar",
    name: "Pisang Cavendish Sisir A",
    bruto: 30.00,
    tara: 0.00,
    netto: 30.00,
    catatan: "Sesuai SOP Buah: Sortir kulit mulus steril",
    synced: false
  }
];

document.addEventListener('DOMContentLoaded', () => {
  renderWeeklyMenu();
  renderStagingList();
});

function switchScreen(screenId) {
  ['menu', 'home', 'staging', 'stock'].forEach(s => {
    const sec = document.getElementById('screen-' + s);
    const tabBtn = document.getElementById('tab-btn-' + s);
    if (sec) {
      if (s === screenId) {
        sec.classList.remove('hidden');
      } else {
        sec.classList.add('hidden');
      }
    }
    if (tabBtn) {
      if (s === screenId) {
        tabBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer';
      } else {
        tabBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
      }
    }
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function selectDay(day) {
  currentDay = day;
  document.querySelectorAll('.day-btn').forEach(btn => {
    if (btn.dataset.day === day) {
      btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer';
    } else {
      btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer';
    }
  });

  const heroLabel = document.getElementById('hero-day-label');
  const heroTitle = document.getElementById('hero-menu-title');
  const heroNutrition = document.getElementById('hero-nutrition');
  const cur = weeklyMenuData[day];

  if (heroLabel) heroLabel.innerText = 'Menu Hari ' + day.toUpperCase();
  if (heroTitle) heroTitle.innerText = cur.title;
  if (heroNutrition) heroNutrition.innerText = cur.nutrition;

  renderWeeklyMenu();
}

function selectStationDirective(station) {
  currentActiveStation = station;
  const stations = ['persiapan', 'pengolahan', 'pemorsian'];

  stations.forEach(st => {
    const btn = document.getElementById('directive-btn-' + st);
    if (!btn) return;
    if (st === station) {
      if (st === 'persiapan') {
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-emerald-600 text-white shadow-sm border border-emerald-700 cursor-pointer transition-all';
      } else if (st === 'pengolahan') {
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-amber-600 text-white shadow-sm border border-amber-700 cursor-pointer transition-all';
      } else {
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-blue-600 text-white shadow-sm border border-blue-700 cursor-pointer transition-all';
      }
    } else {
      btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-white text-slate-700 hover:bg-slate-50 border border-slate-200 cursor-pointer transition-all';
    }
  });

  updateStickyNoteContent();
  renderWeeklyMenu();
}

function updateStickyNoteContent() {
  const stickyNote = document.getElementById('sticky-chef-note');
  const title = document.getElementById('note-team-title');
  const body = document.getElementById('note-team-body');
  const cur = weeklyMenuData[currentDay];

  if (!stickyNote || !title || !body || !cur) return;

  if (currentActiveStation === 'persiapan') {
    stickyNote.className = 'note-paper-persiapan p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PERSIAPAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-emerald-950 mb-1">Pedoman Penerimaan & Pembersihan Bahan:</p>' +
      '<p>• ' + cur.notePersiapan + '</p>' +
      '<p>• Kupas bersih bagian luar, pastikan potongan cm presisi seragam untuk efisiensi masak.</p>' +
      '<p>• Cuci tiga kali dengan air mengalir. Setelah ditimbang di stasiun ini, kirim langsung ke Tim Pengolahan.</p>';
  } else if (currentActiveStation === 'pengolahan') {
    stickyNote.className = 'note-paper-pengolahan p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PENGOLAHAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-amber-950 mb-1">Pedoman Suhu & Standar Bumbu:</p>' +
      '<p>• ' + cur.notePengolahan + '</p>' +
      '<p>• Standar Keamanan Pangan BGN: Suhu inti kaldu & daging matang minimal 75°C (cek berkala pakai termometer tusuk).</p>' +
      '<p>• Masak bumbu hingga tanak berminyak. Begitu matang, timbang hasil olahan sebelum diserahkan ke Tim Pemorsian.</p>';
  } else {
    stickyNote.className = 'note-paper-pemorsian p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PEMORSIAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-blue-950 mb-1">Pedoman Ompreng & SOP Buah Segar:</p>' +
      '<p>• ' + cur.notePemorsian + '</p>' +
      '<p>• Suhu saji ompreng dipertahankan minimal 60°C saat dimasukkan ke wadah thermal tertutup.</p>' +
      '<p>• <span class="font-bold text-blue-900 underline">SOP Buah Segar:</span> Dikerjakan higienis dengan sarung tangan steril di ruang sejuk terpisah dari panas kompor.</p>';
  }
}

function renderWeeklyMenu() {
  const container = document.getElementById('menu-items-container');
  if (!container) return;
  container.innerHTML = '';

  const dayData = weeklyMenuData[currentDay];
  if (!dayData || !dayData.items) return;

  dayData.items.forEach(item => {
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-2.5 hover:border-slate-300 transition-all';

    let directiveText = '';
    let directiveBadge = '';
    let directiveBg = '';
    let actionLabel = 'Timbang';

    if (currentActiveStation === 'persiapan') {
      directiveText = item.persiapan;
      directiveBadge = 'NOTE CHEF UNTUK TIM PERSIAPAN:';
      directiveBg = 'note-paper-persiapan text-emerald-950';
      actionLabel = 'Timbang Persiapan';
    } else if (currentActiveStation === 'pengolahan') {
      directiveText = item.pengolahan;
      directiveBadge = 'NOTE CHEF UNTUK TIM PENGOLAHAN:';
      directiveBg = 'note-paper-pengolahan text-amber-950';
      actionLabel = 'Timbang Olahan';
    } else if (currentActiveStation === 'pemorsian') {
      directiveText = item.pemorsian;
      directiveBadge = (item.category === 'Buah Segar') ? 'NOTE SOP KHUSUS BUAH SEGAR:' : 'NOTE CHEF UNTUK PEMORSIAN:';
      directiveBg = 'note-paper-pemorsian text-blue-950';
      actionLabel = 'Timbang Pemorsian';
    }

    const safeName = item.name.replace(/'/g, "\\'");
    const safeCat = item.category.replace(/'/g, "\\'");
    const safeDirective = (directiveText || '').replace(/'/g, "\\'");
    const mappedTeamName = (currentActiveStation === 'persiapan') ? 'TIM PERSIAPAN' : (currentActiveStation === 'pengolahan' ? 'TIM PENGOLAHAN' : 'TIM PEMORSIAN');

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h3 class="text-xs font-bold text-slate-900">' + item.name + '</h3>' +
          '<span class="text-[9px] font-semibold bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded border border-slate-200">' + item.category + '</span>' +
          (item.category === 'Buah Segar' ? '<span class="text-[9px] font-bold bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded">Khusus Pemorsian</span>' : '') +
        '</div>' +
        '<p class="text-[10px] text-slate-500 font-medium mt-0.5">Standar Porsi: ' + item.portion + '</p>' +
      '</div>' +
      '<button onclick="loadMenuItemToWeigh(\'' + safeName + '\', \'' + safeCat + '\', \'' + mappedTeamName + '\', \'' + item.tare + '\', \'' + safeDirective + '\')" class="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold shadow-sm transition-all flex items-center gap-1 cursor-pointer active:scale-95">' +
        '<span>' + actionLabel + '</span>' +
        '<svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>' +
      '</button>' +
    '</div>' +
    '<div class="' + directiveBg + ' p-3 rounded-xl text-xs space-y-1">' +
      '<span class="font-extrabold flex items-center gap-1.5 text-[11px]">' +
        '<span>📌</span>' +
        directiveBadge +
      '</span>' +
      '<p class="text-slate-900 mt-0.5 font-medium leading-relaxed">' + directiveText + '</p>' +
    '</div>';

    container.appendChild(card);
  });
}

function loadMenuItemToWeigh(name, category, team, tare, directive) {
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;

  const inputCat = document.getElementById('input-kategori');
  if (inputCat) inputCat.value = category;

  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = tare || '0.85';

  selectTeam(team);

  const banner = document.getElementById('autofill-banner');
  const bannerText = document.getElementById('autofill-banner-text');
  const directiveElem = document.getElementById('autofill-directive-text');

  if (banner && bannerText && directiveElem) {
    banner.classList.remove('hidden');
    bannerText.innerText = 'Bahan ' + name + ' dimuat untuk ' + team;
    directiveElem.innerHTML = '<span class="font-extrabold block text-slate-900 mb-0.5">NOTE CHEF UNTUK BAHAN INI:</span>' + (directive || 'Lakukan penimbangan sesuai standar porsi.');
  }

  switchScreen('home');
  showToast('Memuat ' + name + ' dengan Note Chef');
}

function dismissAutofillBanner() {
  const banner = document.getElementById('autofill-banner');
  if (banner) banner.classList.add('hidden');
}

function selectTeam(teamName) {
  document.querySelectorAll('.team-chip').forEach(btn => {
    if (btn.dataset.team === teamName) {
      if (teamName === 'TIM PERSIAPAN') {
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-emerald-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      } else if (teamName === 'TIM PENGOLAHAN') {
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-amber-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      } else {
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-blue-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      }
    } else {
      btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer';
    }
  });

  const badge = document.getElementById('current-stage-badge');
  if (badge) {
    if (teamName === 'TIM PERSIAPAN') {
      badge.innerText = 'Penerimaan & Sortir Persiapan';
      badge.className = 'text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full';
    } else if (teamName === 'TIM PENGOLAHAN') {
      badge.innerText = 'Pengolahan Panas (Masak)';
      badge.className = 'text-[10px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded-full';
    } else {
      badge.innerText = 'Pemorsian Distribusi & Buah';
      badge.className = 'text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded-full';
    }
  }
}

function setTare(val) {
  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = val.toFixed(2);
  showToast('Preset Tara disetel: ' + val.toFixed(2) + ' kg');
}

function pickQuickItem(name) {
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;
  showToast('Memilih bahan: ' + name);
}

function onCategoryChanged() {
  const cat = document.getElementById('input-kategori').value;
  const chipContainer = document.getElementById('quick-item-chips');
  if (!chipContainer) return;

  const quickMap = {
    "Protein Hewani": ["Daging Ayam Fillet", "Daging Sapi Slice", "Ikan Kembung Fillet", "Telur Ayam"],
    "Protein Nabati": ["Tahu Putih Segar", "Tempe Kedelai Murni", "Rolade Tahu Telur"],
    "Sayuran Segar": ["Wortel Brastagi", "Buncis Manis", "Kembang Kol", "Bayam Segar", "Labu Siam"],
    "Karbohidrat Pokok": ["Beras Putih Premium", "Kentang Dieng"],
    "Buah Segar": ["Pisang Cavendish", "Semangka Merah", "Melon Cantaloupe", "Jeruk Manis", "Pepaya California"],
    "Bumbu Dapur": ["Bawang Merah", "Bawang Putih", "Garam Beriodium", "Gula Pasir", "Minyak Goreng Sawit"]
  };

  const items = quickMap[cat] || [];
  chipContainer.innerHTML = '';
  items.forEach(it => {
    const b = document.createElement('button');
    b.onclick = () => pickQuickItem(it);
    b.className = 'px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer';
    b.innerText = it;
    chipContainer.appendChild(b);
  });

  if (items.length > 0) {
    pickQuickItem(items[0]);
  }

  if (cat === 'Buah Segar') {
    selectTeam('TIM PEMORSIAN');
    showToast('Buah Segar otomatis dialihkan ke TIM PEMORSIAN');
  }
}

function simulateWeighAction(mode) {
  const item = document.getElementById('input-item').value || 'Bahan MBG';
  const cat = document.getElementById('input-kategori').value;
  const tare = parseFloat(document.getElementById('input-tare').value) || 0.85;

  let activeTeam = 'TIM PERSIAPAN';
  const activeBtn = document.querySelector('.team-chip.bg-emerald-600, .team-chip.bg-amber-600, .team-chip.bg-blue-600');
  if (activeBtn) activeTeam = activeBtn.dataset.team;

  const simulatedBruto = (mode === 'camera') ? (Math.random() * 15 + 10) : (Math.random() * 8 + 5);
  const roundedBruto = parseFloat(simulatedBruto.toFixed(2));
  const roundedNetto = parseFloat(Math.max(0, roundedBruto - tare).toFixed(2));

  const newItem = {
    id: 'cart_' + Date.now(),
    timestamp: new Date().toLocaleTimeString('id-ID'),
    team: activeTeam,
    category: cat,
    name: item,
    bruto: roundedBruto,
    tara: tare,
    netto: roundedNetto,
    catatan: 'Ditimbang via ' + (mode === 'camera' ? 'OCR Kamera' : 'Manual'),
    synced: false
  };

  stagingItems.unshift(newItem);
  renderStagingList();
  showToast('Ditambahkan ke Keranjang (' + roundedNetto + ' kg)');
  switchScreen('staging');
}

function renderStagingList() {
  const list = document.getElementById('staging-items-list');
  const countBadge = document.getElementById('staging-count-badge');
  const cartTabBadge = document.getElementById('tab-cart-badge');

  if (countBadge) countBadge.innerText = stagingItems.length + ' Item';
  if (cartTabBadge) cartTabBadge.innerText = stagingItems.length;

  if (!list) return;
  list.innerHTML = '';

  if (stagingItems.length === 0) {
    list.innerHTML = '<div class="p-8 text-center text-slate-400 bg-white border border-slate-200 rounded-2xl">' +
      '<p class="text-xs font-bold">Keranjang masih kosong</p>' +
      '<p class="text-[10px] mt-1">Lakukan penimbangan dari menu untuk menambah item</p>' +
    '</div>';
    return;
  }

  stagingItems.forEach(item => {
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 p-3 rounded-2xl shadow-xs space-y-2';

    let teamBg = 'bg-emerald-50 text-emerald-800 border-emerald-200';
    if (item.team === 'TIM PENGOLAHAN') teamBg = 'bg-amber-50 text-amber-800 border-amber-200';
    if (item.team === 'TIM PEMORSIAN') teamBg = 'bg-blue-50 text-blue-800 border-blue-200';

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h4 class="text-xs font-bold text-slate-900">' + item.name + '</h4>' +
          '<span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded border ' + teamBg + '">' + item.team + '</span>' +
        '</div>' +
        '<p class="text-[10px] text-slate-500 mt-0.5 font-mono-num">' + item.timestamp + ' • ' + item.category + '</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<span class="text-sm font-extrabold text-emerald-600 font-mono-num">' + item.netto.toFixed(2) + ' kg</span>' +
        '<span class="block text-[9px] text-slate-400 font-mono-num">Bruto: ' + item.bruto.toFixed(2) + ' | Tara: ' + item.tara.toFixed(2) + '</span>' +
      '</div>' +
    '</div>' +
    (item.catatan ? '<p class="text-[10px] text-slate-600 bg-slate-50 px-2 py-1 rounded-lg border border-slate-100 font-medium">' + item.catatan + '</p>' : '') +
    '<div class="flex items-center justify-end gap-2 pt-1 border-t border-slate-100">' +
      '<button onclick="openEditModal(\'' + item.id + '\')" class="px-2.5 py-1 text-[10px] font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-lg flex items-center gap-1 cursor-pointer">' +
        '<svg class="w-3 h-3 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>' +
        '<span>Koreksi / Edit</span>' +
      '</button>' +
      '<button onclick="confirmDeleteItem(\'' + item.id + '\')" class="px-2.5 py-1 text-[10px] font-bold text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-lg flex items-center gap-1 cursor-pointer border border-rose-200">' +
        '<svg class="w-3 h-3 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>' +
        '<span>Hapus</span>' +
      '</button>' +
    '</div>';

    list.appendChild(card);
  });
}

function openEditModal(itemId) {
  const item = stagingItems.find(i => i.id === itemId);
  if (!item) return;

  document.getElementById('edit-item-id').value = item.id;
  document.getElementById('edit-item-name').value = item.name;
  document.getElementById('edit-item-team').value = item.team;
  document.getElementById('edit-item-bruto').value = item.bruto;
  document.getElementById('edit-item-tara').value = item.tara;
  document.getElementById('edit-item-catatan').value = item.catatan || '';

  recalcEditNetto();
  document.getElementById('edit-cart-modal').classList.remove('hidden');
}

function closeEditModal() {
  document.getElementById('edit-cart-modal').classList.add('hidden');
}

function recalcEditNetto() {
  const b = parseFloat(document.getElementById('edit-item-bruto').value) || 0;
  const t = parseFloat(document.getElementById('edit-item-tara').value) || 0;
  const n = Math.max(0, b - t);
  document.getElementById('edit-item-netto-display').innerText = n.toFixed(2) + ' kg';
}

function saveEditCartItem() {
  const id = document.getElementById('edit-item-id').value;
  const item = stagingItems.find(i => i.id === id);
  if (!item) return;

  item.name = document.getElementById('edit-item-name').value;
  item.team = document.getElementById('edit-item-team').value;
  item.bruto = parseFloat(document.getElementById('edit-item-bruto').value) || 0;
  item.tara = parseFloat(document.getElementById('edit-item-tara').value) || 0;
  item.netto = parseFloat(Math.max(0, item.bruto - item.tara).toFixed(2));
  item.catatan = document.getElementById('edit-item-catatan').value;

  closeEditModal();
  renderStagingList();
  showToast('Perubahan item berhasil disimpan');
}

function confirmDeleteItem(itemId) {
  const item = stagingItems.find(i => i.id === itemId);
  if (!item) return;
  stagingItems = stagingItems.filter(i => i.id !== itemId);
  renderStagingList();
  showToast('Item ' + item.name + ' dihapus dari keranjang');
}

function syncAllToGoogleSheets() {
  if (stagingItems.length === 0) {
    showToast('Keranjang kosong, tidak ada item untuk disinkron');
    return;
  }

  const btn = document.getElementById('btn-sync-all');
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<span class="animate-spin text-base">⏳</span><span>Menyinkronkan ke Google Sheets...</span>';
  }

  setTimeout(() => {
    stagingItems = [];
    renderStagingList();
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Berhasil Tersinkron ke Spreadsheet!</span>';
    }
    showToast('Semua item berhasil disinkronkan ke Google Sheet Monitoring!');
    setTimeout(() => {
      if (btn) {
        btn.innerHTML = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg><span>Sinkronkan ke Google Sheets Monitoring</span>';
      }
    }, 2500);
  }, 1500);
}

function openPdfViewerModal() {
  const modal = document.getElementById('pdf-viewer-modal');
  if (modal) modal.classList.remove('hidden');
}

function closePdfViewerModal() {
  const modal = document.getElementById('pdf-viewer-modal');
  if (modal) modal.classList.add('hidden');
}

function showWebhookInfo() {
  showToast('Tersambung ke Google Sheet MBG PEKAJANGAN 04');
}

function showToast(msg) {
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toast-msg');
  if (!toast || !toastMsg) return;
  toastMsg.innerText = msg;
  toast.classList.remove('opacity-0', 'pointer-events-none');
  setTimeout(() => {
    toast.classList.add('opacity-0', 'pointer-events-none');
  }, 2200);
}
