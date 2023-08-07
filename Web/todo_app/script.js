// --------------- LAYOUT ----------------
const toggleField = document.getElementById("toggle-btn");
const fieldElement = document.querySelector(".field");
const backDrop = document.getElementById("backdrop");

// function to close the form
function closeForm() {
  fieldElement.style.display = "none";
  backDrop.style.display = "none";
}
function viewForm() {
  fieldElement.style.display = "block";
  backDrop.style.display = "block";
}

toggleField.addEventListener("click", () => viewForm());

backDrop.addEventListener("click", () => closeForm());
// --------------- LAYOUT ---------------- //

// ---------------- FORM ------------------ //

function addEvent() {
  const eventTitle = document.getElementById("user-field");
  const eventDesc = document.getElementById("desc");
  title = eventTitle.value
  desc = eventDesc.value

  userEvent = JSON.stringify({ 'title': title, 'description': desc });
  key = title + (localStorage.length + 1);
  localStorage.setItem(key, userEvent);

  viewEvent(title, desc, key);
  eventTitle.value = ""
  eventDesc.value = ""

  closeForm();
}
// ---------------- FORM ------------------ //

function viewEvent(title, content, key) {
  const todoDiv = document.createElement("div");
  todoDiv.className = "todo";
  todoDiv.setAttribute("id", key);

  const expandDiv = document.createElement("div");
  expandDiv.className = "expand-btn";
  // expandDiv.addEventListener

  const expandBtn = document.createElement("button");
  expandBtn.className = "exp-btn";
  expandBtn.setAttribute("id", `exp_${key}`);
  const expImg = document.createElement("img");
  expImg.src = "icons/chevron-down.svg";
  expImg.alt = "expand";
  expImg.setAttribute("id", `down_${key}`);
  expandBtn.appendChild(expImg);
  expandBtn.addEventListener("click", () => expand(key));

  expandDiv.appendChild(expandBtn);

  const contentDiv = document.createElement("div");
  contentDiv.className = "content";
  contentDiv.setAttribute("id", `cont_${key}`);

  const eventTitle = document.createElement("h2");
  eventTitle.textContent = title;
  eventTitle.setAttribute("id", `title_${key}`);

  const eventDesc = document.createElement("p");
  eventDesc.textContent = content;
  eventDesc.setAttribute("id", `para_${key}`);

  contentDiv.appendChild(eventTitle);
  contentDiv.appendChild(eventDesc);

  const opbtnDiv = document.createElement("div");
  opbtnDiv.className = "op-btn";
  opbtnDiv.setAttribute("id", `op_${key}`);

  // const addBtn = document.createElement("button");
  // addBtn.className = "sm-btn";
  // addBtn.setAttribute("id", `add_${key}`);
  // const addImg = document.createElement("img");
  // addImg.src = "icons/plus-square.svg";
  // addImg.alt = "addEvent";
  // addBtn.appendChild(addImg);

  const editBtn = document.createElement("button");
  editBtn.className = "sm-btn";
  editBtn.setAttribute("id", `edit_${key}`);
  const editImg = document.createElement("img");
  editImg.src = "icons/edit-3.svg";
  editImg.alt = "editEvent";
  editImg.setAttribute("id", `edimg_${key}`);
  editBtn.appendChild(editImg);
  editBtn.addEventListener("click", () => editEvent(key));

  const delBtn = document.createElement("button");
  delBtn.className = "sm-btn";
  delBtn.setAttribute("id", `del_${key}`);
  const delImg = document.createElement("img");
  delImg.src = "icons/trash-2.svg";
  delImg.alt = "delEvent";
  delBtn.appendChild(delImg);
  delBtn.addEventListener("click", () => deleteEvent(key));

  // opbtnDiv.appendChild(addBtn);
  opbtnDiv.appendChild(editBtn);
  opbtnDiv.appendChild(delBtn);

  todoDiv.appendChild(expandDiv);
  todoDiv.appendChild(contentDiv);
  todoDiv.appendChild(opbtnDiv);

  const conatainer = document.getElementById("views");
  conatainer.appendChild(todoDiv);
}

// Fetch contents while is loding
window.onload = () => {
  count = localStorage.length;

  for (let i = 0; i < count; i++) {
    let id = localStorage.key(i)
    let value = JSON.parse(localStorage.getItem(id))
    let title = value["title"];
    let content = value["description"].replace(/\n{2,}/g, "\n");
    viewEvent(title, content, id);
  }
};

// function to expand the content
function expand(id) {
  const content = document.getElementById(`cont_${id}`);
  const btnImg = document.getElementById(`down_${id}`);

  const opDiv = document.getElementById(`op_${id}`);
  const todo = document.getElementById(id);

  scrlHeight = content.scrollHeight; // scrollHeight returns the actuall height of a content
  content.classList.toggle("active");
  // checks if the element containt the class active
  if (content.classList.contains("active")) {
    content.style.height = scrlHeight + "px";
    // sets the height of the element to  actuall height
    btnImg.src = "icons/chevron-up.svg";

    opDiv.style.opacity = 1;
    opDiv.style.visibility = "visible";
  } else {
    content.style.height = 4 + "em";
    btnImg.src = "icons/chevron-down.svg";
    opDiv.style.opacity = 0;
    opDiv.style.visibility = "hidden";
  }
}

// Function to edit the content
function editEvent(id) {
  const para = document.getElementById(`para_${id}`);
  const btnImg = document.getElementById(`edimg_${id}`);
  const title = document.getElementById(`title_${id}`).innerText;
  let state = para.getAttribute("contenteditable");
  if (state === "true") {
    const text = para.innerText;
    localStorage.setItem(
      id,
      JSON.stringify({
        title: title,
        description: text,
      })
    );
    para.setAttribute("contenteditable", false);
    para.style.border = 0;
    btnImg.src = "icons/edit-3.svg";
  } else {
    para.setAttribute("contenteditable", true);
    para.style.border = "1px solid";
    btnImg.src = "icons/check.svg";
  }
}

// Function to remove event
function deleteEvent(id) {
  user = confirm("Are You Sure!");
  if (user === true) {
    localStorage.removeItem(id);
    document.getElementById(id).remove();
    console.log("Item removed");
  }
}
