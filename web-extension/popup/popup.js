const popupButton = document.getElementById("popup-button")
const assistantButton = document.getElementById("popup-button-url-assistant")
const popupInput = document.getElementById("popup-input")
const popupInputMessage = document.getElementById("popup-input-message")
const loader = document.querySelector('.loader')
const containerResponse = document.querySelector('.popup-response')
const containerGPT = document.querySelector(".popup-gpt-container")
const bodyGPT = document.querySelector("#popup-gpt-body")
let modelProbability = 0
let urlToCheck = ""
//writing the document with the fethed data got it from the API and from the fine tuned model
const fetchModelProbability = async (text) => {
	containerResponse.innerHTML = ''
	containerResponse.append(loader)
	loader.style.display = "inline-block"
  urlToCheck = text
  fetch("http://3.15.208.82/predict/", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      "accept": "application/json"
    },
    body: JSON.stringify({url: text})
  }).then((response) => {
    if(!response.ok){
      throw new Error('Error 500,  the server response was not ok')
    }
    return response.json()
  })
    .then( data => {
      modelProbability = parseFloat(data.probability.slice(0,-1))
      loader.style.display = "none"
      containerResponse.innerHTML =`
        <p class="popup-response-message"> It is ${data.probability} likely to be a phishing url, </p>
        <p class="popup-response-message">is considered ${data.classification}</p>
        `
      assistantButton.style.display = "block"
    })
    .catch(error => {
      console.error(error)
    })
}
const fetchAsistanceThoughts = () => {
  fetch("http://3.15.208.82/url-assistant/",{
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      "accept": "application/json"
    },
    body: JSON.stringify(({ percentage: modelProbability, url: urlToCheck }))
  }).then( responseAsistant => {
    if (!responseAsistant.ok) {
      throw new Error('Error 500,  the server response was not ok')
    }
    return responseAsistant.json()
  })
    .then( dataAsistant => {
      console.log(dataAsistant)
      const bulletPoints = dataAsistant.data.split("\n")
      const ul = document.createElement("ul")
      bulletPoints.forEach(element => {
        const li = document.createElement("li")
        const newElement = element.replace("-", "")
        li.textContent = newElement
        ul.appendChild(li)
      });
      const newContent = `
        <div class="popup-gpt-title-container">
          <h2 class="popup-gpt-title">ChatGPT says</h2>
          <img class="popup-gpt-underline" src="/favicon_io/underline.png"/>
        </div>
      `
      containerGPT.innerHTML = newContent
      containerGPT.appendChild(ul)
    })
}

const fetchModelMessage = (message) => {
	containerResponse.innerHTML = ''
	containerResponse.append(loader)
  loader.style.display = "inline-block"
  fetch("http://3.15.208.82/message-assistant/", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      "accept": "application/json"
    },
    body: JSON.stringify({message: message})
  }).then((response) => {
    if(!response.ok){
      throw new Error('Error 500,  the server response was not ok')
    }
    return response.json()
  })
    .then( data => {
      loader.style.display = "none"

      console.log(data)
      const bulletPoints = data.data.split("\n")
      const ul = document.createElement("ul")
      bulletPoints.forEach(element => {
        const li = document.createElement("li")
        const newElement = element.replace("-", "")
        li.textContent = newElement
        ul.appendChild(li)
      });
      containerResponse.append(ul)
    })
    .catch(error => {
      console.error(error)
    })
}

popupButton.addEventListener("click", () => {
	const inputValue = popupInput.value
  const inputMessageValue = popupInputMessage.value
	if(inputValue.length > 0) {
		return fetchModelProbability(inputValue)
  }else if(inputMessageValue.length > 0){
    fetchModelMessage(inputMessageValue)
  }
})
assistantButton.addEventListener("click", () => {
  assistantButton.style.display = "none"
  loader.style.display = "inline-block"
  containerGPT.append(loader)
  fetchAsistanceThoughts()
})
