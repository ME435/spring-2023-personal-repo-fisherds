function simpleMQTTTest
clc
fprintf("Connecting...\n");
mqttClient = mqtt('tcp://broker.hivemq.com')
subscribe(mqttClient,'fisherds', "Callback", @myCallback);

for k = 1:3
    pause(1);
    currentMessage = sprintf("Hello %d", k);
    publish(mqttClient, 'fisherds', currentMessage);
end

pause(1);  % Allow the last message to finish before closing
unsubscribeAll(mqttClient)
end

function myCallback(topic, message)
    fprintf("Received message: %s\n", message)
end
