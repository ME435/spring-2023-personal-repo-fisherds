function newSimpleMqtt()
clc
fprintf("Connecting...\n");
mqClient = mqttclient('tcp://broker.hivemq.com');

subscribe(mqClient,"my_messages", "Callback", @myCallback);

for k = 1:3
    pause(1);
    currentMessage = sprintf("Hello %d", k);
    write(mqClient, "my_messages", currentMessage);
end

pause(1);  % Allow the last message to finish before closing
unsubscribe(mqClient)
end

function myCallback(topic, message)
    fprintf("Received message: %s\n", message)
end
