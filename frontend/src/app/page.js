import styles from './page.module.css';
import NewDashboard from './components/newdashboard';

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <NewDashboard />
      </div>
    </main>
  )
}
