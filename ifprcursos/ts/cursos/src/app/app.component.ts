import { CursoDialogComponent } from './curso-dialog/curso-dialog.component';
import { Component, OnInit, ElementRef } from '@angular/core';
import { Http } from '@angular/http';
import { MatSnackBar, MatDialog } from '@angular/material';

@Component( {
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
} )
export class AppComponent implements OnInit
{
    /**
     * 
     */
    private alternativas: Array<any>;

    /**
     * 
     */
    private perguntas: Array<any>;

    /**
     * 
     */
    private showButton: boolean;

    /**
     * 
     * @param http 
     */
    constructor(
        private http: Http,
        private snackbar: MatSnackBar,
        private matDialog: MatDialog
    ){}

    /**
     * 
     */
    ngOnInit()
    {
        this.http.get("alternativas").toPromise()
        .then( ( result ) => {
            this.alternativas = result.json();

            this.listPerguntas();
        })
        .catch( ( exception ) => {
            console.error(exception);
        });
    }

    /**
     * 
     */
    listPerguntas(): void
    {
        this.http.get("perguntas").toPromise()
        .then( ( result ) => {
            this.perguntas = result.json();

            this.perguntas.forEach(pergunta => {
                pergunta.alternativas = this.alternativas.filter( (alternativaToFind) => {
                    return alternativaToFind.pergunta == pergunta.id;
                })
            });
        })
        .catch( ( exception ) => {
            console.error(exception);
        });
    }

    /**
     * 
     */
    salvarResposta(): void
    {
        let respostas = [];
      
        for(let i = 0; i < this.perguntas.length; i++)
        {
            if(this.perguntas[i].resposta == null)
            {
                this.snackbar.open("Todas as perguntas são obrigatórias", null, {duration: 2000});
                return;
            }

            respostas.push(this.perguntas[i].resposta);
        }

        this.http.post("cursos/predict/", respostas).toPromise()
        .then( ( result ) => {
            this.matDialog.open(CursoDialogComponent, {
                data: {
                    curso: result.json()
                },
                disableClose: true
            })
            .afterClosed().subscribe(( result ) => {
                for(let i = 0; i < this.perguntas.length; i++)
                {
                    this.perguntas[i].resposta = null;
                }

                document.body.scrollTop = 0;
            });
        })
        .catch( ( exception ) => {
            console.error(exception);
        });
    }

    scrollTop(): void
    {
        document.body.scrollTop = 0;
    }

    showTopButton(): void
    {
        window.onscroll = ($event) => {
            if(document.body.scrollTop > 400)
            {
                this.showButton = true;
            }
            else
            {
                this.showButton = false;
            }
        }

    }
}
