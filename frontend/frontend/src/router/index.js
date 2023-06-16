import Vue from "vue";
import VueRouter from "vue-router";
import Bricks from "../components/BricksTest.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import HomePage from "../components/Homepage.vue";
import Login_2 from "../components/Login_2.vue";
import Register_2 from "../components/Register_2.vue";
import Homepage_2 from "../components/Homepage_2.vue";
import following from "../components/following.vue";
import follower from "../components/follower.vue";
import list from "../components/list.vue";
import lists from "../components/lists.vue";
import search from "../components/search.vue";
import diary from "../components/diary.vue";
import new_diary from "../components/new_diary.vue";
import edit_diary from "../components/edit_diary.vue";
import review from "../components/review.vue";
import diary_one from "../components/diary_one.vue";
import restaurant_info from "../components/restaurant_info.vue";


Vue.use(VueRouter);


const routes = [
  //測試連線
  {
    path: "/bricks",
    name: "BricksTest",
    component: Bricks,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/homepage",
    name: "Homepage",
    component: HomePage,
  },
  {
    path: "/login_2",
    name: "Login_2",
    component: Login_2,
  },
  {
    path: "/register_2",
    name: "Register_2",
    component: Register_2,
  },
  {
    path: "/homepage_2",
    name: "Homapage_2",
    component: Homepage_2,
  },
  {
    path: "/following",
    name: "following",
    component: following,
  },
  {
    path: "/follower",
    name: "follower",
    component: follower,
  },
  {
    path: "/list/:list_id",
    name: "list",
    component: list,
  },
  {
    path: "/lists",
    name: "lists",
    component: lists,
  },
  {
    path: "/search",
    name: "search",
    component: search,
  },
  {
    path: "/review",
    name: "review",
    component: review,
  },
  {
    path: "/diary",
    name: "diary",
    component: diary,
  },
  {
    path: "/new_diary",
    name: "new_diary",
    component: new_diary,
  },
  {
    path: "/edit_diary/:diary_id",
    name: "edit_diary",
    component: edit_diary,
  },
  {
    path: "/diary_one/:user_id/:diary_id",
    name: "diary_one",
    component: diary_one,
  },
  {
    path: "/restaurant_info",
    name: "restaurant_info",
    component: restaurant_info,
  },
];


const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});


export default router;

