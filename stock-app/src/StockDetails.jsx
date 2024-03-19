import React from "react";
export const StockDetails = (props) => {
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
      {ticker === "AAPL" && (
        <text>
          Apple Inc. designs, manufactures, and markets smartphones, personal
          computers, tablets, wearables, and accessories worldwide. The company
          offers iPhone, a line of smartphones; Mac, a line of personal
          computers; iPad, a line of multi-purpose tablets; and wearables, home,
          and accessories comprising AirPods, Apple TV, Apple Watch, Beats
          products, and HomePod.
        </text>
      )}
      {ticker === "AMZN" && (
        <text>
          Amazon.com, Inc. engages in the retail sale of consumer products,
          advertising, and subscriptions service through online and physical
          stores in North America and internationally. The company operates
          through three segments: North America, International, and Amazon Web
          Services (AWS). It also manufactures and sells electronic devices,
          including Kindle, Fire tablets, Fire TVs, Echo, Ring, Blink, and eero;
          and develops and produces media content. In addition, the company
          offers programs that enable sellers to sell their products in its
          stores; and programs that allow authors, independent publishers,
          musicians, filmmakers, Twitch streamers, skill and app developers, and
          others to publish and sell content. Further, it provides compute,
          storage, database, analytics, machine learning, and other services, as
          well as advertising services through programs, such as sponsored ads,
          display, and video advertising. Additionally, the company offers
          Amazon Prime, a membership program.
        </text>
      )}
      <div>
        <button onClick={() => props.onClick("")}> Exit</button>
      </div>
    </div>
  );
};
