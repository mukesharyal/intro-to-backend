const userList = document.getElementById("userList");

const modal = document.getElementById("userModal");

const addModal = document.getElementById("addModal");

async function loadUsers(ageLimit){

    let url="/users";

    if(ageLimit){
        url+=`?ageLimit=${ageLimit}`;
    }

    const response=await fetch(url);

    const users=await response.json();

    userList.innerHTML="";

    users.forEach(user=>{

        const card=document.createElement("div");

        card.className="user-card";

        card.innerHTML=`
            <img src="/static/avatar.svg" class="avatar">
            <h3>${user.name}</h3>
        `;

        card.onclick=()=>showUser(user.id);

        userList.appendChild(card);

    });

}

async function showUser(id){

    const response=await fetch(`/users/${id}`);

    const user=await response.json();

    document.getElementById("modalName").innerText=user.name;

    document.getElementById("modalAge").innerText=user.age;

    document.getElementById("modalAddress").innerText=user.address;

    const hobbies=document.getElementById("modalHobbies");

    hobbies.innerHTML="";

    user.hobbies.forEach(hobby=>{

        const li=document.createElement("li");

        li.innerText=hobby;

        hobbies.appendChild(li);

    });

    modal.classList.remove("hidden");

}

document.querySelector(".close").onclick=()=>{
    modal.classList.add("hidden");
};

document.querySelector(".closeAdd").onclick=()=>{
    addModal.classList.add("hidden");
};

document.getElementById("searchBtn").onclick=()=>{

    const age=document.getElementById("ageInput").value;

    loadUsers(age);

};

document.getElementById("resetBtn").onclick=()=>{

    document.getElementById("ageInput").value="";

    loadUsers();

};

document.getElementById("newUserBtn").onclick=()=>{

    addModal.classList.remove("hidden");

};

document.getElementById("saveUser").onclick=async()=>{

    const body={

        name:document.getElementById("name").value,

        age:Number(document.getElementById("age").value),

        address:document.getElementById("address").value,

        hobbies:document
            .getElementById("hobbies")
            .value
            .split(",")
            .map(h=>h.trim())
    };

    await fetch("/users",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(body)

    });

    addModal.classList.add("hidden");

    loadUsers();

};

loadUsers();