const net = require("net");

const PROXY_PORT = 2525; // Port for the proxy server
const SMTP_SERVER = "smtp.gmail.com";
const SMTP_PORT = 587;
const DELAY = 3000; // 3 seconds delay

// Create a proxy server with a delay
net.createServer(socket => {
    console.log("Received connection, adding delay...");
    setTimeout(() => {
        const client = net.createConnection({ host: SMTP_SERVER, port: SMTP_PORT }, () => {
            console.log("Connected to SMTP server");
            socket.pipe(client).pipe(socket); // Pipe data between Nodemailer and the Gmail SMTP server
        });

        client.on("error", (err) => {
            console.error("Error with SMTP connection:", err);
        });
    }, DELAY);
}).listen(PROXY_PORT, () => {
    console.log(`Delayed proxy server running on port ${PROXY_PORT}`);
});