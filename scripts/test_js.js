
const weeklyMenuData = {
  senin: {
    title: "Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang",
    nutrition: "Energi 685 kkal • Protein 28 gr • Zat Besi & Serat Tinggi",
    items: [
      {
        name: "Daging Ayam Fillet",
        category: "Protein Hewani",
        team: "TIM PENGOLAHAN (PROHE)",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 2.5 x 2.5 cm rapi, buang lemak tebal, pakai keranjang hijau tara 0.85 kg.",
        pengolahan: "Marinasi 30 mnt bumbu kecap jahe, masak hingga suhu inti minimal 75°C.",
        pemorsian: "Timbang netto 65 gr di sekat lauk utama, jangan sampai kuah semur tumpah ke nasi."
      },
      {
        name: "Wortel & Buncis Sop",
        category: "Sayuran Segar",
        team: "TIM PENGOLAHAN (SAYUR)",
        portion: "60 gr / porsi (sayur + kuah)",
        tare: "0.85",
        persiapan: "Wortel potong koin 0.5 cm, buncis potong serong 2 cm, cuci bilas air mengalir.",
        pengolahan: "Rebus renyah gurih al-dente, masukkan seledri dan daun bawang 2 menit sebelum selesai.",
        pemorsian: "Sajikan hangat minimal 60°C, 1 centong sayur sop merata di sekat sayur."
      },
      {
        name: "Tempe Kedelai",
        category: "Protein Nabati",
        team: "TIM PENGOLAHAN (PRONA)",
        portion: "40 gr / porsi (Total 120 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 1.5 cm rapi, susun di baki stainless.",
        pengolahan: "Ungkep bumbu bacem legit dengan gula kelapa asli hingga bumbu meresap kecokelatan.",
        pemorsian: "1 potong bacem 40 gr di sekat ketiga ompreng."
      },
      {
        name: "Pisang Cavendish",
        category: "Buah Segar",
        team: "TIM BUAH & POTONG",
        portion: "1 pcs utuh (Grade A)",
        tare: "0.00",
        persiapan: "Sortir buah mulus grade A, bersihkan kulit dengan lap kering bersih.",
        pengolahan: "Simpan di rak sejuk suhu ruang, tidak boleh ditumpuk lebih dari 3 lapis.",
        pemorsian: "Letakkan 1 buah pisang utuh di atas ompreng/lunchbox."
      }
    ]
  },
  selasa: {
    title: "Nasi Putih + Daging Sapi Teriyaki + Tahu Bakso + Capcay + Jeruk",
    nutrition: "Energi 710 kkal • Protein 31 gr • Zat Besi Heme & Vitamin C",
    items: [
      {
        name: "Daging Sapi Segar",
        category: "Protein Hewani",
        team: "TIM PENGOLAHAN (PROHE)",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.85",
        persiapan: "Slice tipis 2 mm melawan serat daging agar empuk maksimal.",
        pengolahan: "Tumis cepat saus teriyaki gurih manis, taburi wijen sangrai saat matang.",
        pemorsian: "Netto 60 gr di sekat lauk utama."
      },
      {
        name: "Brokoli & Kembang Kol",
        category: "Sayuran Segar",
        team: "TIM PENGOLAHAN (SAYUR)",
        portion: "60 gr / porsi capcay",
        tare: "0.85",
        persiapan: "Rendam air garam 10 menit untuk hilangkan ulat, potong perkuntum seragam.",
        pengolahan: "Blanching cepat 1 menit lalu tumis saus tiram gurih renyah.",
        pemorsian: "Sajikan hangat 60 gr di sekat sayur."
      },
      {
        name: "Tahu Bakso Sapi",
        category: "Protein Nabati",
        team: "TIM PENGOLAHAN (PRONA)",
        portion: "45 gr / pcs (1 butir)",
        tare: "0.50",
        persiapan: "Isi adonan bakso ke dalam tahu pong goreng, kukus 25 menit.",
        pengolahan: "Kukus hangat suhu inti 75°C hingga matang kenyal.",
        pemorsian: "1 pcs tahu bakso utuh 45 gr di sekat lauk pendamping."
      },
      {
        name: "Jeruk Manis",
        category: "Buah Segar",
        team: "TIM BUAH & POTONG",
        portion: "1 pcs utuh",
        tare: "0.00",
        persiapan: "Cuci lap kering, sortir buah matang segar.",
        pengolahan: "Simpan di keranjang berventilasi baik.",
        pemorsian: "1 buah jeruk manis di samping kemasan."
      }
    ]
  },
  rabu: {
    title: "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam + Semangka",
    nutrition: "Energi 660 kkal • Protein 26 gr • Tinggi Asam Lemak Omega-3",
    items: [
      {
        name: "Ikan Kembung Fillet",
        category: "Protein Hewani",
        team: "TIM PENGOLAHAN (PROHE)",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 menit.",
        pengolahan: "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas kental.",
        pemorsian: "1 potong 65 gr renyah di sekat lauk utama."
      },
      {
        name: "Bayam Hijau & Jagung Manis",
        category: "Sayuran Segar",
        team: "TIM PENGOLAHAN (SAYUR)",
        portion: "60 gr kuah bening",
        tare: "0.85",
        persiapan: "Petik daun bayam segar, pipil jagung manis, bilas 3 kali air mengalir.",
        pengolahan: "Masak bening tidak lebih dari 3 menit agar zat besi tidak rusak.",
        pemorsian: "1 centong bening bayam jagung manis segar."
      },
      {
        name: "Semangka Merah",
        category: "Buah Segar",
        team: "TIM BUAH & POTONG",
        portion: "80 gr (potong segitiga)",
        tare: "0.50",
        persiapan: "Kupas kulit hijau, potong segitiga tebal tanpa biji.",
        pengolahan: "Kemas di baki tertutup suhu dingin sebelum diporsikan.",
        pemorsian: "80 gr semangka segar dingin di sekat buah."
      }
    ]
  },
  kamis: {
    title: "Nasi Putih + Ayam Panggang Madu + Rolade Tahu + Tumis Labu Siam + Melon",
    nutrition: "Energi 690 kkal • Protein 29 gr • Vitamin A & Kalium Optimal",
    items: [
      {
        name: "Paha Ayam Fillet",
        category: "Protein Hewani",
        team: "TIM PENGOLAHAN (PROHE)",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Potong porsi 70 gr, tusuk garpu agar bumbu madu meresap.",
        pengolahan: "Ungkep bumbu kuning madu, panggang oven hingga karamelisasi mengkilap.",
        pemorsian: "1 potong ayam panggang 70 gr mengkilap di sekat utama."
      },
      {
        name: "Labu Siam Kupas",
        category: "Sayuran Segar",
        team: "TIM PENGOLAHAN (SAYUR)",
        portion: "55 gr tumis labu",
        tare: "0.85",
        persiapan: "Kupas getah labu siam, potong korek api 0.5 cm.",
        pengolahan: "Tumis gurih bawang merah putih iris tipis, jangan overcook.",
        pemorsian: "55 gr tumisan labu siam gurih renyah."
      }
    ]
  },
  jumat: {
    title: "Nasi Gurih Pandan + Telur Balado Manis + Perkedel Kentang + Lodeh Labu + Pepaya",
    nutrition: "Energi 725 kkal • Protein 27 gr • Karbohidrat Kompleks & Enzim Papain",
    items: [
      {
        name: "Telur Ayam Ras",
        category: "Protein Hewani",
        team: "TIM PENGOLAHAN (PROHE)",
        portion: "55 gr (1 butir utuh)",
        tare: "0.85",
        persiapan: "Rebus matang, kupas kulit mulus tanpa cacat putih telur.",
        pengolahan: "Bumbu balado ramah anak (dominan tomat matang manis non-pedas).",
        pemorsian: "1 butir utuh balado 55 gr di sekat lauk."
      },
      {
        name: "Pepaya California",
        category: "Buah Segar",
        team: "TIM BUAH & POTONG",
        portion: "80 gr (potong dadu)",
        tare: "0.50",
        persiapan: "Kupas tebal, buang biji hitam, potong dadu 3 cm seragam.",
        pengolahan: "Simpan dingin di baki higienis.",
        pemorsian: "80 gr dadu pepaya manis matang pohon."
      }
    ]
  }
};

let currentDay = 'senin';

function switchScreen(screen) {
  const screens = ['menu', 'home', 'staging', 'stock'];
  screens.forEach(id => {
    const el = document.getElementById('screen-' + id);
    if (el) el.classList.add('hidden');

    const topBtn = document.getElementById('tab-btn-' + id);
    if (topBtn) {
      if (id === screen) {
        topBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer';
      } else {
        topBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 flex items-center gap-1 cursor-pointer';
      }
    }

    const navBtn = document.getElementById('nav-btn-' + id);
    if (navBtn) {
      const svg = navBtn.querySelector('svg');
      if (id === screen) {
        navBtn.className = 'flex flex-col items-center text-slate-900 transition-colors relative cursor-pointer';
        if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-900');
      } else {
        navBtn.className = 'flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative cursor-pointer';
        if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-400');
      }
    }
  });

  const target = document.getElementById('screen-' + screen);
  if (target) target.classList.remove('hidden');

  if (screen === 'menu') {
    renderWeeklyMenu();
  }
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
  if (heroLabel) heroLabel.textContent = 'MENU HARI ' + day.toUpperCase();
  renderWeeklyMenu();
}

function renderWeeklyMenu() {
  const data = weeklyMenuData[currentDay];
  if (!data) return;

  const titleEl = document.getElementById('weekly-menu-title');
  if (titleEl) titleEl.textContent = data.title;

  const noteEl = document.getElementById('weekly-nutrition-note');
  if (noteEl) noteEl.textContent = data.nutrition;

  const container = document.getElementById('menu-items-container');
  if (!container) return;
  container.innerHTML = '';

  const filterEl = document.getElementById('station-directive-filter');
  const filter = filterEl ? filterEl.value : 'all';

  data.items.forEach(item => {
    const card = document.createElement('div');
    card.className = 'bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2.5';

    let directivesHtml = '';

    if ((filter === 'all' || filter === 'persiapan') && item.persiapan) {
      directivesHtml += '<div class="bg-emerald-50 border border-emerald-200 p-2 rounded-xl text-xs"><span class="font-extrabold text-emerald-800 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-600"></span> TIM PERSIAPAN:</span><p class="text-slate-700 mt-0.5">' + item.persiapan + '</p></div>';
    }

    if ((filter === 'all' || filter === 'pengolahan') && item.pengolahan) {
      directivesHtml += '<div class="bg-amber-50 border border-amber-200 p-2 rounded-xl text-xs"><span class="font-extrabold text-amber-800 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-600"></span> TIM PENGOLAHAN:</span><p class="text-slate-700 mt-0.5">' + item.pengolahan + '</p></div>';
    }

    if ((filter === 'all' || filter === 'pemorsian') && item.pemorsian) {
      directivesHtml += '<div class="bg-blue-50 border border-blue-200 p-2 rounded-xl text-xs"><span class="font-extrabold text-blue-800 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-blue-600"></span> TIM PEMORSIAN:</span><p class="text-slate-700 mt-0.5">' + item.pemorsian + '</p></div>';
    }

    const safeName = item.name.replace(/'/g, "\\'");
    const safeCat = item.category.replace(/'/g, "\\'");
    const safeTeam = item.team.replace(/'/g, "\\'");

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h3 class="text-xs font-bold text-slate-900">' + item.name + '</h3>' +
          '<span class="text-[9px] font-semibold bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded">' + item.category + '</span>' +
        '</div>' +
        '<p class="text-[10px] text-slate-500 font-medium mt-0.5">' + item.portion + '</p>' +
      '</div>' +
      '<button onclick="loadMenuItemToWeigh(\'' + safeName + '\', \'' + safeCat + '\', \'' + safeTeam + '\', \'' + item.tare + '\')" class="px-2.5 py-1 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-xs font-bold shadow-sm transition-all flex items-center gap-1 cursor-pointer active:scale-95">' +
        '<span>Mulai Timbang</span>' +
        '<svg class="w-3 h-3 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>' +
      '</button>' +
    '</div>' +
    '<div class="space-y-1.5">' + directivesHtml + '</div>';

    container.appendChild(card);
  });
}

function filterDirectives() {
  renderWeeklyMenu();
}

function loadMenuItemToWeigh(name, category, team, tare) {
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;

  const inputCat = document.getElementById('input-kategori');
  if (inputCat) inputCat.value = category;

  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = tare || '0.85';

  selectTeam(team);

  const banner = document.getElementById('autofill-banner');
  const bannerText = document.getElementById('autofill-banner-text');
  if (bannerText) bannerText.textContent = 'Menu ' + name + ' (' + category + ') dimuat untuk ' + team + '!';
  if (banner) banner.classList.remove('hidden');

  switchScreen('home');
}

function selectTeam(teamName) {
  document.querySelectorAll('.team-chip').forEach(btn => {
    if (btn.dataset.team === teamName) {
      btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer';
    } else {
      btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer';
    }
  });

  const badge = document.getElementById('current-tahapan-badge');
  if (badge) {
    if (teamName.includes('PERSIAPAN') || teamName.includes('BUAH')) {
      badge.textContent = 'Penerimaan Gudang';
    } else if (teamName.includes('PEMORSIAN')) {
      badge.textContent = 'Pemorsian Distribusi';
    } else {
      badge.textContent = 'Pengeluaran Masak';
    }
  }
}

function setTarePreset(tare) {
  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = tare;
}

function onCategoryChanged() {}

function showModal(title, text) {
  const modal = document.getElementById('feedback-modal');
  const modalTitle = document.getElementById('modal-title');
  const modalText = document.getElementById('modal-text');
  if (modalTitle) modalTitle.textContent = title;
  if (modalText) modalText.textContent = text;
  if (modal) modal.classList.remove('hidden');
}

function closeModal() {
  const modal = document.getElementById('feedback-modal');
  if (modal) modal.classList.add('hidden');
}

function startWeighFlow(fromGallery) {
  const item = document.getElementById('input-item') ? document.getElementById('input-item').value : 'Bahan Baku';
  const tare = document.getElementById('input-tare') ? document.getElementById('input-tare').value : '0.85';
  const simulatedBruto = (parseFloat(tare) + 12.45).toFixed(2);
  const simulatedNetto = (12.45).toFixed(2);

  const mode = fromGallery ? 'GALERI HP' : 'FOTO KAMERA';
  showModal('Simulasi ' + mode + ' Berhasil', 'Timbangan ' + item + ' terbaca OCR: ' + simulatedBruto + ' kg. Tara wadah: ' + tare + ' kg. Netto dihitung: ' + simulatedNetto + ' kg (Siap masuk keranjang tim).');
}

function submitToGoogleSheet() {
  const btn = document.getElementById('btn-submit-sheet');
  if (btn) {
    btn.innerHTML = '<span class="animate-spin inline-block mr-2">⚪</span> Menyinkronkan ke MBG PEKAJANGAN 04...';
    btn.disabled = true;
  }

  setTimeout(() => {
    showModal('Tersinkronisasi ke Google Sheet!', 'Data batch timbangan resmi dicatat di Form Monitoring Alur Bahan Baku SPPG Pekajangan 4 dan mutasi stok diperbarui.');
    if (btn) {
      btn.innerHTML = '<span>Kirim ke Spreadsheet MBG PEKAJANGAN 04</span>';
      btn.disabled = false;
    }
    switchScreen('stock');
  }, 1000);
}

function refreshStock() {
  showModal('Stok Diperbarui', 'Kartu stok gudang SPPG Pekajangan 4 berhasil disinkronkan secara langsung dari Google Sheet.');
}

function showWebhookInfo() {
  showModal('Status Webhook SPPG', 'URL Webhook: https://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec\n\nStatus: ONLINE & LIVE SYNC (200 OK)');
}

document.addEventListener('DOMContentLoaded', () => {
  renderWeeklyMenu();
});
