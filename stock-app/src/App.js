import React from "react";
import { StockDetails } from "./StockDetails";
import { AddStock } from "./AddStock";

function App() {
  const [currentStock, setCurrentStock] = React.useState("");

  const [ownedStocks, setOwnedStocks] = React.useState(["AAPL", "AMZN"]);
  const [strategyStock, setStrategyStock] = React.useState("");
  const [sellStock, setSellStock] = React.useState("");
  const [bestPrice, setBestPrice] = React.useState();
  const [bestSellPrice, setBestSellPrice] = React.useState();
  const [deleteAll, setDeleteAll] = React.useState(false);
  const mapper = {
    AMAT: "Applied Materials",
    AMZN: "Amazon",
    DDOG: "Datadog",
    TWLO: "Twilio",
    AAPL: "Apple",
    NOW: "Service Now Inc",
  };

  React.useEffect(() => {
    const getStrategy = async (ticker, action) => {
      const resp = await fetch(
        `https://best-stock-strategies-api-service.vercel.app/api/Best_Strategies/Lowrisk/${ticker}/${action}/2024-03-14/2024-03-18`
      );
      const data = await resp.json();
      if (action === "BUY") {
        setBestPrice(data.bestBuyPrice);
      } else {
        setBestSellPrice(data.bestSellPrice);
      }
    };

    if (strategyStock) {
      getStrategy(strategyStock, "BUY");
    }
    if (sellStock) {
      getStrategy(sellStock, "SELL");
    }
  }, [strategyStock, sellStock]);

  return (
    <div className={"container"}>
      <div className="home-container">
        <h2>Welcome To Stock Tracker</h2>
        <div>
          <p>
            Stock Tracker helps you stay up to date on your favorite stocks. We
            offer free data on stocks as well as recommendations on what to buy
            and sell. No signup required!
          </p>
        </div>
        <div>
          <p>
            It's easy to start right away, to customize start adding stocks
            using the dropdown. Be sure to also check out our current AI powered
            recommendations below!
          </p>
        </div>
      </div>
      <div className={"body-container"}>
        <div>
          <h2>Your Stocks</h2>
          <table>
            <thead>
              <tr>
                <th scope="col">Ticker</th>
                <th scope="col">Name</th>
                <th scope="col">Last Price</th>
                <th scope="col">Action</th>
                <th scope="col">Remove</th>
              </tr>
            </thead>
            <tbody>
              {ownedStocks.map((stock, i) => {
                return (
                  <tr>
                    <td>{stock}</td>
                    <td>{mapper[stock]}</td>
                    <td>177.4</td>
                    <td>
                      <button onClick={() => setCurrentStock(stock)}>
                        More Info
                      </button>
                    </td>
                    <td>
                      <button
                        onClick={() => {
                          const filteredStocks = ownedStocks.filter(
                            (stk) => stk !== stock
                          );
                          setOwnedStocks(filteredStocks);
                        }}
                      >
                        X
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {ownedStocks.length > 0 && (
            <button onClick={() => setDeleteAll(true)}>Delete All</button>
          )}
          {deleteAll && (
            <div>
              Delete all symbols? This cannot be undone!
              <button onClick={() => setDeleteAll(false)}>Cancel</button>
              <button
                onClick={() => {
                  setOwnedStocks([]);
                  setDeleteAll(false);
                }}
              >
                Confirm
              </button>
            </div>
          )}
          {currentStock && (
            <StockDetails ticker={currentStock} onClick={setCurrentStock} />
          )}

          <div>
            <h2>Recommended Strategies</h2>
            <p>
              Disclaimer: Not a substitute for doing your own research. All
              investments inherently carry risk. Not all prices shown may be
              available on the market.
            </p>
            <button
              onClick={() => {
                setStrategyStock("");
                setSellStock("");
                setBestSellPrice(undefined);
                setBestPrice(undefined);
              }}
            >
              Reset All (clears strategies)
            </button>
            <h3>Buy Recommendations</h3>
            <div>Click on a stock below to view the recommendation</div>
            <div>
              <ul>
                <li>
                  <button onClick={() => setStrategyStock("AAPL")}>
                    Apple
                  </button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("NVDA")}>
                    Nvidia
                  </button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("NOW")}>
                    ServiceNow
                  </button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("AMAT")}>
                    Applied Materials
                  </button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("PINS")}>
                    Pinterest
                  </button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("ZM")}>Zoom</button>
                </li>
                <li>
                  <button onClick={() => setStrategyStock("SHOP")}>
                    Shopify
                  </button>
                </li>
              </ul>
            </div>
            {bestPrice && (
              <p>{`Currently recommend buying ${strategyStock} at ${bestPrice}`}</p>
            )}
          </div>
          <div>
            <h3>Sell Recommendations</h3>
            <div>Click on a stock below to view the recommendation</div>
            <div>
              <ul>
                <li>
                  <button onClick={() => setSellStock("AMD")}>AMD</button>
                </li>
                <li>
                  <button onClick={() => setSellStock("SMCI")}>
                    Super Micro
                  </button>
                </li>
                <li>
                  <button onClick={() => setSellStock("CAR")}>Avis</button>
                </li>
              </ul>
            </div>
            {sellStock && (
              <p>{`Currently recommend selling ${sellStock} at ${bestSellPrice}`}</p>
            )}
          </div>
        </div>
        <AddStock onSelect={setOwnedStocks} ownedStocks={ownedStocks} />
      </div>
    </div>
  );
}

export default App;
