import { useSession, signIn } from 'next-auth/react';
import styles from './styles.module.scss';

type SubscribeButtonProps = {
  priceId: string
}

export const SubscribeButton = ({ priceId }: SubscribeButtonProps) => {
  const { data: session } = useSession();


  function handleSubscribe() {
    if (!session) {
      signIn('github');
      return;
    }

    // CREATE CHECKOUT SESSION
    
  }

  return (
    <button
        type="button"
        className={styles.subscribeButton}
        onClick={handleSubscribe}
    >
        Subscribe now
    </button>
  );
}
