class InforMationEvent {
    static #instance = null;
    static getInstance() {
        if (this.#instance == null) {
            this.#instance = new InforMationEvent();
        }
        return this.#instance;
    }

    addEventPhotoChangeClick() {
        const infoPhoto = document.querySelector(".info-photo");
        infoPhoto.onclick = () => {
            const photoFile = document.querySelector(".photo-file");
            photoFile.click();
        }
    }

    addEventPhotoChange() {
        const photoFile = document.querySelector(".photo-file");
        photoFile.onchange = () => {
            fileService.getInstance().changePhoto();
        }
    }

    addEventAboutMeModifyClick() {
        const aboutMeModifyButton = document.querySelector(".m-aboutme");
        aboutMeModifyButton.onclick = () => {
            const aboutMeSaveButton = document.querySelector(".s-aboutme");
            aboutMeSaveButton.classList.remove("button-hidden");
            aboutMeModifyButton.classList.add("button-hidden");
            
            const infoInputContainers = document.querySelectorAll(".info-input-container");
            infoInputContainers.forEach(infoInputContainer => {
                infoInputContainer.querySelector(".info-input").disabled = false;
            });
        }
    }

    addEventAboutMeSaveClick() {
        const aboutMeSaveButton = document.querySelector(".s-aboutme");
        aboutMeSaveButton.onclick = () => {
            const aboutMeModifyButton = document.querySelector(".m-aboutme");
            aboutMeModifyButton.classList.remove("button-hidden");
            aboutMeSaveButton.classList.add("button-hidden");
            
            const infoInputContainers = document.querySelectorAll(".info-input-container");
            const userInfo = InforMationService.getInstance().userInfo;
            
            infoInputContainers.forEach(infoInputContainer => {
                const infoInput = infoInputContainer.querySelector(".info-input");
                userInfo[infoInput.id] = infoInput.value;
                infoInput.disabled = true;
            });
           
            localStorage.setItem("userInfo",JSON.stringify(userInfo));
        }
    }


    addEventIntroduceModifyClick() {
        const IntroduceModifyButton = document.querySelector(".m-introduce");
        IntroduceModifyButton.onclick = () => {
            const IntroduceSaveButton = document.querySelector(".s-introduce");
            IntroduceSaveButton.classList.remove("button-hidden");
            IntroduceModifyButton.classList.add("button-hidden");
           
            const introduceInput = document.querySelector(".introduce-input");
            introduceInput.disabled = false;
        }
    }

    addEventIntroduceSaveClick() {
        const IntroduceSaveButton = document.querySelector(".s-introduce");
        
        IntroduceSaveButton.onclick = () => {
            const IntroduceModifyButton = document.querySelector(".m-introduce");
            IntroduceModifyButton.classList.remove("button-hidden");
            IntroduceSaveButton.classList.add("button-hidden");
            
            const introduceInput = document.querySelector(".introduce-input");
            const userInfo = InforMationService.getInstance().userInfo;
            introduceInput.disabled = true;
            userInfo["introduce"] = introduceInput.value;
            localStorage.setItem("userInfo",JSON.stringify(userInfo));
        }
    }
}

class InforMationService{
    static #instance = null;
    static getInstance() {
        if (this.#instance == null) {
            this.#instance = new InforMationService();
        }
        return this.#instance;
    }

    loadInfo(){
        this.loadInfoPhoto();
        this.loadInfoUser();
    }

    userInfo = {};

    loadInfoPhoto(){
        const infoPhotoImg = document.querySelector(".info-photo img");
        const infoPhoto = localStorage.getItem("infoPhoto")
        if(localStorage.getItem("infoPhoto") == null){
            infoPhotoImg.src ="./images/noimage.jpg";
        }else{
            infoPhotoImg.src = infoPhoto; 
        }
    }
    loadInfoUser(){
        this.userInfo = JSON.parse(localStorage.getItem("userInfo"));
        if(this.userInfo == null){
            this.userInfo = {};
            return;
        }
        Object.keys(this.userInfo).forEach(key =>{
            const infoInput = document.querySelectorAll(".info-input");
            infoInput.forEach(input => {
                if(input.id ==key){
                    input.value = this.userInfo[key];
                }
            });
        });
        if(typeof this.userInfo.introduce =='undefined'){
            return;
        }
        const introduceInfo = document.querySelector(".introduce-input");
        introduceInfo.value = this.userInfo.introduce;
    }
}

class fileService {
    static #instance = null;
    static getInstance() {
        if (this.#instance == null) {
            this.#instance = new fileService();
        }
        return this.#instance;
    }

    changePhoto() {
        const photoFrom = document.querySelector(".photo-form");
        const formData = new FormData(photoFrom);//FromData 내장객체
        const fileValue = formData.get("file");
        
        if(fileValue.size == 0){
            return;
        }

        this.showPreview(fileValue);
    }

    showPreview(fileValue) {
        const fileReader = new FileReader();

        fileReader.readAsDataURL(fileValue);//event가 발생

        fileReader.onload = (e) => {//event를 매개변수로 받음
            const photoImg = document.querySelector(".info-photo img");
            photoImg.src = e.target.result;//event의 결과값
            localStorage.setItem("infoPhoto",photoImg.src);
        }
    }

}


//     addEventInput(){
//     const modifyButtons = document.querySelectorAll(".modify-button");
//     const infoInputs = document.querySelectorAll(".info-input");
//     const introduceInfo = document.querySelector(".introduce-input");
//     for(let i = 0; i<modifyButtons.length; i++){
//         modifyButtons[i].onclick = () =>{
//             if(modifyButtons[i].classList.contains("m-aboutme")){
//                 modifyButtons[i].classList.add("button-hidden");
//                 infoInputs.forEach(infoinput => {
//                     infoinput.disabled = false;
//                 });
//                 modifyButtons[i+1].classList.remove("button-hidden");
//             }else if(modifyButtons[i].classList.contains("s-aboutme")){
//                 modifyButtons[i].classList.add("button-hidden");
//                 infoInputs.forEach(infoinput => {
//                     infoinput.disabled = true;
//                 });
//                 modifyButtons[i-1].classList.remove("button-hidden");

//             }
//             if(modifyButtons[i].classList.contains("m-introduce")){
//                 modifyButtons[i].classList.add("button-hidden");
//                 introduceInfo.disabled = false;
//                 modifyButtons[i+1].classList.remove("button-hidden");

//             } else if(modifyButtons[i].classList.contains("s-introduce")){
//                 modifyButtons[i].classList.add("button-hidden");
//                 introduceInfo.disabled = true;
//                 modifyButtons[i-1].classList.remove("button-hidden");
//             }

//         }
//     }
// }