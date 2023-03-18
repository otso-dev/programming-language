window.onload = () =>{//Only One
    AsideEvent.getInstance().addEventShowMenuButton();
    AsideEvent.getInstance().addEventMainChange();
    InforMationService.getInstance().loadInfo();
    InforMationEvent.getInstance().addEventPhotoChangeClick();
    InforMationEvent.getInstance().addEventPhotoChange();
    InforMationEvent.getInstance().addEventAboutMeModifyClick();
    InforMationEvent.getInstance().addEventAboutMeSaveClick();
    InforMationEvent.getInstance().addEventIntroduceModifyClick();
    InforMationEvent.getInstance().addEventIntroduceSaveClick();
    TodoService.getInstance();
    TodoEvent.getInstance().addEventAddTodoClick();
    TodoEvent.getInstance().addEventAddTodoKeyUp();
    // InforMationEvent.getInstance().addEventInput();
}