import * as PIXI from 'pixi.js';
import $ from "jquery";
import { Live2DModel } from 'pixi-live2d-display/cubism4';
window.PIXI = PIXI;

const app = new PIXI.Application({
    view: document.getElementById("canvas2"),
    autoStart: true,
    // resizeTo: window
  });

const cubism4Model = "assets/haru/haru_greeter_t03.model3.json";
const model = await Live2DModel.from(cubism4Model);

app.stage.addChild(model);

// transforms
model.x = 900;
model.y = 0;
model.rotation = Math.PI;
model.skew.x = Math.PI;
model.scale.set(0.45);

// 设置嘴型
const setMouthOpenY = v=>{
    v = Math.max(0,Math.min(1,v));
    model.internalModel.coreModel.setParameterValueById('ParamMouthOpenY',v);
}


setInterval(()=>{
    $.ajax({
        type : "GET",
        url : "/api/get_mouth_y",
        dataType: 'json',
        async: true,
        success(data) {
            setMouthOpenY(parseFloat(data.y))
        },
    });
}, 10)
