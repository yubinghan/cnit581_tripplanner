destination = ""

function addMembers() {
    numTra = parseInt(document.getElementById('travellerNum').value, 10); 
    destination = document.getElementById('to').value
    fieldHTML = "<div><label>Name</label><input type='text' id='traNm'> <label>Email</label><input type='text' id='traEmail'></div>";

    document.getElementById("add_Member").innerHTML += fieldHTML;
    alert(destination)
    for (let x = 1; x < numTra; x++) {
        document.getElementById("add_Member").innerHTML += fieldHTML;
    }
}



function displayMap() {
    const mapOptions = {
      center: { lat: 38.90, lng: -77.04 },
      zoom: 10
    };
    const mapDiv = document.getElementById('map');
    const map = new google.maps.Map(mapDiv, mapOptions);
    return map;
}

