var createItemBtn = document.querySelector('[value="Create item"]');
var messageForm = document.querySelector('#message-form');
var cancelButton = document.querySelector('[value="Cancel"]');
var addItemBtn = document.querySelector('[value="Add new item"]');
var myList = document.querySelector('#my-list');
var todoAction = '';
var elementToEdit; 

createItemBtn.onclick = toggleMessageFormView;
cancelButton.onclick = toggleMessageFormView;
addItemBtn.onclick = addTodoItem;

function toggleMessageFormView() {
    messageForm.classList.toggle('visible');
}

function addTodoItem() {
    var textarea = document.querySelector('textarea');
    var todoItem = `<li>
                        <span>${textarea.value}</span>
                        <input type="button" value="" class="edit-btn" onclick="editItem(this)">
                        <input type="button" value="&times;" class="delete-btn" onclick="deleteItem(this)">
                    </li>`;

    if(todoAction === 'edit') {
        elementToEdit.children[0].innerText = textarea.value;
        todoAction = '';

    } else {
        myList.insertAdjacentHTML('beforeend', todoItem);
    }
    
    textarea.value = '';
    toggleMessageFormView();
}

function editItem(editBtn) {
    todoAction = 'edit';
    elementToEdit = editBtn.parentNode;
    toggleMessageFormView();
    document.querySelector('textarea').value = elementToEdit.innerText.trim();
}

function deleteItem(deleteBtn) {
        //myList.removeChild(deleteBtn.parentNode);
        deleteBtn.parentNode.style.textDecoration = 'line-through';
}