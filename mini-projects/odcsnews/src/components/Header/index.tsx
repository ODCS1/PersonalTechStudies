import React from 'react'
import styles from './styles.module.scss';
import { SignInButton } from '../SignInButton';

export const Header = () => {
  return (
    <header className={styles.headerContainer}>
        <div className={styles.headerContent}>
            <img src="/images/logo.png" alt="odcs.news" />
            <nav>
                <a className={styles.active} href="#">Home</a>
                <a className={styles.active} href="#">Posts</a>
            </nav>

            <SignInButton />
        </div>
    </header>
  );
}
