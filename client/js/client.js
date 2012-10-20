var BASE_URL = "";

function login(username, password) {
  $.ajax({
    type: "POST",
    url: BASE_URL + "/login/",
    data: {
      username: username,
      password: password
    },
    success: function(data) {
    }
  });
}

function tags() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/tags/",
    success: function(data) {
    }
  });
}

function save_expense(cost, name, time, tag_id) {
  $.ajax({
    type: "POST",
    url: BASE_URL + "/crud/expense/",
    data: {
      cost: cost,
      name: name,
      time: time,
      tag_id: tag_id
    },
    success: function(data) {
    }
  });
}

function save_income(cost, name, time) {
  $.ajax({
    type: "POST",
    url: BASE_URL + "/crud/income/",
    data: {
      cost: cost,
      name: name,
      time: time,
    },
    success: function(data) {
    }
  });
}

function progress() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/progress/",
    success: function(data) {
    }
  });
}

function all_expenses() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses/",
    success: function(data) {
    }
  });
}

function expenses_by_tag(tag_name) {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses/" + tag_name + "/",
    success: function(data) {
    }
  });
}

function top_expenses() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses_top/",
    success: function(data) {
    }
  });
}

function top_expenses_by_tag(tag_name) {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses_top/" + tag_name + "/",
    success: function(data) {
    }
  });
}

function all_incomes() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/incomes/",
    success: function(data) {
    }
  });
}
