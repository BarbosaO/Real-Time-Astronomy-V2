import axios from 'axios';

class CalculationsService {

    retrieveAllCalculations(){
        return axios.get('http://127.0.0.1:5000/api/calculations/all');
    }

    retrieveHelioData(){
        return axios.get('http://127.0.0.1:5000/api/calculations/heliocentric')
    }

    retrieveGeoData(){
        return axios.get('http://127.0.0.1:5000/api/calculations/geocentric')
    }

    retrieveMiDistances(distance_type){

        if(distance_type === 'helio'){
            return axios.get('http://127.0.0.1:5000/api/calculations/heliocentric/distances/mi');
        }
        
        return axios.get('http://127.0.0.1:5000/api/calculations/geocentric/distances/mi');
    }

    retrieveKmDistances(distance_type){

        if(distance_type === 'helio'){
            return axios.get('http://127.0.0.1:5000/api/calculations/heliocentric/distances/km');
        }
        
        return axios.get('http://127.0.0.1:5000/api/calculations/geocentric/distances/km');
    }
    
    retrieveAuDistances(distance_type){

        if(distance_type === 'helio'){
            return axios.get('http://127.0.0.1:5000/api/calculations/heliocentric/distances/au');
        }
        
        return axios.get('http://127.0.0.1:5000/api/calculations/geocentric/distances/au');
    }

}
export default new CalculationsService();