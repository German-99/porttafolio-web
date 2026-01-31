const masterItems = document.querySelectorAll('.master-item');

const titleEl = document.getElementById('detailTitle');
const imgEl = document.getElementById('detailImage');
const langEl = document.getElementById('detailLang');
const langIconEl = document.getElementById('detailLangIcon');
const dateEl = document.getElementById('detailDate');
const descEl = document.getElementById('detailDesc');
const linkEl = document.getElementById('detailLink');

masterItems.forEach(item => {

    item.addEventListener('click', function () {

        // quitar activo
        masterItems.forEach(i =>
            i.classList.remove('active-item')
        );

        this.classList.add('active-item');

        // llenar detail panel
        titleEl.textContent = this.dataset.title;
        imgEl.src = this.dataset.image;

        langEl.textContent = this.dataset.lang;
        langIconEl.src = this.dataset.langIcon;

        descEl.textContent = this.dataset.desc;

        // fecha
        if (this.dataset.date && this.dataset.date !== "None") {
            dateEl.textContent = this.dataset.date;
            dateEl.parentElement.classList.remove('d-none');
        } else {
            dateEl.parentElement.classList.add('d-none');
        }

        // link
        if (this.dataset.url) {
            linkEl.href = this.dataset.url;
            linkEl.classList.remove('d-none');
        } else {
            linkEl.classList.add('d-none');
        }

    });

});