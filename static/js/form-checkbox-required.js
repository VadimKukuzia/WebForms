function handleData()
{
    var form_data = new FormData(document.querySelector("form"));

    if(!form_data.has("education_direction"))
    {
        document.getElementById("chk_option_error").style.visibility = "visible";
        return false;
    }
    else
    {
        document.getElementById("chk_option_error").style.visibility = "hidden";
        return true;
    }

}