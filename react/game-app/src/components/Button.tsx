interface buttonProps {
    onClick: () => void;
    label: string;
    className: string;
}

const Button = ({ onClick, label, className }: buttonProps) => {
  return (
    <button type="button"
            onClick={onClick} 
            className={className}>
        {label}
    </button>
  )
}

export default Button