import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";
import base64 from 'base-64';
import axios from "axios";
import {useOpenCv} from "opencv-react";
import {OpenCvProvider} from "opencv-react";
function App() {
  const [state,setState]=useState()
   const { loaded, cv } = useOpenCv()
  useEffect(()=>{
    var oReq = new XMLHttpRequest();
    oReq.open("GET", 'http://127.0.0.1:8000/api/', true);
    oReq.setRequestHeader("Content-Type", "multipart/x-mixed-replace;boundary=frame;");
    oReq.onreadystatechange  = function() {
      if (oReq.readyState === 3) {
        var x = oReq.responseText.split("---osclivepreview---");
        console.log(oReq.status);
        let image = cv.decode(x[x.length-1]);
        setState(image);
        console.log(x[x.length - 1]);
      }
    };
    oReq.send(JSON.stringify({
      name: "camera.getLivePreview"
    }));

    console.log("effect");
  },)
  return (
   <div>

       {state}

     <h1>Hello</h1>

   </div>
  );
}

export default App;
