function simpleMqttTest()
clc
clear all
% mqClient = mqtt("tcp://broker.hivemq.com")
mqClient = mqttclient("tcp://broker.hivemq.com");
subscribe(mqClient, "my_messages", "Callback", @myCallback)
for k = 1:5
    % publish()
    message = sprintf('{"type": "chat", "payload": "fisherds %d"}', k);
    write(mqClient, "my_messages", message)
    pause(2)
end

% unsubscribeAll(mqClient)
unsubscribe(mqClient)
end

function myCallback(topic, message)

messageCell = jsondecode(message)
messageType = messageCell.type;
messagePayload = messageCell.payload;

% fprintf(messagePayload)
end