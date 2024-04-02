package praticando.p016;

public class Ex14 {
    public interface Movable {
        void moveUp();
        void moveDown();
        void moveLeft();
        void moveRight();
    }

    public class MovablePoint implements Movable {
        private int x;
        private int y;
        private int speed;
    
        public MovablePoint(int x, int y, int speed) {
            this.x = x;
            this.y = y;
            this.speed = speed;
        }
    
        public void moveUp() {
            this.y -= this.speed;
        }
    
        public void moveDown() {
            this.y += this.speed;
        }
    
        public void moveLeft() {
            this.x -= this.speed;
        }
    
        public void moveRight() {
            this.x += this.speed;
        }

        public String toString(){
            return "";
        }
    }

    public class MovableRectangle implements Movable {
        private MovablePoint topLeft;
        private MovablePoint bottomRight;
    
        public MovableRectangle(int x1, int y1, int x2, int y2, int speed) {
            topLeft = new MovablePoint(x1, y1, speed);
            bottomRight = new MovablePoint(x2, y2, speed);
        }
    
        @Override
        public void moveUp() {
            topLeft.moveUp();
            bottomRight.moveUp();
        }
    
        @Override
        public void moveDown() {
            topLeft.moveDown();
            bottomRight.moveDown();
        }
    
        @Override
        public void moveLeft() {
            topLeft.moveLeft();
            bottomRight.moveLeft();
        }
    
        @Override
        public void moveRight() {
            topLeft.moveRight();
            bottomRight.moveRight();
        }
    }
    
}
