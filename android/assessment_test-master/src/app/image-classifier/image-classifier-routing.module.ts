import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ImageClassifierPage } from './image-classifier.page';

const routes: Routes = [
  {
    path: '',
    component: ImageClassifierPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ImageClassifierPageRoutingModule {}
