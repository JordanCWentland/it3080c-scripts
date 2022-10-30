//Creation of dictionary for rank values
var rankDict = {
  bronze: 10,
  silver: 20,
  gold: 30,
  platinum: 40,
  diamond: 50,
  masters: 60,
  grandmaster: 70,
};
const key = Object.keys(obj).find((key) => obj[key] === value);

//function called when button is pressed to pull and calculate ranks based on html input
function buttonPressed() {
  genVar();
  returnVal();
  //alert(avgRank);
}

//Function to generate our global variables in the script
function genVar() {
  globalThis.p1 = document.getElementById("player1").value;
  globalThis.p1d = parseInt(document.getElementById("p1d").value);
  globalThis.p2 = document.getElementById("player2").value;
  globalThis.p2d = parseInt(document.getElementById("p2d").value);
  globalThis.p3 = document.getElementById("player3").value;
  globalThis.p3d = parseInt(document.getElementById("p3d").value); //surely there is a better way, right jordan?
  globalThis.p4 = document.getElementById("player4").value;
  globalThis.p4d = parseInt(document.getElementById("p4d").value);
  globalThis.p5 = document.getElementById("player5").value;
  globalThis.p5d = parseInt(document.getElementById("p5d").value);
  funMath();
}

//function for heavy lifting math
function funMath() {
  p1di = rankDict[p1];
  p2di = rankDict[p2];
  p3di = rankDict[p3];
  p4di = rankDict[p4];
  p5di = rankDict[p5];

  avgRank = (p1di + p2di + p3di + p4di + p5di) / 5;
  avgDiv = Math.round((p1d + p2d + p3d + p4d + p5d) / 5);

  if (avgRank % 10) {
    avgRank = Math.ceil(avgRank / 10) * 10;
    avgDiv = 5;
  }
  avgRank = getKeyByValue(rankDict, avgRank);
  globalThis.avgDivRank =
    "You should be practicing against a team with the average rank of: " +
    avgRank +
    " " +
    avgDiv;
}

//Function to return calculated values to the HTML doc
function returnVal() {
  document.getElementById("team").innerText = avgDivRank;
}

//Function used to do key look up by values in the dictionary
function getKeyByValue(object, value) {
  return Object.keys(object).find((key) => object[key] === value);
}
