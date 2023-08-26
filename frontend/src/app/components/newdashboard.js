import styles from './components.module.css';
import Button from '@mui/material/Button';

export default function NewDashboard() {
  return (
    <div className={styles.components}>
      <Button variant="contained">Add a Chart</Button>
    </div>
  )
}
