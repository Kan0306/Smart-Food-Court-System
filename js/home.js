function showAccOptions()
{
    var x = document.getElementById("op-active");
    document.getElementById("acc").style.textDecoration = "none";
    if (x.style.display === "block")
    {
        x.style.display = "none";
    } else
    {
        x.style.display = "block";
        x.style.position = "absolute";
        x.style.background = "white";
        x.style.width = "220px";
        x.style.padding = "0px";
        x.style.margin = "0";
        x.style.left = "-140px";
        x.style.top = "20px";
        x.style.lineHeight = "30px";
        x.style.zIndex = "1";
        x.style.fontSize = "14px";
    }
    
}