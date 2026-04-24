// Initiate FIGS module
function initFigsModule() {
    const tableBody = document.getElementById("figs-table-body");
    if (!tableBody) {
        return;
    }

    fetch("https://jsonplaceholder.typicode.com/users")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to fetch FIGS data");
            }
            return response.json();
        })
        .then((users) => {
            tableBody.innerHTML = "";

            users.forEach((user) => {
                const row = document.createElement("tr");
                row.className = "odd:bg-white even:bg-stone-50";

                const cells = [
                    user.id ?? "",
                    user.name ?? "",
                    user.username ?? "",
                    user.email ?? "",
                    user.address?.street ?? "",
                    user.address?.city ?? "",
                    user.address?.zipcode ?? "",
                ];

                cells.forEach((value) => {
                    const cell = document.createElement("td");
                    cell.className = "px-4 py-3";
                    cell.textContent = String(value);
                    row.appendChild(cell);
                });

                tableBody.appendChild(row);
            });
        })
        .catch((error) => {
            tableBody.innerHTML = '<tr><td colspan="7" class="px-4 py-3 text-red-600">Unable to load FIGS data right now. Please try again.</td></tr>';
            console.error(error);
        });
}

export { initFigsModule };