async function generateResponse(){

    const prompt =
    document.getElementById("prompt").value;

    const output =
    document.getElementById("output");

    if(prompt.trim()===""){
        output.innerHTML =
        "Please enter a question.";
        return;
    }

    output.innerHTML =
    "⏳ Generating response...";

    try{

        const response =
        await fetch("/generate",{
            method:"POST",
            headers:{
                "Content-Type":
                "application/json"
            },
            body:JSON.stringify({
                prompt:prompt
            })
        });

        const data =
        await response.json();

        output.innerHTML =
        data.response;

    }
    catch(error){

        output.innerHTML =
        "Something went wrong.";

    }
}