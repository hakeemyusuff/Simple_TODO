const checkBtns = document.querySelectorAll(".checked");
const uncheckBtns = document.querySelectorAll(".unchecked");
const obj = document.querySelectorAll(".obj");
const clearAll = document.querySelector(".clear");
// const comp = document.querySelectorAll(".complete")
const deleteBtns = document.querySelectorAll(".delete");
const urlParam = new URLSearchParams(window.location.search);
// console.log(checkBtns);
// console.log(uncheckBtns);

function add(val) {
  uncheckBtns[val].addEventListener("click", () => {
    const objName = obj[val].innerText;
    checkBtns[val].classList.remove("none");
    uncheckBtns[val].classList.add("none");
    // obj[val].classList.add("strikeThrough");
    urlParam.set("complete", objName);
    window.location.search = urlParam;
  });
}

function remove(val) {
  checkBtns[val].addEventListener("click", () => {
    const objName = obj[val].innerText;
    checkBtns[val].classList.add("none");
    uncheckBtns[val].classList.remove("none");
    // obj[val].classList.remove("strikeThrough");
    urlParam.set("remove", objName);
    window.location.search = urlParam;
  });
}

function clear(val) {
  deleteBtns[val].addEventListener("click", () => {
    const objName = obj[val].innerText;
    urlParam.set("name", objName);
    window.location.search = urlParam;
  });
}

function edit(val) {
  const original = obj[val].textContent;
  obj[val].addEventListener("dblclick", (e) => {
    obj[val].contentEditable = "true";
    obj[val].focus();
  });
  obj[val].addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      obj[val].contentEditable = "false";
      let editedText = obj[val].textContent;
      urlParam.set("original", original);
      urlParam.set("edited", editedText);
      window.location.search = urlParam;
    }
  });
//   obj[val].addEventListener("blur", () => {
//     let editedText = obj[val].textContent;
//     console.log(editedText, original);
//   });
}

clearAll.addEventListener("click", () => {
  urlParam.set("clear", "clear");
  window.location.search = urlParam;
});

const values = [];
for (let I = 0; I < checkBtns.length; I++) {
  if (checkBtns) {
    add(I);
    remove(I);
    clear(I);
    edit(I);
  }
}

// console.log(values);
