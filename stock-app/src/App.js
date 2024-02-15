import React from "react";

const StockDetails = (props) => {
  const ticker = props.ticker;

  return (
    <div className={"stock-details"}>
      <h2>{ticker}</h2>
      {ticker === "TTD" && (
        <text>
          The Trade Desk, Inc. operates as a technology company in the United
          States and internationally. The company operates a self-service
          cloud-based platform that allows buyers to plan, manage, optimize, and
          measure data-driven digital advertising campaigns across various ad
          formats and channels, including video, display, audio,
          digital-out-of-home, native, and social on various devices, such as
          computers, mobile devices, televisions, and streaming devices. It also
          provides data and other value-added services. The company serves
          advertising agencies, brands, and other service providers for
          advertisers. The Trade Desk, Inc. was incorporated in 2009 and is
          headquartered in Ventura, California.
        </text>
      )}
      {ticker === "AMAT" && (
        <text>
          Applied Materials, Inc. engages in the provision of manufacturing
          equipment, services, and software to the semiconductor, display, and
          related industries. The company operates through three segments:
          Semiconductor Systems, Applied Global Services, and Display and
          Adjacent Markets. The Semiconductor Systems segment develops,
          manufactures, and sells various manufacturing equipment that is used
          to fabricate semiconductor chips or integrated circuits. This segment
          also offers various technologies, including epitaxy, ion implantation,
          oxidation/nitridation, rapid thermal processing, physical vapor
          deposition, chemical vapor deposition, chemical mechanical
          planarization, electrochemical deposition, atomic layer deposition,
          etching, and selective deposition and removal, as well as metrology
          and inspection tools.
        </text>
      )}
      <button onClick={() => props.onClick("")}>Exit</button>
    </div>
  );
};

const AddStock = (props) => {
  const addStock = () => {
    const newStocks = props.ownedStocks.concat([selection]);
    props.onSelect(newStocks);
  };

  const [selection, setSelection] = React.useState("");

  return (
    <div className={"adder"}>
      <label>Track More Stocks </label>
      <p>Select from the dropdown, then click "Add to Tracker" below</p>
      <select onChange={(e) => setSelection(e.target.value)}>
        <option>AAPL</option>
        <option>AMZN</option>
        <option>TWLO</option>
        <option>DDOG</option>
      </select>

      <button style={{ margin: "10px" }} onClick={addStock}>
        Add to Tracker
      </button>
    </div>
  );
};

function App() {
  const [currentStock, setCurrentStock] = React.useState("");

  const [ownedStocks, setOwnedStocks] = React.useState([]);

  const mapper = {
    AMAT: "Applied Materials",
    AMZN: "Amazon",
    DDOG: "Datadog",
    TWLO: "Twilio",
    AAPL: "Apple",
  };

  return (
    <div className={"container"}>
      <div className="home-container">
        <h2>Welcome To Stock Tracker</h2>
        <div>
          <p>
            Stock Tracker helps you stay up to date on your favorite stocks.
          </p>
        </div>
        <div>
          <p>
            It's easy to start right away, to customize start adding stocks
            using the dropdown.
          </p>
        </div>
      </div>
      <div className={"body-container"}>
        <div>
          <h3>Your Stocks</h3>
          <table>
            <thead>
              <tr>
                <th scope="col">Ticker</th>
                <th scope="col">Name</th>
                <th scope="col">Last Price</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>NVDA</td>
                <td>Nvidia</td>
                <td>722.30</td>
                <td>
                  <button>More Info</button>
                </td>
              </tr>
              <tr>
                <td>URI</td>
                <td>United Rentals</td>
                <td>655.53</td>
                <td>
                  <button>More Info</button>
                </td>
              </tr>
              <tr>
                <td>TTD</td>
                <td>The Trade Desk</td>
                <td>75.21</td>
                <td>
                  <button onClick={() => setCurrentStock("TTD")}>
                    More Info
                  </button>
                </td>
              </tr>
              <tr>
                <td>AMAT</td>
                <td>Applied Materials</td>
                <td>178.68</td>
                <td>
                  <button onClick={() => setCurrentStock("AMAT")}>
                    More Info
                  </button>
                </td>
              </tr>
              {ownedStocks.map((stock, i) => {
                return (
                  <tr>
                    <td>{stock}</td>
                    <td>{mapper[stock]}</td>
                    <td>177.4</td>
                    <td>
                      <button>More Info</button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        <AddStock onSelect={setOwnedStocks} ownedStocks={ownedStocks} />
      </div>

      {currentStock && (
        <StockDetails ticker={currentStock} onClick={setCurrentStock} />
      )}
    </div>
  );
}

export default App;
