'use client'
import React from 'react'
import { usePathname } from 'next/navigation'
import Link from 'next/link'
import styles from '../styles/Login.module.css'

function Login() {
  const pathname = usePathname()
  const [login, setLogin] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [error, setError] = React.useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    // здесь можно добавить логику аутентификации
    if (login && password) {
      if (password.length >= 8) {
        // здесь не нужно вызывать navigate
      } else {
        setError('Пароль должен быть не менее 8 символов')
      }
    } else {
      setError('Пожалуйста, заполните все поля')
    }
  }

  return (
    <div className={styles.container}>
      <form className={styles.form} onSubmit={handleSubmit}>
        <div className={styles.inputGroup}>
          <input
            type="text"
            name="login"
            value={login}
            onChange={(e) => setLogin(e.target.value)}
            placeholder="Логин"
            className={styles.input}
          />
          <img src="/user.svg" alt="user icon" className={styles.icon} />
        </div>
        <div className={styles.inputGroup}>
          <input
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Пароль"
            className={styles.input}
          />
          <img src="/lock.svg" alt="lock icon" className={styles.icon} />
        </div>
        {error && <p className={styles.error}>{error}</p>}
        {/* здесь мы используем Link */}
        <Link href="/home">
          <button type="submit" className={styles.button}>
            Войти
          </button>
        </Link>
        
        <p className={styles.register}>Зарегистрироваться</p>
      </form>
    </div>
  )
}

export default Login
