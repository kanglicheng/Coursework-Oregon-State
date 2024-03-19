import React from "react";

export const AddStock = (props) => {
  const addStock = (stock) => {
    if (!stock) {
      return;
    }
    const newStocks = props.ownedStocks.concat([stock]);
    props.onSelect(newStocks);
  };

  const [selection, setSelection] = React.useState("");

  const options = ["AAPL", "AMZN", "TWLO", "DDOG", "NOW", "TTD", "AMAT"];

  return (
    <div className={"adder"}>
      <label>Track More Stocks </label>
      <p>Select from the dropdown, then click "Add to Tracker" below</p>
      <select onChange={(e) => setSelection(e.target.value)}>
        {options.map((ticker) => (
          <option>{ticker}</option>
        ))}
      </select>

      <button style={{ margin: "10px" }} onClick={() => addStock(selection)}>
        Add to Tracker
      </button>
      <p>
        Not sure what stocks to add? Try some of our users' current favorites
      </p>
      <button onClick={() => addStock("NVDA")}>Add Nvidia</button>
      <button onClick={() => addStock("META")}>Add Meta</button>
      <button onClick={() => addStock("MSFT")}>Add Microsoft</button>
    </div>
  );
};
