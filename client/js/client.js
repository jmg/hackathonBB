var BASE_URL = "173.255.241.184:4321";

function login(username, password) {
  $.ajax({
    type: "POST",
    url: BASE_URL + "/login/",
    data: {
      username: username,
      password: password
    },
    success: function(data) {
        console.log("Successfully logged in");
    }
  });
}

function tags() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/tags/",
    success: function(data) {
        tag_list = eval("(" + data + ")")['data'];

        tags_select = document.getElementById("#add-tag");
        for(var i = 0; i < tag_list.length; i++) {
            var tag = document.createElement("option");
            tag.setAttribute('value', tag_list[i]["_id"]);
            tag.innerHTML = tag_list[i]["name"];
            tags_select.appendChild(tag)
        }

        tags_select.refresh();
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
        sendNotification("Expense Saved", "Success");
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
        sendNotification("Income Saved", "Success");
    }
  });
}

function progress() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/progress/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}

function all_expenses() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}

function expenses_by_tag(tag_name) {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses/" + tag_name + "/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}

function top_expenses() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses_top/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}

function top_expenses_by_tag(tag_name) {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/expenses_top/" + tag_name + "/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}

function all_incomes() {
  $.ajax({
    type: "GET",
    url: BASE_URL + "/report/incomes/",
    success: function(data) {
       $("#report-area").html(eval("(" + data + ")")['data']);
    }
  });
}
