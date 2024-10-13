// src/components/TripForm.js
import React, { useEffect, useRef } from 'react';

const TripForm = () => {
    const searchInputRef = useRef(null);

    useEffect(() => {
        const loadScript = (url) => {
            const script = document.createElement('script');
            script.src = url;
            script.async = true;
            script.defer = true;
            document.body.appendChild(script);
        };



        const autocomplete = new window.google.maps.places.Autocomplete(searchInputRef.current, {
            // types: ['geocode'],
            // componentRestrictions: {},
        });

        autocomplete.addListener('place_changed', () => {
            const near_place = autocomplete.getPlace();
            console.log(near_place);
        });
    }, []);

    return (
        <div style={{ width: '100vw', display: 'flex', justifyContent: 'center' }}>
            <div style={{ width: '800px', height: '150vh', backgroundColor: 'rgb(118, 246, 161)', padding: '50px', position: 'relative' }}>
                <h1>HACK DEARBORN</h1>
                <div className="divforinputs" style={{ display: 'flex', flexDirection: 'column', position: 'relative', width: '500px' }}>
                    <div className="inputdivs" style={{ display: 'flex', alignItems: 'center' }}>
                        <p>Start of Trip:</p>
                        <input type="date" className="inputs01" />
                    </div>
                    <div className="inputdivs" style={{ display: 'flex', alignItems: 'center' }}>
                        <p>End of Trip:</p>
                        <input type="date" className="inputs01" />
                    </div>
                    <div className="inputdivs" style={{ display: 'flex', alignItems: 'center' }}>
                        <p>Price:</p>
                        <input type="text" className="inputs01" />
                    </div>
                    <div className="inputdivs" style={{ display: 'flex', alignItems: 'center' }}>
                        <p>Location:</p>
                        <input ref={searchInputRef} name="search_input" type="text" placeholder="Search location" className="KB W Z pac-target-input locationin" autoComplete="off" />
                    </div>
                </div>
                <div style={{ height: '30px' }}></div>
                <button style={{ width: '600px', height: '100px' }}>BUTTON</button>
            </div>
        </div>
    );
};

export default TripForm;
