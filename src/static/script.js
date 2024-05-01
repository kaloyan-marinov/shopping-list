const divForTable = document.getElementById("table");

const grid = new gridjs.Grid({
  columns: [
    { id: "id", name: "ID" },
    { id: "name", name: "Name", sort: false },
    { id: "category", name: "Category" },
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
  pagination: true,
});

grid.render(divForTable);
