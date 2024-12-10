import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonCol,
  IonGrid,
  IonRow,
  IonButton,
  IonIcon,
  IonList,
  IonSelect,
  IonSelectOption,
} from '@ionic/react';
import { searchSharp } from 'ionicons/icons';

const Search: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <div style={{ display: 'flex', alignItems: 'center', marginLeft: '20px' }}>
            <IonIcon icon={searchSharp} style={{ fontSize: '24px', marginRight: '8px' }} />
            <IonTitle>Search</IonTitle>
          </div>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonGrid>
          {/* Linha 1 */}
          <IonRow>
            <IonCol size="12" sizeMd="6" sizeLg="4">
              <IonSelect label='Select Database' labelPlacement='floating'>
                <IonSelectOption value='sigfox'>SigFox</IonSelectOption>
                <IonSelectOption value='lora-ble'>LoRa-BLE</IonSelectOption>
                <IonSelectOption value='nb-iot'>NB-IoT</IonSelectOption>
              </IonSelect>
            </IonCol>
            <IonCol size="12" sizeMd="6" sizeLg="4">
              <IonButton expand="block" color="secondary">Button 2</IonButton>
            </IonCol>
            <IonCol size="12" sizeMd="6" sizeLg="4">
              <IonButton expand="block" color="tertiary">Button 3</IonButton>
            </IonCol>
          </IonRow>

          {/* Linha 2 */}
          <IonRow>
            <IonCol size="12">
              <div style={{ textAlign: 'center', padding: '20px' }}>
                <IonTitle>Footer Section</IonTitle>
              </div>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Search;
