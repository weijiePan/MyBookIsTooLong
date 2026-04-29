import path from "path"
import { spawn } from "child_process";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
//python setup
const pythonVenvPath = path.join(__dirname, "python", "venv");
const pythonExecutable = process.platform == "win32"? 
    path.join(pythonVenvPath, "Scripts", "python.exe"):
    path.join(pythonVenvPath, "bin", "python")
const editorFile = path.join(pythonVenvPath, "..", "editor.py");
//document setup 

const importDocumentFolder = path.join(__dirname,  "importedDocument");
const exportedDocumentFolder = path.join(__dirname,  "exportedDocument");

const documentName = "Can't Hurt Me_ Master Your Mind and Defy the Odds - Can_t-Hurt-Me-David-Goggins.pdf";
const exportName = "goggins.pdf";
const importedDocument =  path.join(importDocumentFolder, documentName);
const exportedDocument = path.join(exportedDocumentFolder, exportName);


console.log(importedDocument);
const editPdf = spawn(pythonExecutable, [editorFile, importedDocument, exportedDocument]);
editPdf.stdout.on("data", (data)=>{
    console.log(data.toString());
} )
editPdf.stderr.on("data", (data)=>{
    console.log(data.toString());
} )