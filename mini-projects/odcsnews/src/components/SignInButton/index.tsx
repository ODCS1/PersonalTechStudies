import style from './style.module.scss';
import { FaGithub } from 'react-icons/fa';
import { FiX } from 'react-icons/fi';
import { signIn, useSession } from 'next-auth/react';

export const SignInButton = () => {
  const { data: session } = useSession();

  return session ? (
    <button type="button" className={style.signInButton}>
      <FaGithub color='#04d361'/>
      UserName
      <FiX color='#737380' className={style.closeIcon}/>
    </button>
  ) : (
    <button 
      type="button" 
      className={style.signInButton}
      onClick={() => {
        console.log('Redirecting to GitHub...');
        signIn('github');
      }}
    >
      <FaGithub color='#eba417'/>
      Sign in with GitHub
    </button>
  );
}
