function our_layers(map,options){
    var osm = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var datas = new L.GeoJSON.AJAX("{% url 'location' %}",{
        onEachFeature: function(feature, layer){
            layer.bindPopup(feature.properties.text.toString());
        }
    });
    datas.addTo(map);
    var baseLayers = {
        "OSM": osm
    };
    var groupedOverlays = {
        "Layers": {
            "location": datas
        }};
    L.control.groupedLayers(baseLayers, groupedOverlays).addTo(map);
}
function clicked(map) {
    if (document.getElementById("flu").checked == true) {
        window.alert("saysth");
    }
}
function checkbox_checker(checkboxElem) {
    if (checkboxElem.checked){
        window.alert("stuff")
    }
    else{
        window.alert("bye")
    }
}

