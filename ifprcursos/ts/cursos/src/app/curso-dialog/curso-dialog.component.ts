import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material';

@Component( {
    selector: 'app-curso-dialog',
    templateUrl: './curso-dialog.component.html',
    styleUrls: ['./curso-dialog.component.css']
} )
export class CursoDialogComponent implements OnInit
{
    private curso: any;

    constructor(
        @Inject(MAT_DIALOG_DATA) private data: {
            curso: any
        },
        private dialogRef: MatDialogRef<CursoDialogComponent>
    ) { }

    ngOnInit()
    {
        this.curso = this.data.curso;
    }

}
