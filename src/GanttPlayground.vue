<template>
  <g-gantt-chart
    v-bind:chart-start="chartStart"
    v-bind:chart-end="chartEnd"
    precision="day"
    :row-height="40"
    grid
    width="100%"
    bar-start="beginDate"
    bar-end="endDate"
    :date-format="format"
    @click-bar="onClickBar($event.bar, $event.e, $event.datetime)"
    @mousedown-bar="onMousedownBar($event.bar, $event.e, $event.datetime)"
    @dblclick-bar="onMouseupBar($event.bar, $event.e, $event.datetime)"
    @mouseenter-bar="onMouseenterBar($event.bar, $event.e)"
    @mouseleave-bar="onMouseleaveBar($event.bar, $event.e)"
    @dragstart-bar="onDragstartBar($event.bar, $event.e)"
    @drag-bar="onDragBar($event.bar, $event.e)"
    @dragend-bar="onDragendBar($event.bar, $event.e, $event.movedBars)"
    @contextmenu-bar="onContextmenuBar($event.bar, $event.e, $event.datetime)"
  >
    <g-gantt-row
      label="My row 1"
      :bars="bars1"
      highlight-on-hover
    />
    <g-gantt-row
      label="My row 2"
      highlight-on-hover
      :bars="bars2"
    />
  </g-gantt-chart>

  <button @click="addBar()">
    Add bar
  </button>
  <button @click="deleteBar()">
    Delete bar
  </button>

  <button @click="shiftLeft()">
   ←  
  </button>
  <button @click="shiftRight()">
   →
  </button>

</template>

<script setup lang="ts">
import { ref } from "vue"
import GGanttRow from "./components/GGanttRow.vue"
import GGanttChart from "./components/GGanttChart.vue"
import { GanttBarObject } from "./models/models"
import dayjs from 'dayjs';

//const format = ref("DD.MM.YYYY HH:mm")
//const chartStart = ref("01.01.2021 12:00")
//const chartEnd = ref("15.07.2021 12:00")
const format = ref("YYYY/MM/DD HH:mm")
//const chartStart = ref("2021/01/01 12:00")
const chartStart = ref("2021/06/10 12:00")  //error duplicate
//const chartStart = ref("2021/07/01 12:00") // ok
const chartEnd   = ref("2021/07/15 12:00")
//let chartStart = ref("2021/05/31 12:00")
//let  chartEnd   = ref("2021/07/14 12:00")


 //const element = document.getElementById("circle");
 let element = ""

  let currentAnimation;

  function move(transformStart, transformEnd) {
    currentAnimation = element.animate(
      [{ transform: transformStart }, { transform: transformEnd }],
      {
        duration: 1000,
        easing: "linear",
        fill: "forwards",
      }
    );
  }

const bars1 = ref([
  {
    //beginDate: "24.04.2021 13:00",
    //endDate: "25.05.2021 19:00",
    beginDate: "2021/04/24 13:00",
    endDate: "2021/05/25 19:00",
    ganttBarConfig: {
      id: "8621987329",
      label: "I'm in a bundle",
      bundle: "bundle2"
    }
  }
])

const bars2 = ref([
  {
    //beginDate: "24.04.2021 13:00",
    //endDate: "25.05.2021 19:00",
    beginDate: "2021/04/24 13:00",
    endDate: "2021/05/25 19:00",
    ganttBarConfig: {
      id: "1592311887",
      label: "I'm in a bundle",
      bundle: "bundle2",
      style: {
        background: "magenta"
      }
    }
  },
  {
    //beginDate: "01.01.2021 00:00",
    //endDate: "01.03.2021 00:00",
    beginDate: "2021/01/01 00:00",
    endDate: "2021/04/01 00:00",
    ganttBarConfig: {
      id: "7716981641",
      label: "Lorem ipsum dolor",
      hasHandles: true,
      style: {
        background: "#b74b52"
      }
    }
  },
  {
    //beginDate: "15.06.2021 00:00",
    //endDate: "10.07.2021 00:00",
    beginDate: "2021/06/15 00:00",
    endDate: "2021/07/10 00:00",
    ganttBarConfig: {
      id: "9716981641",
      label: "Oh hey",
      style: {
        background: "#69e064",
        borderRadius: "15px",
        color: "blue",
        fontSize: "10px"
      }
    }
  }
])

const shiftLeft = () => {
  console.log("shiftLeft")
 //chartStart = ref("2021/05/31 12:00")
 //chartEnd   = ref("2021/07/14 12:00")
 //chartStart.value = "2021/05/31 12:00"
 //chartEnd.value   = "2021/07/14 12:00"
element = document.querySelector("#g-gantt-chart");

 const start = dayjs(chartStart.value ).subtract(1,"d")
 const end   = dayjs(chartEnd.value ).subtract(1,"d")
 chartStart.value = dayjs(start).format('YYYY/MM/DD HH:mm')
 chartEnd.value   = dayjs(end).format('YYYY/MM/DD HH:mm')
 console.log(chartStart.value)
 console.log(chartEnd.value)
 // move("translateX(100px)", "translateX(0)");

 
}

const shiftRight = () => {
element = document.querySelector("#g-gantt-chart");
 //move("translateX(0)", "translateX(100px)");
  console.log("shiftRight")
 //chartStart = ref("2021/06/02 12:00")
 //chartEnd   = ref("2021/07/16 12:00")
 const start = dayjs(chartStart.value ).add(1,"d")
 const end   = dayjs(chartEnd.value ).add(1,"d")
 chartStart.value = dayjs(start).format('YYYY/MM/DD HH:mm')
 chartEnd.value   = dayjs(end).format('YYYY/MM/DD HH:mm')
 console.log(chartStart.value)
 console.log(chartEnd.value)
 //move("translateX(0)", "translateX(100px)");

}

const addBar = () => {
  if (bars1.value.some(bar => bar.ganttBarConfig.id === "test1")) {
    return
  }
  const bar = {
    //beginDate: "26.02.2021 00:00",
    //endDate: "26.03.2021 02:00",
    beginDate: "2021/06/30 00:00",
    endDate: "2021/07/10 02:00",
    ganttBarConfig: {
      id: "test1",
      hasHandles: true,
      label: "Hello!",
      style: {
        background: "#5484b7",
        borderRadius: "20px"
      }
    }
  }
  bars1.value.push(bar)
}

const deleteBar = () => {
  const idx = bars1.value.findIndex(b => b.ganttBarConfig.id === "test1")
  if (idx !== -1) {
    bars1.value.splice(idx, 1)
  }
}

const onClickBar = (bar: GanttBarObject, e:MouseEvent, datetime?: string) => {
  console.log("click-bar", bar, e, datetime)
}

const onMousedownBar = (bar: GanttBarObject, e:MouseEvent, datetime?: string) => {
  console.log("mousedown-bar", bar, e, datetime)
}

const onMouseupBar = (bar: GanttBarObject, e:MouseEvent, datetime?: string) => {
  console.log("mouseup-bar", bar, e, datetime)
}

const onMouseenterBar = (bar: GanttBarObject, e:MouseEvent) => {
  console.log("mouseenter-bar", bar, e)
}

const onMouseleaveBar = (bar: GanttBarObject, e:MouseEvent) => {
  console.log("mouseleave-bar", bar, e)
}

const onDragstartBar = (bar: GanttBarObject, e:MouseEvent) => {
  console.log("dragstart-bar", bar, e)
}

const onDragBar = (bar: GanttBarObject, e:MouseEvent) => {
  console.log("drag-bar", bar, e)
}

const onDragendBar = (bar: GanttBarObject, e:MouseEvent, movedBars?: Map<GanttBarObject, {oldStart: string, oldEnd: string}>) => {
  console.log("dragend-bar", bar, e, movedBars)
}

const onContextmenuBar = (bar: GanttBarObject, e:MouseEvent, datetime?: string) => {
  console.log("contextmenu-bar", bar, e, datetime)
}
</script>
