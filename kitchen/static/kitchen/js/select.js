var x, i;
x = document.getElementsByClassName("card");
for (i = 0; i < x.length; i++)
{
    select_ele = x[i].getElementsByTagName("select")[0];
    if (select_ele.value == "0")
    {
        select_ele.style.background = "red";
        select_ele.style.color = "white";
    }
}