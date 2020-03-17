function RandomColor() {
    var hex = (Math.round(Math.random()*0xffffff)).toString(16);
    while (hex.length < 6) hex = "0" + hex;
    return hex;
  }

function SetRandomColor()
{
    var clr_div = document.getElementById("colorDiv");
    var random_color = RandomColor();
    random_color = '#'+random_color;
    console.log(random_color);
    clr_div.style.backgroundColor = random_color;
}