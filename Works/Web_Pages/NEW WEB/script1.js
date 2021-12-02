function msg(){
    alert("Hello Webpage");

}
setInterval(liveclock,1000);
function liveclock(){
    const time = new Date();
    const hrs = time.getHours();
    const min = time.getMinutes();
    const sec = time.getSeconds();

    if(hrs>12){
        hrs=hrs-12;
    }
    if (hrs==0){
        hrs=12;
    }
    document.getElementById('clock').innerHTML= hrs + ':'+min+ ':' +sec;
}
liveclock();