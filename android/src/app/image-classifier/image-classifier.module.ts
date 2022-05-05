import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ImageClassifierPageRoutingModule } from './image-classifier-routing.module';

import { ImageClassifierPage } from './image-classifier.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ImageClassifierPageRoutingModule
  ],
  declarations: [ImageClassifierPage]
})
export class ImageClassifierPageModule {}
