function jsonMQTTTest()
clc
fprintf("Connecting...\n");
mqttClient = mqttclient('tcp://broker.hivemq.com')
subscribe(mqttClient,'my_messages',"Callback",@myCallback);

for k = 1:5
    currentMessage = sprintf('{"type": "chat", "payload": "Hello %d"}', k);
    write(mqttClient, "my_messages", currentMessage);
    pause(2);
end

pause(1);  % Allow the last message to finish before closing
unsubscribe(mqttClient)
end

function myCallback(topic, message)
    fprintf("Received message: %s\n", message)    
    messageCell = jsondecode(message)
    messageType = messageCell.type
    payload = messageCell.payload
end

