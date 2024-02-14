
var downloadBtn = document.getElementById('btnDownload');
var imprimirBtn = document.getElementById('btnImprimir');

downloadBtn.addEventListener('click', function () {
    var link = document.createElement('a');
    link.download = 'qrcol_img.png';
    link.href = '/static/qrcol_img.png';
    console.log(link + "link")
    link.click();
});

imprimirBtn.addEventListener('click', function () {
    console.log("clicou")
    window.print();
});

//deixar os botoes visiveis aos a impressao
window.onafterprint = function() {
    document.getElementById("btnDownload").style.display = "block";
    document.getElementById("btnImprimir").style.display = "block";
    document.getElementById("textoTitulo").style.display = "block";
};
