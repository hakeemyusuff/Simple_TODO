//To clear the input fied after adding a task
const inputField = document.querySelector('.btn')
inputField.addEventListener('htmx:afterRequest', () => {
  document.querySelector(".task-input").value = ''
})