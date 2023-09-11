@import url(https://fonts.googleapis.com/css?family=Shadows+Into+Light);

@import url(https://fonts.googleapis.com/css?family=Gloria+Hallelujah);

#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
  overflow: scroll;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}

.button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  text-decoration: none;
  color: white;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
.button:hover {
  border-color: #646cff;
}
.button:focus,
.button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

body {
  background-color: #6D7993;
  margin: 20px;
}

/* .tab-panel {

} */

.tab-panel__header {
  font-family: 'Trebuchet MS';
  font-size: 12px;
  position: relative;
  top: 1px
}

.tab-panel__content {
  background-color: #D5D5D5;
  border: 1px solid #9099A2;
  min-height: 450px;
  min-width: 900px;
  overflow: scroll;
} 

.tab {
  background-color: #D5D5D5;
  border: 1px solid #9099A2;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  color: #96858F;
  cursor: pointer;
  display: inline-block;
  padding: 6px 24px;
  position: relative;
  text-transform: uppercase;
  z-index: 0;
}

.tab:nth-child(n+2) {
    margin-left: -8px;
}

.tab:hover {
  color: #6D7993;
}

.tab--selected {
  border-bottom: 1px solid #D5D5D5;
  color: #6D7993;
  font-size: 14px;
  font-weight: bold;
  padding-top: 6px;
  z-index: 1;
}


nav {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 40px;
}


* { box-sizing:border-box; }

body { background:url(https://subtlepatterns.com/patterns/little_pluses.png) #cacaca; margin:30px; }

#create, textarea  { 
  float:left; 
  padding:25px 25px 40px;
  margin:0 20px 20px 0;
  width:250px;
  height:250px; 
}

#create {
  float:left; 
  padding:25px 25px 40px;
  margin:0 20px 20px 0;
  width:250px;
  height:250px; 

  user-select:none;
  padding:10px; 
  border-radius:20px;
  text-align:left; 
  border:3px solid rgba(0, 0, 0, 0.224); 
  cursor:pointer;
  color:rgb(0, 0, 0);
  font:25px  "Roboto", sans-serif;
  
  line-height:30px;
}

#create:hover { border-color:rgba(0,0,0,0.2); color:rgb(47, 47, 47); }

textarea {
  font:20px 'Gloria Hallelujah', cursive; 
  line-height:1.5;
  border:0;
  border-radius:3px;
  background: linear-gradient(#F9EFAF, #F7E98D);
  box-shadow:0 4px 6px rgba(0,0,0,0.1);
  overflow:hidden;
  transition:box-shadow 0.5s ease;
  /* font-s:subpixel-antialiased; */
  max-width:500px;
  max-height:2450px;
}
textarea:hover { box-shadow:0 5px 8px rgba(0,0,0,0.15); }
textarea:focus { box-shadow:0 5px 12px rgba(0,0,0,0.2); outline:none; }




body,
html,
div.board,
div#react-container {
    height: 100%;
    overflow: hidden;
}

body {
    margin: 0;
    padding: 0;
}

div.board {
    /* background-color: brown; */
    width: 100%;
    /* background: #eab92d; */
    /* background: -moz-radial-gradient(center, ellipse cover, #eab92d 57%, #c79810 99%);
    background: -webkit-gradient(radial, center center, 0px, center center, 100%, color-stop(57%, #eab92d), color-stop(99%, #c79810));
    background: -webkit-radial-gradient(center, ellipse cover, #eab92d 57%, #c79810 99%);
    background: -o-radial-gradient(center, ellipse cover, #eab92d 57%, #c79810 99%);
    background: -ms-radial-gradient(center, ellipse cover, #eab92d 57%, #c79810 99%);
    background: radial-gradient(ellipse at center, #eab92d 57%, #c79810 99%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#eab92d', endColorstr='#c79810', GradientType=1); */

}

div.note{
    height: 150px;
    width: 150px;
    background-color: yellow;
    margin: 2px 0;
    position: absolute;
    cursor: -webkit-grab;
    -webkit-box-shadow: 5px 5px 15px 0 rgba(0, 0, 0, .2);
    box-shadow: 5px 5px 15px 0 rgba(0, 0, 0, .2);
   

}

div.note:active {
    cursor: -webkit-grabbing;
}

div.note p {
    font-size: 22px;
    padding: 5px;
    font-family: "Shadows Into Light", Arial;
}

div.note:hover > span {
    opacity: 1;
}

div.note > span {
    position: absolute;
    bottom: 2px;
    right: 2px;
    opacity: 0;
    transition: opacity .25s linear;
}

div.note button {
    margin: 2px;
}

div.note > textarea {
    height: 75%;
    background: rgba(255, 255, 255, .5);
}

div.note react-draggable {
    top: var(--random-top);
    left: var(--random-left);
 
}

.paragraph--type--snap-state-list-popup .usa-state-map a,
.paragraph--type--snap-state-list-popup .usa-state-map a:focus {
    fill: #757575;
}

/* Color change on hover for all state links */
.a:hover  {
    fill: #006600; /* Change to the desired hover color */
}


 .paragraph--type--snap-state-list-popup .usa-state-map text {

    font-family:Helvetica,Arial,sans-serif;
    fill: #ffffff;
    }

text {
    text-rendering: auto;
}