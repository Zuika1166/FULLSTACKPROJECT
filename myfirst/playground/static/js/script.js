document.querySelector('button').onclick = btnclick;


// Click button Login Up
function btnclick() {
    let a = document.querySelector('.input1').value;

    console.log(a);
};



// Check CheckBox
function isCheckedCheckBox() {
    if (document.getElementById("checkbox").checked) {
        document.getElementById('CheckBoxAnswer').textContent='You Accept';
        }
        else {
            document.getElementById('CheckBoxAnswer').textContent='';
        }
    }

