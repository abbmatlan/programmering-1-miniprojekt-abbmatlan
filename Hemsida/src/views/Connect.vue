<template>
 <v-container
   full-height
   style="height:75%; "
  >
 <v-container style="display: flex;  align-items: center; align-content: flex-start; flex-direction: column; height: 100%;">        
<v-row> 
  <v-col>
      <v-switch
               @change="send()"
               v-model="Message"
               :label="`On/Off Color`"
               align-center
            
             ></v-switch>
    </v-col>
<v-col style="align-items: end; justify-content: middle; "> 
   </v-col>

    </v-row>
<v-row style="height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
           <color-picker v-bind="color" @input="onInput" id="copi"></color-picker>
         
         <v-btn @click="uppdatera()" class="mt-5">Choose</v-btn>
             </v-row>
    </v-container>  
  </v-container>
</template>

<script>
var mqtt = require("mqtt");                  //Berättar att man använder MQTT
export default {
  components: { ColorPicker },
  data() {                                   //datan programmet arbetar med
    return {                                 //datan man returnerar vid förändring av sliden
       devices: [],
      Name: "",
      bruh: 0,
      value: 1,
      Message: false,
      client: undefined,
      clientId: "Ahahah",                          //vad klienten heter
      user: "jesper.ribe@abbindustrigymnasium.se",  //MQTT publishern
      pass: "samstalosenordet",                      //lösenordet
      connected: false,
      
      color: {
        //sätter värde allt nedanför "standardFärgen"
        hue: 50, 
        saturation: 100,
        luminosity: 50,
        alpha: 1
      }
    };
  },
  
  methods: {

      connect() {
      var mqtt_url = "maqiatto.com";                      //Broker adressen som vi använder
      var url = "mqtt://" + mqtt_url;                       //definerar det som ska vara innan url:n
      var options = {
        port: 8883,                                      //porten för att publisha
        clientId:                                         //genererar ett random clientId för att annars skulle alla få samma
          "mqttjs_" +
          Math.random()
            .toString(16)
            .substr(2, 8),
        username: this.user,                           //användarnamn
        password: this.pass                             //lösenord
      };
      console.log("connecting");                       
      this.client = mqtt.connect(url, options);
      console.log("connected?");                      //frågar om det har connectat

      this.client
        .on("error", function() {
          console.log("no");                        // vid fel consol loggar "no"
        })
        .on("close", function() {
          console.log("no");                        // vid fel consol loggar "no"
        });
      this.connected = true;
      console.log(this.connected);                    //loggar om den har connectat
    },
  }
};
</script>

<style>

#lay{
    display: flex;
    align-items: center;
    justify-content: center;
}

#copi{
  width:250px;
  height: 250px;
}

@import "~@radial-color-picker/vue-color-picker/dist/vue-color-picker.min.css";
</style>
