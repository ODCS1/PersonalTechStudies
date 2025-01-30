import style from './style.module.scss';
import { FaGithub } from 'react-icons/fa';
import { FiX } from 'react-icons/fi';

export const SignInButton = () => {
  const isUserLoggedIn = true;

  return isUserLoggedIn ? (
    <button type="button" className={style.signInButton}>
      <FaGithub color='#04d361'/>
      UserName
      <FiX color='#737380' className={style.closeIcon}/>
    </button>
  ) : (
    <button type="button" className={style.signInButton}>
      <FaGithub color='#eba417'/>
      Sign in with GitHub
    </button>
  );
}
