const divForTable = document.getElementById("table");

const grid = new gridjs.Grid({
  columns: [
    { id: "id", name: "ID" },
    { id: "category", name: "Category" },
    { id: "name", name: "Name", sort: false },
  ],
  server: {
    url: "/api/items?for_backend=false",
    headers: {
      "Content-Type": "application/json",
    },
    then: (results) => {
      console.log(results);
      return results.items;
    },
  },
  search: {
    selector: (cell, rowIndex, cellIndex) =>
      [1, 2].includes(cellIndex) ? cell : null,
  },
  sort: true,
  pagination: {
    enabled: true,
    limit: 160,
  },
});

grid.render(divForTable);
