# Comandos WSL

## Instalação e Configuração
wsl --install: Instala o WSL e baixa a versão padrão do Ubuntu.
wsl --update: Atualiza o WSL para a versão mais recente.
wsl --status: Mostra o status atual, versão do kernel e distribuição padrão.

## Gerenciamento de Distribuições
wsl: Abre a distribuição padrão do Linux.
wsl -d <nome>: Abre uma distribuição específica informando o nome.
wsl --list --verbose ou wsl -l -v: Lista todas as distros instaladas e seus estados.
wsl --list --online: Mostra as opções de distros que podem ser instaladas.
wsl --set-default <nome>: Define uma distro como padrão.

## Controle e Manutenção
wsl --shutdown: Fecha e desliga todas as instâncias ativas do WSL.
wsl --terminate <nome>: Encerra uma distribuição específica.
wsl --export <nome> <arquivo.tar>: Cria um backup da distro.
wsl --import <nome> <pasta> <arquivo.tar>: Restaura um backup da distro.
wsl --unregister <nome>: Remove e desinstala uma distribuição do Linux.