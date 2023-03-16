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
}

function send_command(command) {
    fetch(`/api/${command}`);
}

main();