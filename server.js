import express from "express";
import multer from "multer";
import cors from "cors";
import { spawn } from "child_process";
import fs from "fs";

const app = express();
app.use(cors());

const upload = multer({ dest: "/tmp" });

app.post("/remove-bg", upload.single("image"), (req, res) => {
  const inputPath = req.file.path;
  const outputPath = `/tmp/output-${Date.now()}.png`;

  const python = spawn("rembg", ["i", inputPath, outputPath]);

  python.on("close", () => {
    fs.readFile(outputPath, (err, data) => {
      res.setHeader("Content-Type", "image/png");
      res.send(data);

      fs.unlinkSync(inputPath);
      fs.unlinkSync(outputPath);
    });
  });
});

app.get("/", (req, res) => {
  res.send("RMBG API Running ✔ Railway Deployment");
});

app.listen(8080, () => console.log("Server running on port 8080"));
