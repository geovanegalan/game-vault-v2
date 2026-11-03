import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  template: `
    <a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
    <main id="conteudo" tabindex="-1">
      <h1>GameVault 2.0</h1>
      <p>Biblioteca de jogos em construção.</p>
    </main>
    <router-outlet />
  `,
})
export class App {}
