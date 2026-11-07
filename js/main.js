/* =========================================================
   リンク設定：ここを書き換えるだけで全ボタンに反映されます
   ========================================================= */
var LINKS = {
  // ▼ LINE公式アカウント（体験予約・ご相談）
  line: 'https://lin.ee/SpYlcYa',
  instagram: 'https://www.instagram.com/arvo_2026/',
  whitening: 'https://arvo-4ef22.web.app/'
};

document.querySelectorAll('[data-link]').forEach(function (a) {
  var url = LINKS[a.getAttribute('data-link')];
  if (url) a.href = url;
});

/* ヘッダー・固定CTA */
var hd = document.getElementById('hd');
var fix = document.getElementById('fixCta');
function onScroll() {
  var y = window.scrollY;
  if (hd) hd.classList.toggle('is-scrolled', y > 40);
  if (fix) {
    var nearEnd = window.innerHeight + y > document.body.scrollHeight - 700;
    fix.classList.toggle('is-show', y > window.innerHeight * 0.7 && !nearEnd);
  }
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

/* スマホメニュー */
var menuBtn = document.getElementById('menuBtn');
var nav = document.getElementById('nav');
if (menuBtn && nav) {
  function setMenu(open) {
    nav.classList.toggle('is-open', open);
    hd.classList.toggle('menu-open', open);
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
    menuBtn.querySelector('use').setAttribute('href', open ? '#i-close' : '#i-menu');
  }
  menuBtn.addEventListener('click', function () { setMenu(!nav.classList.contains('is-open')); });
  nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
}

/* 「私のことだ」チェック */
var boxes = document.querySelectorAll('.check-item input');
var HINTS = {
  none: ['あなたに合う通い方を探しましょう。', '気になる項目を選ぶと、おすすめのレッスンが表示されます。'],
  group: ['仲間と楽しく、グループレッスンがおすすめ。', 'ピラティス・ヨガ・ダンス系から、その日の気分や体調で選べます。「通う習慣」づくりにぴったりです。'],
  personal: ['じっくり整える、ピラティスパーソナルがおすすめ。', '姿勢や身体の使い方を、マンツーマンでていねいにサポート。まずは体験（1回4,400円）でいまの身体を確認してみませんか。'],
  both: ['パーソナル＋グループの組み合わせがおすすめ。', 'パーソナルで身体の使い方を知り、グループで楽しく続ける。迷ったら、LINEでいまの気持ちをそのまま送ってください。'],
  night: ['平日夜のレッスンがおすすめ。', '平日は21:15まで。お仕事や家事のあと、一日の終わりに自分のための時間をつくりませんか。夜の空き状況はLINEでお気軽にどうぞ。']
};
function updateCheck() {
  var g = 0, p = 0, nt = 0, n = 0;
  boxes.forEach(function (b) {
    if (!b.checked) return;
    n++;
    var h = b.getAttribute('data-hint');
    if (h === 'group') g++; else if (h === 'personal') p++; else if (h === 'night') nt++; else { g++; p++; }
  });
  var key = n === 0 ? 'none'
    : (nt > 0 && nt >= g && nt >= p) ? 'night'
    : (g > p ? 'group' : p > g ? 'personal' : 'both');
  document.getElementById('cnt').textContent = n;
  document.getElementById('resTitle').textContent = HINTS[key][0];
  document.getElementById('resText').textContent = HINTS[key][1];
}
boxes.forEach(function (b) { b.addEventListener('change', updateCheck); });
var reset = document.getElementById('reset');
if (reset) reset.addEventListener('click', function () { boxes.forEach(function (b) { b.checked = false; }); updateCheck(); });

/* スクロール表示 */
if ('IntersectionObserver' in window) {
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
} else {
  document.querySelectorAll('.rv').forEach(function (el) { el.classList.add('is-in'); });
}
