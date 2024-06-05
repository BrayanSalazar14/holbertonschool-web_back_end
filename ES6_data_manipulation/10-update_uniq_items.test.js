import updateUniqueItems from "./10-update_uniq_items.js";
import groceriesList from "./9-groceries_list.js";

test("updateUniqueItems is implemented correctly", () => {
  const map = groceriesList();
  updateUniqueItems(map);

  expect(() => {
    updateUniqueItems(true);
  }).toThrowError('Cannot process');
});