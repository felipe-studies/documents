// refazer codigo do jogo do nim que fiz errado em C
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int numero_jogada;
int pecas_limite;
int pecas_limite_jogada;

int usuario_escolhe_jogada() {
    printf("\nVocê começa!\n\n");

    while (pecas_limite >= pecas_limite_jogada && true) {
        int pecas_atuais;
        printf("Quantas peças você vai tirar? ");
        scanf("%d", &pecas_atuais);
        if (pecas_atuais > pecas_limite_jogada || pecas_atuais == 0) {
            printf("Oops! Jogada inválida! Tente de novo.\n");
            usuario_escolhe_jogada();
        }
        if (pecas_atuais == 1) {
            printf("Você tirou uma peça.\n");
        } else if (pecas_atuais > 1) {
            printf("Você tirou %d peças.\n", pecas_atuais);
        }
        pecas_limite = pecas_limite - pecas_atuais;
        if (pecas_limite_jogada >= pecas_atuais) {
            break;
        }
    }
    if (pecas_limite == 0) {
        printf("Fim do jogo! Voce ganhou!\n");
        return 2;
    } else {
        if (pecas_limite > 1) {
            printf("Agora restam %d peças no tabuleiro.\n", pecas_limite);
        } else {
            printf("Agora resta apenas uma peça no tabuleiro\n");
        }
        return 0;
    }
}

int computador_escolhe_jogada() {
    printf("\nComputador começa!\n\n");
    int pecas_atuais = pecas_limite % (pecas_limite_jogada + 1);
    if (pecas_atuais > 1) {
        printf("O computador tirou %d peças.\n", pecas_atuais);
    } else if (pecas_atuais == 1) {
        printf("O computador tirou uma peça.\n");
    } else {
        printf("O computador passou a vez.\n");
    }
    pecas_limite = pecas_limite - pecas_atuais;
    if (pecas_limite == 0) {
        printf("Fim do jogo! O computador ganhou!\n");
        return 1;
    } else {
        if (pecas_limite > 1) {
            printf("Agora restam %d peças no tabuleiro.\n", pecas_limite);
        } else {
            printf("Agora resta apenas uma peça no tabuleiro.\n");
        }
        return 0;
    }
}

bool partida(int numero_partida) {
    bool jogo_ganho;
    int resultado_jogo = 0;

    // int pecas_limite, pecas_limite_jogada;

    if (numero_partida == 0) {
        printf("\n**** Rodada Única ****\n\n");
    } else {
        printf("\n**** Rodada %d ****\n\n", numero_partida);
    }
        
    printf("Quantas peças? ");
    scanf("%d", &pecas_limite);
    printf("Limite de peças por jogada? ");
    scanf("%d", &pecas_limite_jogada);

    if ((pecas_limite_jogada + 1) % pecas_limite == 0) {
        resultado_jogo = usuario_escolhe_jogada();
        numero_jogada = 0;
    } else {
        resultado_jogo = computador_escolhe_jogada();
        numero_jogada = 1;
    }

    while (resultado_jogo == 0) {
        numero_jogada++;
        /*
            nao acabou = 0
            acabou pc ganhou = 1
            acabou usuario ganhou = 2
        */
        if (numero_jogada % 2 == 0) {
            resultado_jogo = usuario_escolhe_jogada();
        } else {
            resultado_jogo = computador_escolhe_jogada();
        }
    }
    if (resultado_jogo == 1) {
        jogo_ganho = false;
    } else {
        jogo_ganho = true;
    }
    
    return jogo_ganho;
}

void campeonato() {
    int pontos_usuario = 0;
    int pontos_computador = 0;
    bool jogo_atual;

    for (int i = 1; i < 4; i++) {
        jogo_atual = partida(i);
        if (jogo_atual) {
            pontos_usuario++;
        } else {
            pontos_computador++;
        }
    }
    printf("\n**** Final do campeonato! ****\n\n");
    printf("Placar: Você %d X Computador %d\n", pontos_usuario, pontos_computador);
}

int main() {
    int tipo_jogo;
    int pontos_usuario = 0;
    int pontos_computador = 0;

    printf("Bem-vindo ao jogo do NIM! Escolha:\n");
    printf("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n> ");
    scanf("%d", &tipo_jogo);

    switch (tipo_jogo) {
        case 1:
            printf("\nVoce escolheu uma partida!\n");
            partida(0);
            break;
        case 2:
            printf("\nVoce escolheu um campeonato!\n");
            campeonato();
            break;
        default:
            printf("\nOpção inválida!\nFechando jogo...\n");
            break;
    }
    return 0;
}
