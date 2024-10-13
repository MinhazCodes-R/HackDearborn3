import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div>
    
    
    <div style={{width: '100vw', display: 'flex', justifyContent: 'center'}}>
        
        <div style={{width: '800px', height: '150vh', backgroundColor: 'rgb(118, 246, 161)',padding:' 50px', position: 'relative'}}>
            <h1>HACK DEARBORN</h1>
            
            <div class="divforinputs" style={{display: 'flex', flexDirection: 'column', position: 'relative', width: '500px'}}>
                
                <div class="inputdivs" style={{display: 'flex', alignItems: 'center'}}><p>Start of Trip:</p><input type="date" class="inputs01"/></div>
                <div class="inputdivs" style={{display: 'flex', alignItems: 'center'}}><p>End of Trip:</p><input type="date" class="inputs01"/></div>
                <div class="inputdivs" style={{display: 'flex', alignItems: 'center'}}><p>Price:</p><input type="text" class="inputs01"/></div>
                <div class="inputdivs" style={{display: 'flex', alignItems: 'center'}}><p>Location:</p><input name="search_input" type="text" placeholder="Search location" class="KB W Z pac-target-input locationin" autocomplete="off"/></div>
                
            </div>

            <div style={{height: '30px'}}></div>
            <button style={{width: '600px',height: '100px'}}> BUTTON</button>




        </div>



    </div>
    

  </div>
  );
}

export default App;
