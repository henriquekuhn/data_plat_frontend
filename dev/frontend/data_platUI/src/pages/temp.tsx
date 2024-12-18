import './search.css';

import React, { useState, useEffect } from 'react';
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
  IonSelect,
  IonSelectOption,
  IonList,
  IonItem,
  IonLabel
} from '@ionic/react';
import { searchSharp } from 'ionicons/icons';

const Search: React.FC = () => {
  const [selectedDatabase, setSelectedDatabase] = useState<string | undefined>(undefined);
  const [filterOptions, setFilterOptions] = useState<string[]>([]);
  const [TableColumns, setTableColumns] = useState<string[]>([]);
  const [selectedValue, setSelectedValue] = useState<any[]>([]); // Aqui o tipo pode ser ajustado conforme o formato de dados recebido
  const [selectedTable, setSelectedTable] = useState<string | undefined>(undefined);
  const [selectedColumn, setSelectedColumn] = useState<string[]>([]);
  const [handleData, setHandleData] = useState<string[]>([]);

  // Função para conectar ao banco de dados
  const handleConnectClick = async () => {
    if (!selectedDatabase) {
      console.log('Por favor, selecione um banco de dados.');
      return;
    }

    const backendUrl = `http://localhost:5000/connect/cafrunikuhn/admin/${selectedDatabase}`;

    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      if (response.ok) {
        console.log('Conexão bem-sucedida:', data.message);
        console.log('Tabelas recebidas:', data.tabelas);
        setFilterOptions(data.tabelas);
      } else {
        console.log('Erro ao conectar:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  // Função para selecionar a tabela e buscar suas colunas
  const handleSelectTable = async (event: CustomEvent) => {
    const selectedTable = event.detail.value;
    setSelectedTable(selectedTable); // Atualiza o estado da tabela selecionada
    const backendUrl = `http://localhost:5000/connect/columns/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}`;
    
    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {
        console.log('Colunas recebidas:', data.colunas);
        setTableColumns(data.colunas);
      } else {
        console.log('Erro ao buscar as colunas:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  // Função para selecionar um valor e buscar os dados correspondentes
  const handleSelectValue = async (event: CustomEvent) => {
    const selectedColumn = event.detail.value; // Valor da coluna selecionada
    setSelectedColumn(selectedColumn);
    const backendUrl = `http://localhost:5000/connect/data/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}/${selectedColumn}`;
    
    console.log('Coluna selecionada:', selectedColumn); // Verifique se a coluna está sendo corretamente passada

    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {
        console.log('Valores recebidos:', data.dados); // Verifique o nome correto do campo no backend
        setSelectedValue(data.dados); // Atualize o estado com os valores recebidos
      } else {
        console.log('Erro ao buscar os valores:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  const getDataTable = async () => {
    if (!selectedDatabase || !selectedTable || !selectedColumn || selectedValue.length === 0) {
      console.log('Por favor, selecione todos os campos necessários.');
      return;
    }

    // Supondo que o valor selecionado seja um único valor e não um array
    const selectedValueParam = selectedValue[0]; // Caso selectedValue seja um array e você queira pegar o primeiro valor

    const backendUrl = `http://localhost:5000/connect/value/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}/${selectedColumn}/${selectedValueParam}`;

    console.log('Valor selecionado:', selectedValueParam); // Verifique se o valor está correto

    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {
        console.log('Dados recebidos:', data.dados);
        setHandleData(data.dados); // Atualize o estado com os valores recebidos
      } else {
        console.log('Erro ao buscar os dados:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

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
          <IonRow className="vertical-center-row">
            <IonCol size="12" sizeMd="6" sizeLg="2.4">
              <div className="horizontal-container">
                <IonSelect
                  className="centered-select"
                  label="Select Database"
                  labelPlacement="floating"
                  value={selectedDatabase}
                  onIonChange={(e) => setSelectedDatabase(e.detail.value)}
                >
                  <IonSelectOption value="data_plat">data_plat</IonSelectOption>
                  <IonSelectOption value="other_db">other_db</IonSelectOption>
                </IonSelect>
              </div>
            </IonCol>
            <IonCol size="12" sizeMd="6" sizeLg="2.4">
              <div className="horizontal-container">
                <IonButton className="connect-button" onClick={handleConnectClick}>
                  Connect
                </IonButton>
              </div>
            </IonCol>
          </IonRow>

          <IonRow>
            <IonCol size="12" sizeMd="6" sizeLg="3">
              <div className="horizontal-container">
                <IonSelect
                  className="centered-select"
                  label="Database Tables"
                  labelPlacement="floating"
                  onIonChange={handleSelectTable}
                >
                  {filterOptions.map((option, index) => (
                    <IonSelectOption key={index} value={option}>
                      {option}
                    </IonSelectOption>
                  ))}
                </IonSelect>
              </div>
            </IonCol>

            <IonCol size="12" sizeMd="6" sizeLg="3">
              <div className="horizontal-container">
                <IonSelect
                  className="centered-select"
                  label="Select Filter"
                  labelPlacement="floating"
                  onIonChange={handleSelectValue}
                >
                  {TableColumns.map((option, index) => (
                    <IonSelectOption key={index} value={option}>
                      {option}
                    </IonSelectOption>
                  ))}
                </IonSelect>
              </div>
            </IonCol>

            <IonCol size="12" sizeMd="6" sizeLg="3">
              <div className="horizontal-container">
                <IonSelect 
                  className="centered-select" 
                  label="Select Value" 
                  labelPlacement="floating"
                    >
                  {selectedValue.map((option, index) => (
                    <IonSelectOption key={index} value={option}>
                      {option}
                    </IonSelectOption>
                  ))}
                </IonSelect>
              </div>
            </IonCol>

          </IonRow>

          <IonRow>
            <IonCol size="12">
              <div style={{ textAlign: 'center', padding: '0px' }}>
                <IonButton className="custom-button" color="tertiary" onClick={getDataTable}>
                  Send Request
                </IonButton>
              </div>
            </IonCol>
          </IonRow>

          {/* Exibir os dados recebidos como tabela */}
          <IonRow>
            <IonCol size="12">
              {handleData.length > 0 ? (
                <IonGrid>
                  {handleData.slice(0, 40).map((row, rowIndex) => ( // Limitar a 40 linhas
                    <IonRow key={rowIndex}>
                      {Object.values(row).map((cell, cellIndex) => (
                        <IonCol key={cellIndex} size="auto" className="cell">
                          {cell}
                        </IonCol>
                      ))}
                    </IonRow>
                ))}
                </IonGrid>
              ) : (
              <IonItem>
                <IonLabel>Nenhum dado disponível</IonLabel>
              </IonItem>
              )}
            </IonCol>
          </IonRow>

      </IonGrid>
    </IonContent>
  </IonPage>
  );
};

export default Search;
