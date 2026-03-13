def highlight(locator):
    """Highlight the element located by the given locator."""
    locator.evaluate(
        """el => {
            // Salva o estilo original para possível restauração posterior
            const originalStyle = {
                border: el.style.border,
                backgroundColor: el.style.backgroundColor,
                color: el.style.color,
                textShadow: el.style.textShadow,
                padding: el.style.padding,
                margin: el.style.margin
            };
            
            // Armazena os estilos originais como atributo de dados
            el.setAttribute('data-original-style', JSON.stringify(originalStyle));
            
            // Aplica o novo estilo de destaque
            el.style.border = '3px solid red';
            el.style.backgroundColor = 'yellow';
            el.style.color = 'black';  // Garante contraste com fundo amarelo
            el.style.textShadow = 'none';  // Remove qualquer sombra que possa atrapalhar
            el.style.padding = '2px';  // Adiciona um pequeno padding para melhor visibilidade
            el.style.margin = '2px';   // Adiciona uma pequena margem para destacar melhor
        }"""
    )