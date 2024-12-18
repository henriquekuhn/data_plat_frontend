import {
  IonContent,
  IonIcon,
  IonItem,
  IonLabel,
  IonList,
  IonListHeader,
  IonMenu,
  IonMenuToggle,
  IonNote,
} from '@ionic/react';

import { useLocation } from 'react-router-dom';
import { analyticsSharp, helpSharp, homeSharp, layersSharp, searchSharp } from 'ionicons/icons';
import './menu.css';

interface AppPage {
  url: string;
  icon: string;
  title: string;
}

const appPages: AppPage[] = [
  {
    title: 'Home',
    url: '/home',
    icon: homeSharp,  // Ícone correto para 'Home'
  },
  {
    title: 'Database',
    url: '/database',
    icon: layersSharp,  // Ícone correto para 'Database'
  },
  {
    title: 'Search',
    url: '/search',
    icon: searchSharp,  // Ícone correto para 'Search'
  },
  {
    title: 'Analysis',
    url: '/analysis',
    icon: analyticsSharp,  // Ícone correto para 'Analysis'
  },
  {
    title: 'Help',
    url: '/help',
    icon: helpSharp,  // Ícone correto para 'Help'
  }
];

const Menu: React.FC = () => {
  const location = useLocation();

  return (
    <IonMenu contentId="main" type="overlay" className='custom-menu'>
      <IonContent>
        <IonList id="inbox-list">
        <IonListHeader className="header">
          <div className='header-content'>
            <div className="ht-micron">HT MICRON</div>
            <div className="semiconductors">SEMICONDUCTORS</div>
          </div>
        </IonListHeader>

          <IonNote className='welcome'>hi, Admin.</IonNote>
          {appPages.map((appPage, index) => (
            <IonMenuToggle key={index} autoHide={false}>
              <IonItem
                className={location.pathname === appPage.url ? 'selected' : ''}
                routerLink={appPage.url}
                routerDirection="none"
                lines="none"
                detail={false}
              >
                <IonIcon
                  aria-hidden="true"
                  slot="start"
                  icon={appPage.icon}
                />
                <IonLabel>{appPage.title}</IonLabel>
              </IonItem>
            </IonMenuToggle>
          ))}
        </IonList>
      </IonContent>
    </IonMenu>
  );
};

export default Menu;
