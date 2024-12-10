import './home.css';

interface ContainerProps {
}

const Home: React.FC<ContainerProps> = () => {
  return (
    <div id="container">
      <strong>Home</strong>
      <p>Explore <a target="_blank" rel="noopener noreferrer" href="https://ionicframework.com/docs/components">UI Components</a></p>
    </div>
  );
};

export default Home;
