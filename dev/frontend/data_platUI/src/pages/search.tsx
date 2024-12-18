import './search.css';
import { ReactTabulator } from 'react-tabulator';
import 'tabulator-tables/dist/css/tabulator.min.css';

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
  IonItem,
  IonLabel,
  IonText,
  IonList
} from '@ionic/react';
import { searchSharp } from 'ionicons/icons';

interface DataRow {
  [key: string]: any; // Estrutura flexível para os dados recebidos
}

const Search: React.FC = () => {
  const [selectedDatabase, setSelectedDatabase] = useState<string | undefined>(undefined);
  const [filterOptions, setFilterOptions] = useState<string[]>([]);
  const [tableColumns, setTableColumns] = useState<string[]>([]);
  const [selectedValue, setSelectedValue] = useState<string[]>([]); 
  const [selectedTable, setSelectedTable] = useState<string | undefined>(undefined);
  const [selectedColumn, setSelectedColumn] = useState<string[]>([]);
  const [handleData, setHandleData] = useState<DataRow[]>([]);
  const [numOfPass, setNumOfPass] = useState<number>(0); 
  const [numOfFail, setNumOfFail] = useState<number>(0); 
  const [totalNum, setTotalNum] = useState<number>(0); 
  const [highestResult, setHighestResult] = useState<number>(0);
  const [lowestResult, setLowestResult] = useState<number>(0);
  const [avgResult, setAvgResult] = useState<number>(0);
  const [selectedColumnData, setSelectedColumnData] = useState<string[]>([]); 

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
        setFilterOptions(data.tabelas);
      } else {
        console.log('Erro ao conectar:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  const handleSelectTable = async (event: CustomEvent) => {
    const selectedTable = event.detail.value;
    setSelectedTable(selectedTable);
    const backendUrl = `http://localhost:5000/connect/columns/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}`;
    
    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {
        setTableColumns(data.colunas);
      } else {
        console.log('Erro ao buscar as colunas:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  const handleSelectValue = async (event: CustomEvent) => {
    const selectedColumn = event.detail.value;
    setSelectedColumn(selectedColumn);
    const backendUrl = `http://localhost:5000/connect/data/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}/${selectedColumn}`;
    
    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {
        setSelectedValue(data.dados);
      } else {
        console.log('Erro ao buscar os valores:', data.error);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  const getDataTable = async () => {

    const backendUrl = `http://localhost:5000/connect/value/cafrunikuhn/admin/${selectedDatabase}/${selectedTable}/${selectedColumn}/${selectedColumnData}`;

    try {
      const response = await fetch(backendUrl, { method: 'GET' });
      const data = await response.json();
      
      if (response.ok) {

        setHandleData(data.dados);
        console.log(selectedColumnData)

        const index_judgement = data.dados[0].indexOf("judgement");
        const index_result = data.dados[0].indexOf("result");
        const index_unit = data.dados[0].indexOf("unit");

        let num_of_pass = 0;
        let highest_result = data.dados[1][index_result];
        let lowest_result = data.dados[1][index_result];

        for (let i = 0; i < Math.min(100, data.dados.length); i++) {

          if (data.dados[i+1][index_result] > highest_result) { // Checa o elemento da coluna "judgement"
            highest_result = data.dados[i+1][index_result];
          }

          if (data.dados[i+1][index_result] < lowest_result) { // Checa o elemento da coluna "judgement"
            lowest_result = data.dados[i+1][index_result];
          }

          if (data.dados[i+1][index_judgement] === 'PASS') { // Checa o elemento da coluna "judgement"
            num_of_pass += 1;
          }
        }

        const num_of_fail = 100 - num_of_pass;
        setTotalNum( 100 );
        setNumOfPass( num_of_pass );
        setNumOfFail( num_of_fail );
        setHighestResult( highest_result );
        setLowestResult( lowest_result );
        setAvgResult( 10 );

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
        <IonToolbar style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-start', height: "70px" }}>
          <div className="centered-container">
              <IonIcon icon={searchSharp} style={{ fontSize: '24px', marginRight: '0px' }} />
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

        {/* Wrapper para coluna independente */}
        <div className="independent-column-wrapper">
          <div className="independent-column">
            <p><span className="left">Total of data:</span><span className="right">{totalNum}</span></p>
            <p><span className="left">Pass/Fail:</span><span className="right">{numOfPass}/{numOfFail}</span></p>
            <p><span className="left">Highest result:</span><span className="right">{highestResult}</span></p>
            <p><span className="left">Lowest result:</span><span className="right">{lowestResult}</span></p>
            <p><span className="left">Avg result:</span><span className="right">{avgResult}</span></p>            

          </div>
        </div>
      </IonRow>

      <IonRow>
        <IonCol size="12" sizeMd="6" sizeLg="3">
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
        </IonCol>

        <IonCol size="12" sizeMd="6" sizeLg="3">
          <IonSelect
            className="centered-select"
            label="Select Filter"
            labelPlacement="floating"
            onIonChange={handleSelectValue}
          >
            {tableColumns.map((option, index) => (
              <IonSelectOption key={index} value={option}>
                {option}
              </IonSelectOption>
            ))}
          </IonSelect>
        </IonCol>
        
        <IonCol size="12" sizeMd="6" sizeLg="3">
          <IonSelect
            className="centered-select"
            label="Select Value"
            labelPlacement="floating"
            onIonChange={(e) => {
              const selectedOption = e.detail.value;
              setSelectedColumnData([selectedOption]);  // Atualizando selectedValue com o valor selecionado
            }}
          >
            {selectedValue.map((option, index) => (
              <IonSelectOption key={index} value={option}>
                {option}
              </IonSelectOption>
            ))}
          </IonSelect>
        </IonCol>
      </IonRow>

      <IonRow>
        <IonCol size="12">
          <IonButton className="custom-button" onClick={getDataTable}>
            Send Request
          </IonButton>
        </IonCol>
      </IonRow>

      <IonRow>
        <IonCol size="12">
          {handleData.length > 1 ? (
            <ReactTabulator
              data={handleData.slice(1)}
              columns={
                handleData[0]
                  ? Object.keys(handleData[0]).map((key) => ({
                      title: handleData[0][key],
                      field: key,
                    }))
                  : []
              }
              layout="fitColumns"
              options={{
                pagination: 'local',
                paginationSize: 40,
              }}
            />
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
