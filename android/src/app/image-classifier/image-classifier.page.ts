import { ServerService } from './../server.service';
import { NgxUiLoaderService } from 'ngx-ui-loader';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Camera, CameraOptions } from '@ionic-native/camera/ngx';

@Component({
  selector: 'app-image-classifier',
  templateUrl: './image-classifier.page.html',
  styleUrls: ['./image-classifier.page.scss'],
})
export class ImageClassifierPage implements OnInit {

  responseText: string; image: string; loading = false;

  constructor(
    private router: Router,
    private babyLoader: NgxUiLoaderService,
    private camera: Camera,
    private server: ServerService,
    ) { }

  ngOnInit() {
    this.snapShot();
  }

  // Rout to home
  home() {
    this.router.navigate(['']);
  }
  // Rout to back
  back() {
    this.home();
  }

  snapShot() {
    const options: CameraOptions = {
      quality: 100,
      destinationType: this.camera.DestinationType.DATA_URL,
      encodingType: this.camera.EncodingType.JPEG,
      mediaType: this.camera.MediaType.PICTURE
    };
    this.camera.getPicture(options).then((imageData: any) => {
      this.image = 'data:image/jpeg;base64,'+imageData;
      this.loading = true;
      // Send image to service to send to AI
      this.server.sendImageForAnalysis(this.image).subscribe((dat: any)=>{
        this.loading = false;
        this.responseText = dat;
        // Handle Error
      }, err => { this.loading = false; this.responseText = err.error.text;});
    }, (err) => {
      // Handle error
      });
  }

}
