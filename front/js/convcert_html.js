function convertHTML(str) {
    return str.replace(/&/g, "&amp;")
              .replace(/>/g, "&gt;")
              .replace(/</g, "&lt;")
              .replace(/"/g, "&quot;")
              .replace(/'/g, "&apos;")
    ;
  }

  convertHTML("Dolce & Gabbana");