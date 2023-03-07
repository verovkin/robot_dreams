    function change_friends(friends_number){
        let friends_txt = document.getElementById("friends_number");
        friends_txt.innerText = `${friends_number}`;
    }
    let friends_counter = Math.floor(Math.random() * 101);
    change_friends(friends_counter)

    btn_add = document.getElementById("btn_add_friend");
    btn_add.onclick = (event) => {
        event.target.innerText = "Очікується підтвердження";
        event.target.disabled = true;
        change_friends(++friends_counter);
    }

    let btn_write = document.getElementById("btn_write");
    let style = getComputedStyle(btn_write);
    let prev_color = style['background-color'];
    let new_color = "rgb(100,255,60)";
    let color_changed = true;
    let color;
    btn_write.onclick = (event) => {
        color_changed = !color_changed;
        if (color_changed) { color = prev_color; }
        else { color = new_color; }
        btn_write.style.backgroundColor = color
        btn_write.style.borderColor = color
    }

    // let btn_job =
    document.getElementById("btn_job").onclick = (event) => {
        btn_add.parentElement.style.display = ((btn_add.parentElement.style.display!='none') ? 'none' : 'block');
    }


    let btns_container = document.getElementById("btns");

    let btn_pass_hw_container = document.createElement("div");
    btn_pass_hw_container.classList = "col-12 col-md-auto";
    let btn_pass_hw = document.createElement("button");
    btn_pass_hw.innerText = "Здати ДЗ";
    btn_pass_hw.classList = "btn btn-primary";
    btn_pass_hw.type = "button";
    btns_container.append(btn_pass_hw_container);
    btn_pass_hw_container.append(btn_pass_hw);


    btn_pass_hw.onclick = (event) => {


        let myTr = document.createElement('tr');

        let myTd1 = document.createElement("td");
        myTd1.innerHTML = "23"
        let myTd2 = document.createElement("td");
        myTd2.innerHTML = "Базовий JS"
        let myTd3 = document.createElement("td");
        myTd3.innerHTML = "5<span>/5</span>"

        let tbody = document.getElementsByTagName('tbody')[0];
        myTr.appendChild(myTd1);
        myTr.appendChild(myTd2);
        myTr.appendChild(myTd3);
        tbody.insertBefore(myTr, tbody.lastElementChild)
    }


    // myDiv.className = 'buttons';
    // myDiv.style.background = 'coral';
    // myDiv.style.textAlign = 'center'
