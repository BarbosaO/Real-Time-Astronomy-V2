import axios from 'axios';

class CalculationsService {

    retrieveAllCalculations(){
        return axios.get('http://127.0.0.1:5000/api/calculations/all');
    }

    retrieveMiDistances(){
        return axios.get('http://127.0.0.1:5000/api/calculations/distances/mi');
    }

    retrieveKmDistances(){
        return axios.get('http://127.0.0.1:5000/api/calculations/distances/km');
    }
    
    retrieveAuDistances(){
        return axios.get('http://127.0.0.1:5000/api/calculations/distances/au');
    }

}
export default new CalculationsService();