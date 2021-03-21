import axios from 'axios';

class CalculationsService {

    retrieveAllCalculations(){
        return axios.get('http://127.0.0.1:5000/api/calculations/all');
    }

    retrieveMercuryCalculations(){
        return axios.get('http://127.0.0.1:5000/api/calculations/mercury');
    }

}
export default new CalculationsService();