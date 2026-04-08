let userscr=0;
let compscr=0;
const msg=document.querySelector("#msg");

const choices=document.querySelectorAll(".choices");

const draw=()=>{
    msg.innerText="IT WAS A DRAW, PICK AGAIN!"
};

const win=()=>{
    msg.innerText="YOU WIN THIS TIME, NOT AGAIN!"
};

const lose=()=>{
    msg.innerText="I WIN, DARE TO PICK AGAIN?"
};

const gameLogic=(user,comp)=>{
    if(user===comp){
        return 1;//draw
    }
    else if(user==='rock' && comp==='scissor'){
        return 2;//user win
    }
    else if(user==='rock' && comp==='paper'){
        return 3;//comp win
    }
    else if(user==='paper' && comp==='rock'){
        return 2;
    }
    else if(user==='paper' && comp==='scissor'){
        return 3;
    }
    else if(user==='scissor' && comp==='rock'){
        return 3;
    }
    else if(user==='scissor' && comp==='paper'){
        return 2;
    }

};

const compChoice=()=>{
    const options=["rock", "paper", "scissor"];
    const inx=Math.floor(Math.random()*3);
    return options[inx];
};

const game=(userchoice)=>{
    console.log("The user picked", userchoice);
    randomCompChoice=compChoice();
    console.log("Computer picked", randomCompChoice);
    const winner=gameLogic(userchoice,randomCompChoice);
    const victory=["","DRAW", "USER", "COMPUTER"];
    console.log("THE WINNER IS",victory[winner]);

    if(winner==1){
        draw();
    }
    else if(winner==2){
        userscr++;
        win();
    }
    else if(winner==3){
        compscr++;
        lose();
    }

    userScrPoints=document.querySelector("#user-scr");
    userScrPoints.innerText=userscr;

    compScrPoints=document.querySelector("#comp-scr");
    compScrPoints.innerText=compscr;

};

choices.forEach((choice)=>{
    choice.addEventListener("click", ()=> {
        const choiceid=choice.getAttribute("id");
        game(choiceid);

    })
});

