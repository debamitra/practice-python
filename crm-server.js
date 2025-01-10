const express = require("express");
const nodemailer = require("nodemailer");

const app = express();
const PORT = 3000;

// Configure Nodemailer transporter to use the local proxy with a delay
const transporter = nodemailer.createTransport({
    host: "localhost", // Connect to the local proxy
    port: 2525,        // Proxy server port with delay
    secure: false,
    auth: {
        user: "crm@sigmoidanalytics.com",
        pass: "flgd xkbx tvax smen",
    },
    debug: true,       // Show debug output
    logger: true,      // Log information to console
    tls: {
        rejectUnauthorized: false, // Ignore certificate verification (for local testing only)
    }
});

// Endpoint to trigger email sending
app.get("/send-email", async (req, res) => {
    try {
        // Define email options
        const mailOptions = {
            from: "crm@sigmoidanalytics.com",      // Sender's email
            to: "debamitra.mukherjee@gmail.com",   // Recipient's email
            subject: "Hello from Node.js",         // Subject of the email
            text: "Hi there! This email was sent from a Node.js server!", // Plain text body
        };

        // Send email
        let info = await transporter.sendMail(mailOptions);
        console.log("Email sent:", info.messageId);
        res.send("Email sent successfully!");
    } catch (error) {
        console.error("Error sending email:", error);
        res.status(500).send("Error sending email.");
    }
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});