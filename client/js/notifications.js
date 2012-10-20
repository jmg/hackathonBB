/*
 * Copyright 2012 Research In Motion Limited.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

function sendMessage(message, title) {
    var imgPath, title;

    //local Image:
    imgPath = "../img/icon.png";

    //The following will add a notification to the desktop / homescreen:
    webkitNotifications.createNotification(imgPath, title, message).show();
}

function sendNotification(message, title) {

    if (window.webkitNotifications) {
        if (window.webkitNotifications.checkPermission() === 0) {
            sendMessage(message, title);
        } else {
            webkitNotifications.requestPermission(sendMessage);
        }
    } else {
        console.log("Error in sendNotification: webkitNotifications API is undefined");
    }
}
