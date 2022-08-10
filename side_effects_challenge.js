const database = {};

function findStandardAgent() {}

function findAgentByRequestType(request) {}

function initApp() {
  const success = connectDatabase();
  if (!success) {
    console.log("Could not connect to database");
  }
}

function connectDatabase() {
  const didConnect = database.connect(); //expected side effect
  return didConnect;
}

function determineSupportAgent(ticket) {
  if (ticket.requestType === "unknown") {
    return findStandardAgent(); // doesn't look like it'll have a side effect
  }
  return findAgentByRequestType(ticket.requestType); // same here
}

function isValid(email, password) {
  if (!email.includes("@") || password.length < 7) {
    console.log("Invalid input!"); // unexpected side effect, can extract
    return false;
  }
  return true;
}
