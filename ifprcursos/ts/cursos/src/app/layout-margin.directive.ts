import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive( {
    selector: '[layout-margin]'
} )
export class LayoutMarginDirective
{

    constructor( private el: ElementRef, private renderer: Renderer2 )
    {
        this.renderer.addClass(el.nativeElement, "layout-margin");
    }

}
