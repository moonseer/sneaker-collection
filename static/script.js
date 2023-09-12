// Reusable function to create card
function createCard(sneaker) {
    return `
        <div class="col-md-3">
            <div class="card">
                <a href="/sneaker/${sneaker.id}">
                    <img src="${sneaker.image}" class="card-img-top" alt="${sneaker.name}">
                </a>
                <div class="card-body">
                    <h5 class="card-title">${sneaker.name}</h5>
                    <a href="/sneaker/${sneaker.id}" class="btn btn-primary">Details</a>
                </div>
            </div>
        </div>
    `;
}

// Function to fetch data
function fetchPage(page) {
    fetch(`/fetch/${page}`)
        .then(response => response.json())
        .then(data => {
            const cardContainer = document.querySelector('.card-container');
            cardContainer.innerHTML = '';
            data.forEach(sneaker => {
                cardContainer.innerHTML += createCard(sneaker);
            });
        });
}

// Pagination
document.querySelector('.next-button').addEventListener('click', function () {
    currentPage++;
    fetchPage(currentPage);
});

document.querySelector('.previous-button').addEventListener('click', function () {
    currentPage--;
    fetchPage(currentPage);
});

let currentPage = 1; // Initialize currentPage

// Sorting logic
function sortTable(n) {
    let table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("sneakerTable");
    switching = true;
    dir = "asc";

    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];

            if (dir === "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir === "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount === 0 && dir === "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

// Function to render charts
function renderCharts() {
    // Logic for Brand Chart
    var brandCtx = document.getElementById('brandChart').getContext('2d');
    var modelCtx = document.getElementById('modelChart').getContext('2d');
    var brandData = JSON.parse(document.getElementById('brand-data').textContent);
    var modelData = JSON.parse(document.getElementById('model-data').textContent);

    var brandLabels = brandData.map(item => item[0]);
    var brandValues = brandData.map(item => item[1]);
    var modelLabels = modelData.map(item => item[0]);
    var modelValues = modelData.map(item => item[1]);

    var colors = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
        '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D'
    ];

    new Chart(brandCtx, {
        type: 'pie',
        data: {
            labels: brandLabels,
            datasets: [{
                data: brandValues,
                backgroundColor: colors
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
            },
        },
    });

    // Logic for Model Chart
    new Chart(modelCtx, {
        type: 'pie',
        data: {
            labels: modelLabels,
            datasets: [{
                data: modelValues,
                backgroundColor: colors
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
            },
        },
    });
}

// Call the renderCharts function when the DOM is ready
document.addEventListener("DOMContentLoaded", renderCharts);


