var notify_badge_id;
var notify_menu_id;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_refresh_period = 15000;
var consecutive_misfires = 0;
var registered_functions = [];

function fill_notification_badge(data) {
    var badge = document.getElementById(notify_badge_id);
    if (badge) {
        badge.innerHTML = data.unread_count;
    }
}

function fill_notification_list(data) {
    var menu = document.getElementById(notify_menu_id);
    if (menu) {
        menu.innerHTML = "";
        for (var i=0; i < data.unread_list.length; i++) {
            var item = data.unread_list[i];
            console.log(item)
            var message = ""
            if(typeof item.actor !== 'undefined'){
                message = item.actor;
            }
            if(typeof item.verb !== 'undefined'){
                message = message + " " + item.verb;
            }
            if(typeof item.target !== 'undefined'){
                message = message + " " + item.target;
            }
            if(typeof item.timestamp !== 'undefined'){
                message = message + " " + item.timestamp;
            }

            menu.innerHTML = menu.innerHTML + "<li>"+ message + "</li>";
        }
    }
}

function register_notifier(func) {
    registered_functions.push(func);
}

function fetch_api_data() {
    if (registered_functions.length > 0) {
        //only fetch data if a function is setup
        var r = new XMLHttpRequest();
        r.open("GET", notify_api_url+'?max='+notify_fetch_count, true);
        r.onreadystatechange = function () {
            if (r.readyState != 4 || r.status != 200) {
                consecutive_misfires++;
            }
            else {
                consecutive_misfires = 0;
                for (var i=0; i < registered_functions.length; i++) {
                    var func = registered_functions[i];
                    func(JSON.parse(r.responseText));
                }
            }
        }
        r.send();
    }
    if (consecutive_misfires < 10) {
        setTimeout(fetch_api_data,notify_refresh_period);
    } else {
        var badge = document.getElementById(notify_badge_id);
        if (badge) {
            badge.innerHTML = "!";
            badge.title = "Connection lost!"
        }
    }
}

setTimeout(fetch_api_data,1000);