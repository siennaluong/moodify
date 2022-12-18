window.addEventListener("DOMContentLoaded", () => {
    document.getElementById("sList").onclick = () => {
      document.getElementById("lgDemo").classList.remove("grid");
    };
    document.getElementById("sGrid").onclick = () => {
      document.getElementById("lgDemo").classList.add("grid");
    };
  });