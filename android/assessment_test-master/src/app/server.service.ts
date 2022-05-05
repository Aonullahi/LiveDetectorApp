import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServerService {

  constructor(private http: HttpClient) { }

  sendImageForAnalysis(data) {
    return this.http.post('https://livedetector.herokuapp.com/predict', {data});
  }

}
