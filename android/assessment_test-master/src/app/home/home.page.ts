import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})
export class HomePage implements OnInit {

  // Array handling different available tabs
  items = [
    {
      text: 'Classify an image',
      bgColor: '#732CA4',
      boxShadow: '0px 0px 8px rgba(115, 44, 164, 0.8)',
      rout: 'image-classifier'
    }
   ];

  constructor(
    private router: Router
  ) { }


  ngOnInit(): void {
  }
  // Navigation handler
  screenTo(rout) {
    this.router.navigate([rout]);
  }

}
