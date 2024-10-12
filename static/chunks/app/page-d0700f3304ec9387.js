(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[931],{4760:function(e,t,s){Promise.resolve().then(s.bind(s,7143)),Promise.resolve().then(s.bind(s,6590)),Promise.resolve().then(s.bind(s,2102)),Promise.resolve().then(s.bind(s,3953)),Promise.resolve().then(s.bind(s,845)),Promise.resolve().then(s.t.bind(s,2972,23))},6590:function(e,t,s){"use strict";s.d(t,{default:function(){return w}});var a=s(7437),i=s(3145),r=s(97),n=s(2265),l=s(9811),o=s(875),c=s(4508);let d=l.fC,h=n.forwardRef((e,t)=>{let{className:s,...i}=e;return(0,a.jsx)(l.ck,{ref:t,className:(0,c.cn)("border-b",s),...i})});h.displayName="AccordionItem";let x=n.forwardRef((e,t)=>{let{className:s,children:i,...r}=e;return(0,a.jsx)(l.h4,{className:"flex",children:(0,a.jsxs)(l.xz,{ref:t,className:(0,c.cn)("flex flex-1 items-center justify-between py-4 font-medium transition-all hover:underline [&[data-state=open]>svg]:rotate-180",s),...r,children:[i,(0,a.jsx)(o.Z,{className:"h-4 w-4 shrink-0 transition-transform duration-200"})]})})});x.displayName=l.xz.displayName;let m=n.forwardRef((e,t)=>{let{className:s,children:i,...r}=e;return(0,a.jsx)(l.VY,{ref:t,className:"overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down",...r,children:(0,a.jsx)("div",{className:(0,c.cn)("pb-4 pt-0",s),children:i})})});m.displayName=l.VY.displayName;var u=s(1936);let p=[{id:1,qs:"can you work on my project immediately?",answer:"Yes, if i am not currently engaged in other commitments, otherwise i will get the jobe done in deadline"},{id:2,qs:"What experience do you have with front-end development?",answer:"I have 5 years of experience working with front-end development creating responsive, user-friendly websites and web applications"},{id:3,qs:"How proficient are you with WordPress?",answer:" I’ve worked on multiple WordPress projects, customizing themes, developing plugins, and optimizing sites for performance, SEO, and user experience."}],f={initial:{x:"0%"},animate:{x:"-50%",transition:{duration:30,repeat:1/0,ease:"linear",repeatType:"loop"}}},g=[{src:"/tech/wordpress.svg",width:46.14,height:45.24,alt:"Wordpress"},{src:"/tech/node.svg",width:106.2,height:31,alt:"Node.js"},{src:"/tech/ts.svg",width:46.14,height:45.24,alt:"TypeScript"},{src:"/tech/shopify.svg",width:54.98,height:48.73,alt:"Shopify"},{src:"/tech/framer.svg",width:47.48,height:52.48,alt:"Framer"},{src:"/tech/figma.svg",width:47.48,height:52.48,alt:"Figma"},{src:"/tech/react.svg",width:54.98,height:48.73,alt:"React"},{src:"/tech/angular.svg",width:47.48,height:51.23,alt:"Angular"},{src:"/tech/css.svg",width:54.98,height:45.24,alt:"Css"},{src:"/tech/js.svg",width:54.98,height:51.23,alt:"Js"},{src:"/tech/html.svg",width:54.98,height:51.23,alt:"Html"},{src:"/tech/elementor.svg",width:54.98,height:51.23,alt:"elementor"},{src:"/tech/git.svg",width:43.73,height:51.23,alt:"Git"},{src:"/tech/github.svg",width:43.73,height:51.23,alt:"Github"}];var w=()=>(0,a.jsxs)("section",{id:"FAQ",className:"bg-white py-20",children:[(0,a.jsxs)("div",{className:"container mx-auto sm:px-2",children:[(0,a.jsxs)("h1",{className:"text-5xl font-bold text-center text-gray-900 leading-tight",children:["Frequently ",(0,a.jsx)("br",{})," ",(0,a.jsx)("span",{className:"text-gray-600 underline",children:"Asked"})]}),(0,a.jsx)(r.E.div,{variants:(0,u.Z)("up",.2),initial:"hidden",whileInView:"show",viewport:{once:!0,amount:.8},className:"mt-12 mx-auto max-w-2xl bg-white rounded-lg shadow-xl p-6 sm:p-8",children:p.map(e=>(0,a.jsx)(d,{type:"single",collapsible:!0,className:"w-full text-left",children:(0,a.jsxs)(h,{value:"item-".concat(e.id),children:[(0,a.jsx)(x,{className:"flex justify-between items-center text-xl font-semibold text-gray-800 py-4 px-2 hover:bg-gray-100 transition duration-200",children:e.qs}),(0,a.jsx)(m,{className:"px-4 py-2 text-base text-gray-700 border-t",children:e.answer})]})},e.id))})]}),(0,a.jsx)("div",{className:"mt-36 relative w-full overflow-hidden",children:(0,a.jsx)("div",{className:"flex justify-center",children:(0,a.jsx)("div",{className:"w-full max-w-[1200px] overflow-hidden",children:(0,a.jsxs)(r.E.div,{variants:f,initial:"initial",animate:"animate",className:"flex gap-16 items-center whitespace-nowrap",children:[g.map((e,t)=>(0,a.jsx)("div",{className:"flex-shrink-0",children:(0,a.jsx)(i.default,{src:e.src,width:e.width,height:e.height,alt:e.alt,className:"transition-transform duration-300 hover:scale-110 shadow-sm filter grayscale hover:filter-none"})},"first-".concat(t))),g.map((e,t)=>(0,a.jsx)("div",{className:"flex-shrink-0",children:(0,a.jsx)(i.default,{src:e.src,width:e.width,height:e.height,alt:e.alt,className:"transition-transform duration-300 hover:scale-110 shadow-sm filter grayscale hover:filter-none"})},"second-".concat(t)))]})})})})]})},7143:function(e,t,s){"use strict";var a=s(7437),i=s(4743),r=s(2265),n=s(97),l=s(1936),o=s(2926);t.default=()=>{let[e,t]=(0,r.useState)({name:"",subject:"",message:""}),s=s=>{t({...e,[s.target.name]:s.target.value})};return(0,a.jsx)("section",{id:"Contact",className:"bg-white py-28",children:(0,a.jsxs)("div",{className:"container flex flex-col justify-between px-6 md:flex-row",children:[(0,a.jsx)(n.E.div,{variants:(0,l.Z)("right",.2),initial:"hidden",whileInView:"show",viewport:{once:!0,amount:.8},className:"mb-12 mr-6 flex items-center py-6",children:(0,a.jsxs)("h1",{className:"text-4xl font-extrabold leading-tight text-gray-800",children:["Let's Work ",(0,a.jsx)("br",{})," ",(0,a.jsx)("span",{className:"text-blue-600 underline",children:"Together"})]})}),(0,a.jsxs)(n.E.form,{onSubmit:s=>{s.preventDefault(),o.ZP.send("service_jnkcmsn","template_ch3lr07",{from_name:e.name,subject:e.subject,message:e.message,to_email:"shiralimohammadi47@gmail.com"},"YOUR_USER_ID").then(e=>{console.log("Message sent: ",e.text)},e=>{console.log("Failed to send: ",e.text)}),t({name:"",subject:"",message:""})},variants:(0,l.Z)("left",.2),initial:"hidden",whileInView:"show",viewport:{once:!0,amount:.8},className:"flex max-w-xl flex-1 flex-col items-start gap-y-6 rounded-lg bg-white shadow-md p-10 transition-transform duration-300 hover:shadow-lg",children:[(0,a.jsx)("input",{type:"text",name:"name",value:e.name,onChange:s,placeholder:"Your Name",required:!0,className:"w-full border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0"}),(0,a.jsx)("input",{type:"text",name:"subject",value:e.subject,onChange:s,placeholder:"Subject",required:!0,className:"w-full border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0"}),(0,a.jsx)("textarea",{name:"message",id:"message",value:e.message,onChange:s,placeholder:"Your Message",required:!0,className:"mb-6 w-full resize-none border-b-2 border-gray-300 bg-transparent py-3 outline-none text-gray-800 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-0"}),(0,a.jsxs)("button",{type:"submit",className:"flex items-center justify-between gap-x-2 rounded-full bg-blue-600 px-6 py-3 text-white transition-all duration-300 hover:bg-blue-700",children:[(0,a.jsx)("p",{className:"text-md font-semibold capitalize",children:"Send Message"}),(0,a.jsx)(i.Z,{className:"h-5 w-5"})]})]})]})})}},2102:function(e,t,s){"use strict";var a=s(7437);s(2265);var i=s(3145),r=s(97);t.default=()=>(0,a.jsx)("div",{className:"relative flex items-center justify-center h-full",children:(0,a.jsx)(r.E.div,{initial:{opacity:0},animate:{opacity:1,transition:{delay:.1,duration:.4,ease:"easeIn"}},className:"relative flex items-center justify-center",children:(0,a.jsxs)(r.E.div,{initial:{opacity:0},animate:{opacity:1,transition:{delay:.5,duration:.4,ease:"easeIn"}},className:"relative",children:[(0,a.jsxs)(r.E.svg,{initial:{opacity:.8},animate:{opacity:1,rotate:[120,360]},transition:{duration:20,repeat:1/0,repeatType:"reverse",delay:1},className:"h-[300px] w-[300px] lg:h-[580px] lg:w-[580px]",viewBox:"0 0 537 537",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,a.jsx)("path",{d:"M156.815 121.725C159.44 124.929 158.97 129.655 155.766 132.28C152.562 134.905 147.836 134.435 145.211 131.231C142.586 128.026 143.056 123.301 146.26 120.676C149.465 118.051 154.19 118.521 156.815 121.725Z",fill:"#274FB2"}),(0,a.jsx)("path",{d:"M389.242 407.037C391.866 410.241 391.397 414.967 388.193 417.591C384.988 420.216 380.263 419.747 377.638 416.542C375.013 413.338 375.483 408.613 378.687 405.988C381.891 403.363 386.617 403.833 389.242 407.037Z",fill:"#274FB2"}),(0,a.jsx)("circle",{cx:"267.683",cy:"268.113",r:"183",transform:"rotate(-39.3234 267.683 268.113)",stroke:"#274FB2",strokeOpacity:"0.7",strokeWidth:"2"}),(0,a.jsx)("circle",{cx:"268",cy:"268",r:"254",stroke:"#274FB2",strokeOpacity:"0.9",strokeWidth:"2"}),(0,a.jsx)("path",{d:"M520.634 279.082C514.761 277.528 511.26 271.507 512.815 265.634C514.369 259.761 520.39 256.26 526.263 257.815C532.136 259.369 535.637 265.39 534.082 271.263C532.528 277.136 526.507 280.637 520.634 279.082Z",fill:"#274FB2"}),(0,a.jsx)("path",{d:"M10.6338 279.082C4.76093 277.528 1.26011 271.507 2.81453 265.634C4.36895 259.761 10.39 256.26 16.2629 257.815C22.1358 259.369 25.6366 265.39 24.0822 271.263C22.5278 277.136 16.5067 280.637 10.6338 279.082Z",fill:"#274FB2"}),(0,a.jsx)("path",{d:"M279.082 16.2629C277.528 22.1358 271.507 25.6366 265.634 24.0822C259.761 22.5278 256.26 16.5067 257.815 10.6338C259.369 4.76093 265.39 1.26011 271.263 2.81453C277.136 4.36895 280.637 10.39 279.082 16.2629Z",fill:"#274FB2"}),(0,a.jsx)("path",{d:"M279.082 526.263C277.528 532.136 271.507 535.637 265.634 534.082C259.761 532.528 256.26 526.507 257.815 520.634C259.369 514.761 265.39 511.26 271.263 512.815C277.136 514.369 280.637 520.39 279.082 526.263Z",fill:"#274FB2"})]}),(0,a.jsx)(r.E.div,{initial:{opacity:0},animate:{opacity:1,transition:{delay:.3,duration:.4,ease:"easeIn"}},className:"absolute inset-0 flex items-center justify-center",children:(0,a.jsx)(i.default,{src:"/hero/Group 6.svg",height:580,width:580,alt:"profile",className:"object-contain"})})]})})})},3953:function(e,t,s){"use strict";s.d(t,{Project:function(){return d}});var a=s(7437),i=s(2265),r=s(3145),n=s(7648),l=s(4769),o=s(4317),c=s(97);let d=e=>{let{title:t,image:s,category:d,description:h,index:x}=e,m=(0,i.useRef)(null),{scrollYProgress:u}=(0,l.v)({target:m,offset:["0 1","1.33 1"]}),p=(0,o.H)(u,[0,1],[.95,1]),f=(0,o.H)(u,[0,1],[.75,1]);return(0,a.jsxs)(c.E.div,{ref:m,style:{scale:p,opacity:f},className:"flex flex-col items-center bg-white rounded-xl shadow-lg p-8 transition-transform hover:-translate-y-2 hover:shadow-xl xl:flex-row xl:justify-between",children:[(0,a.jsxs)("div",{className:"text-center xl:text-left xl:w-1/2 ".concat(x%2==0?"xl:pr-8":"xl:pl-8"),children:[(0,a.jsx)("h5",{className:"text-sm font-bold text-blue-600 uppercase tracking-wide",children:d}),(0,a.jsx)("h3",{className:"mt-4 text-2xl font-semibold text-gray-800 leading-tight",children:t}),(0,a.jsx)("p",{className:"mt-4 text-base text-gray-600 max-w-lg leading-relaxed",children:h}),(0,a.jsx)(n.default,{href:["https://shir.framer.website/","https://afgweb.com.au/","https://42adelaide.netlify.app/"][x],target:"_blank",rel:"noopener noreferrer",className:"mt-6 inline-block text-sm font-medium text-blue-600 hover:underline",children:"View Details"})]}),(0,a.jsx)("div",{className:"relative mt-6 w-full xl:w-1/2 h-80 xl:h-96",children:(0,a.jsx)(r.default,{src:s,width:384,height:384,alt:"".concat(t," project image"),className:"rounded-lg object-cover transition-transform duration-500 ease-in-out hover:scale-105 shadow-md"})})]})}},845:function(e,t,s){"use strict";s.d(t,{default:function(){return h}});var a=s(7437),i=s(97),r=s(1936),n=s(3433),l=s(1534),o=s(2396),c=s(2265);function d(e){let{from:t,to:s,animationOptions:i}=e,r=(0,c.useRef)(null),d=(0,n.Y)(r,{once:!0});return(0,l.L)(()=>{let e=r.current;if(!e||!d)return;e.textContent=String(t);let a=(0,o.j)(t,s,{duration:1.5,ease:"easeOut",delay:.6,...i,onUpdate(t){e.textContent=t.toFixed(0)}});return()=>{a.stop}},[r,d,t,s]),(0,a.jsx)("span",{ref:r})}var h=()=>(0,a.jsx)("section",{id:"services",className:"relative z-30 bg-white py-20",children:(0,a.jsx)("div",{className:"container mx-auto w-full py-[100px] lg:py-[200px]",children:(0,a.jsxs)("div",{className:"flex flex-col justify-between gap-12 px-4 lg:flex-row lg:px-0",children:[(0,a.jsxs)(i.E.div,{variants:(0,r.Z)("right",.2),initial:"hidden",whileInView:"show",viewport:{once:!0,amount:.8},className:"flex flex-col justify-between lg:mr-8 lg:w-1/2",children:[(0,a.jsx)("h1",{className:"pb-4 text-5xl font-extrabold leading-tight text-blue-800",children:"What I Do"}),(0,a.jsx)("p",{className:"mb-8 text-xl text-gray-600",children:"I specialize in designing and developing responsive, user-friendly websites and web applications. With expertise in HTML, CSS, JavaScript, and frameworks like React and Angular, I create clean, modern interfaces that deliver seamless user experiences. I also focus on UI/UX design, optimizing websites for performance, and integrating custom features for platforms like WordPress and Shopify. Whether you need a landing page, full website, or app interface, I turn your ideas into polished, functional digital products."}),(0,a.jsxs)("div",{className:"flex justify-between space-x-12 py-8",children:[(0,a.jsxs)("div",{className:"flex flex-col items-center",children:[(0,a.jsx)("p",{className:"text-lg font-semibold uppercase text-gray-500",children:"Projects"}),(0,a.jsxs)("p",{className:"text-5xl font-bold text-blue-700",children:["+ ",(0,a.jsx)(d,{from:0,to:50})]})]}),(0,a.jsxs)("div",{className:"flex flex-col items-center",children:[(0,a.jsx)("p",{className:"text-lg font-semibold uppercase text-gray-500",children:"Satisfied Clients"}),(0,a.jsx)("p",{className:"text-5xl font-bold text-blue-700",children:(0,a.jsx)(d,{from:0,to:25})})]})]})]}),(0,a.jsx)(i.E.div,{variants:(0,r.Z)("left",.4),initial:"hidden",whileInView:"show",viewport:{once:!0,amount:.8},className:"flex flex-col gap-8 lg:w-1/2",children:[{title:"Front-end Development",number:"01",description:"Convert your Figma/XD design to a fully responsive web app with React/Next.js, Angular, or HTML with Tailwind CSS"},{title:"WordPress and Shopify",number:"02",description:"Customization theme , plugin integration, and performance optimization. Whether it’s a landing page, e-commerce store, or complete website, I deliver polished, functional, and SEO-optimized digital solutions tailored to your needs."}].map(e=>(0,a.jsxs)("div",{className:"flex transform items-center space-x-6 rounded-lg border-l-4 border-blue-600 bg-white p-6 shadow-lg transition-transform hover:scale-105 hover:shadow-2xl",children:[(0,a.jsx)("p",{className:"text-6xl font-extrabold text-blue-700",children:e.number}),(0,a.jsxs)("div",{children:[(0,a.jsx)("h2",{className:"mb-2 text-2xl font-semibold text-gray-800",children:e.title}),(0,a.jsx)("p",{className:"text-gray-600",children:e.description})]})]},e.number))})]})})})},4508:function(e,t,s){"use strict";s.d(t,{cn:function(){return r}});var a=s(1994),i=s(3335);function r(){for(var e=arguments.length,t=Array(e),s=0;s<e;s++)t[s]=arguments[s];return(0,i.m6)((0,a.W)(t))}},1936:function(e,t,s){"use strict";function a(e,t){return{hidden:{y:"up"===e?80:"down"===e?-80:0,opacity:0,x:"left"===e?80:"right"===e?-80:0},show:{y:0,x:0,opacity:1,transition:{type:"tween",duration:1.2,delay:t,ease:[.25,.25,.25,.75]}}}}s.d(t,{Z:function(){return a}})}},function(e){e.O(0,[160,53,971,117,744],function(){return e(e.s=4760)}),_N_E=e.O()}]);