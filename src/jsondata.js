
/*
const jsonData = `[
  {"id" : "1", "name" : "tanaka"},
  {"id" : "2", "name" : "nakata"}
]`;
*/

const jsonData = `[
  {
   "label" : "row label01", 
   "bars" : [
              { 
               "beginDate"      : "2021/06/14 13:00", 
	       "endDate"        : "2021/07/05 19:00", 
	       "ganttBarConfig" : {
	                             "id"    : "1592311881",
                                     "label" : "I'm in a bundle",
                                     "style" : {
                                       "background": "magenta"
                                     }
                                  }
   	      } 
	     ]
  }
  ,

  {
   "label" : "row label02", 
   "bars" : [
              { 
               "beginDate"      : "2021/06/20 13:00", 
	       "endDate"        : "2021/06/25 19:00", 
	       "ganttBarConfig" : {
	                             "id"    : "1592311882",
                                     "label" : "I'm in a bundle",
                                     "style" : {
                                       "background": "blue",
                                       "color": "#FFFFFF",
				       "borderRadius": "10px"
                                     }
                                  }
   	      } 
	     ]
  }
  ,
  {
   "label" : "row label03", 
   "bars" : [
              { 
               "beginDate"      : "2021/06/24 13:00", 
	       "endDate"        : "2021/06/29 19:00", 
	       "ganttBarConfig" : {
	                             "id"    : "1592311883",
                                     "label" : "I'm in a bundle",
				     "hasHandles": "true" ,
                                     "style" : {
                                       "background": "magenta"
                                     }
                                  }
   	      } 
	     ]
  }
]`;


export const objData = JSON.parse(jsonData);

//export default { objData };




