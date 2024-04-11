export const authRoutes = [
  {
    path: 'signup',
    name: 'signup',
    component: () => import('../views/auths/SignupView.vue')
  },
  {
    path: 'login',
    name: 'login',
    component: () => import('../views/auths/LoginView.vue')
  }
]
