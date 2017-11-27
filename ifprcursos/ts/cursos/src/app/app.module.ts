import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { FlexLayoutModule } from '@angular/flex-layout';

import { AppComponent } from './app.component';

import {
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatIconModule,
    MatSnackBarModule,
    MatToolbarModule,
    MatTooltipModule,
    MatRadioModule,
} from '@angular/material';

import {
    CovalentCommonModule,
    CovalentLayoutModule
} from '@covalent/core';

import { LayoutMarginDirective } from './layout-margin.directive';
import { CursoDialogComponent } from './curso-dialog/curso-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    LayoutMarginDirective,
    CursoDialogComponent,
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    CovalentCommonModule,
    CovalentLayoutModule,
    FlexLayoutModule,
    FormsModule,
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatIconModule,
    MatRadioModule,
    MatSnackBarModule,
    MatToolbarModule,
    MatTooltipModule,
    HttpModule
  ],
  providers: [],
  entryComponents: [CursoDialogComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
