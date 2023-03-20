function main() {
    console.log("Hello, JavaScript!!!!");

    document.querySelector("#reset").onclick = () => {
        console.log("You clicked reset");
        send_command("RESET");
    };

    document.querySelector("#x1").onclick = () => {
        send_command("X-AXIS 1");
    };
    document.querySelector("#x2").onclick = () => {
        send_command("X-AXIS 2");
    };


    document.querySelector("#move").onclick = () => {
        var moveFrom = document.querySelector("#moveFrom").value;
        var moveTo = document.querySelector("#moveTo").value;
        var command = `MOVE ${moveFrom} ${moveTo}`;
        console.log(command);
        send_command(command);
    };
}

async function send_command(command) {
    var reply = await fetch(`/api/${command}`);
    var textReply = await reply.text();
    console.log("The robot reply:", textReply);
    document.querySelector("#robotReply").innerHTML = textReply;
}

main();