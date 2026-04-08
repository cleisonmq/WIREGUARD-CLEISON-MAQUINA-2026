# CMEasy
# Versão 0.1v
# Create By Cleison Máquina

import subprocess
import shutil
import os
import shutil

# Botao para quando o utilisador clicar em enter o programa limpre a tela 
def enter_clear ():
    input("Pressione [ ENTER ] para continuar")
    os.system("cls" if os.name == "nt" else "clear")
# Caso o utilizador nao digite nada
def entrada_invalida1 ():
    print("|---------------- Entrada inválida, você deve escolher uma opção! ---------------------------|")
    input ("Presione [ ENTER ] para continuar... ")
# Se a conversão falhar (não for um número), exibe uma mensagem de erro
def entrada_invalida2 ():
    print("|---------------- Opção inválida! Por favor, insira um número. ---------------------------|")
    enter_clear()
# Este case captura qualquer entrada que não seja uma opção válida
def entrada_invalida3 ():
    print("|---------------- Opção inválida, tente novamente ---------------------------|")
    enter_clear ()
#------------------------------------------------------------

#---> Wiregroup VPN <---
# Menus
def wireguardvpn_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                VPN WIREGUARD                                |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | É um protocolo de VPN de código aberto, moderno e extremamente   |")
    print("|          |rápido, focado em alta segurança e desempenho.                    |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Criptografia Segura.                                           |")
    print("|          | - Conexão Simples e Leve.                                        |")
    print("| Funções  | - Roteamento de Rede.                                            |")
    print("|          | - Baixa Latência e Alto Desempenho.                              |")
    print("|          | - Roaming.                                                       |")
    print("+----------+------------------------------------------------------------------+")
    print("| Site ofi-| Link: https://www.wireguard.com/                                 |")
    print("|----------+------------------------------------------------------------------|")
    print("|  Testes  |                                                                  |")
    print("|-----------------------------------------------------------------------------+")
    print("|          1. Instalar no servidor      |      2. Instalar no Cliente         |")
    print("+---------------------------------------+-------------------------------------+")
    print("|             4. Comandos               |           5. Condigurações          |")
    print("+---------------------------------------+-------------------------------------+")
    print("|             6. Teste no servidor      |          7. Teste no cliente        |")
    print("+---------------------------------------+-------------------------------------+")
    print("|              8. Desinstalar           |             9. Voltar               |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_server ():
    print("+-----------------------------------------------------------------------------+")
    print("|                   Cópie, cole e altere como bem entender                    |")
    print("+-----------------------------------------------------------------------------+")
    print("[Interface]")
    print("# Endereço IP do servidor na rede VPN (sub-rede interna)")
    print("Address = 10.10.0.1/24")
    print("# Chave privada do servidor (NUNCA partilhar)")
    print("PrivateKey = <SUA_CHAVE_PRIVADA_AQUI>")
    print("# Porta UDP onde o WireGuard vai escutar")
    print("ListenPort = 51820")
    print("\n# ================================")
    print("# CONFIGURAÇÃO DE ENCAMINHAMENTO")
    print("# ================================")
    print("# ATIVAR encaminhamento de pacotes IPv4 (necessário para acesso à internet via VPN)")
    print("PostUp = sysctl -w net.ipv4.ip_forward=1")
    print("# NAT: permite que os clientes da VPN acedam à internet através da interface do servidor")
    print("# IMPORTANTE: substituir 'enp0s3' pela interface de rede correta do servidor")
    print("PostUp = iptables -t nat -A POSTROUTING -s 10.10.0.0/24 -o enp0s3 -j MASQUERADE")
    print("# Permitir tráfego da VPN (wg0) para a interface externa")
    print("PostUp = iptables -A FORWARD -i wg0 -o enp0s3 -j ACCEPT")
    print("# Permitir tráfego de retorno (estado ESTABLISHED, RELATED)")
    print("PostUp = iptables -A FORWARD -i enp0s3 -o wg0 -m state --state ESTABLISHED,RELATED -j ACCEPT")
    print("\n# ================================")
    print("# LIMPEZA DAS REGRAS (AO DESLIGAR)")
    print("# ================================")
    print("# Remove as regras criadas acima para evitar duplicação")
    print("PostDown = iptables -t nat -D POSTROUTING -s 10.10.0.0/24 -o enp0s3 -j MASQUERADE")
    print("PostDown = iptables -D FORWARD -i wg0 -o enp0s3 -j ACCEPT")
    print("PostDown = iptables -D FORWARD -i enp0s3 -o wg0 -m state --state ESTABLISHED,RELATED -j ACCEPT")
    print("\n# ================================")
    print("# CONFIGURAÇÃO DO CLIENTE")
    print("# ================================")
    print("[Peer]")
    print("# Chave pública do cliente")
    print("PublicKey = <CHAVE_PUBLICA_CLIENTE>")
    print("# IP atribuído ao cliente dentro da VPN (apenas este IP é permitido)")
    print("AllowedIPs = 10.10.0.2/32")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_client ():
    print("+-----------------------------------------------------------------------------+")
    print("|                   Cópie, cole e altere como bem entender                    |")
    print("+-----------------------------------------------------------------------------+")
    print("[Interface]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO CLIENTE")
    print("# ================================")
    print("# Endereço IP do cliente dentro da VPN")
    print("# Este IP deve ser único na sub-rede da VPN (não repetir)")
    print("# Ex.: servidor é 10.10.0.1/24, clientes podem ser 10.10.0.2/24, 10.10.0.3/24, etc.")
    print("Address = 10.10.0.2/24")
    print("# Chave privada do cliente")
    print("# MANTER SECRETA, nunca partilhar")
    print("PrivateKey = Chave privada do cliente")
    print("DNS = 1.1.1.1")
    print("\n[Peer]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO SERVIDOR")
    print("# ================================")
    print("# Chave pública do servidor")
    print("# Vem do arquivo server_public.key")
    print("PublicKey = Chave pública do servidor")
    print("# Endereço público ou IP do servidor e porta WireGuard")
    print("# Substituir pelo IP ou domínio real do servidor")
    print("# Certificar que a porta UDP (51820) está aberta no firewall/router")
    print("Endpoint = 192.168.5.199:51820")
    print("# Define quais IPs o cliente pode acessar através da VPN")
    print("# 0.0.0.0/0 → todo o tráfego IPv4 passa pela VPN")
    print("# ::/0 → todo o tráfego IPv6 passa pela VPN")
    print("# Isso faz da VPN “full tunnel”, roteando toda a internet do cliente pelo servidor")
    print("AllowedIPs = 0.0.0.0/0, ::/0")
    print("# Mantém o túnel ativo mesmo sem tráfego")
    print("# Necessário para clientes atrás de NAT/firewall")
    print("PersistentKeepalive = 25")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_comandos_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                              C O M A N D O S                                |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Iniciar o serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Ativar o Serviço.                                                      |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar o serviço.                                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar o serviço.                                                   |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                          ARQUIVOS DE CONFIGURAÇÃO                           |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Arquivo principal.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Configurar parâmetros do kernel.                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
# Comandos
def start_wireguardvpn ():
    try:
        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def enable_wireguardvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def stop_wireguardvpn ():
    try:
        subprocess.run(["sudo", "sudo", "wg-quick", "down", "wg0"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def restart_wireguardvpn ():
    try:
        subprocess.run(["sudo", "sudo", "wg-quick", "down", "wg0"], check=True)
        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def version_wireguardvpn ():
    try:
        subprocess.run(["wg", "--version"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
# instalação
def instalacao_wireguardvpn_server():
    result = subprocess.run(["dpkg", "-l", "wireguard"], capture_output=True, text=True)
    if result.returncode == 0 and "wireguard" in result.stdout:
        print("|---------------------------- WireGuard já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "curl"], check=True)
            subprocess.run(["sudo", "apt", "install", "iptables-persistent"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            subprocess.run(["sudo", "netfilter-persistent", "save"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "ufw"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando wireGuard ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "wireguard"], check=True)      
            subprocess.run(["wg", "--version"], check=True)
            print("|---------------------------- Wireguard Instalado com sucesso ----------------------------|") 

            print("|---------------------------- Gerando chaves para o servidor ---------------------------|")
            # Gerar chave privada
            print("|---------------------------- Gerando chave privada do servidor ---------------------------|")
            priv = subprocess.run(
                ["wg", "genkey"],
                capture_output=True,
                text=True,
                check=True
            )
            chave_privada = priv.stdout.strip()
            with open("server_private.key", "w") as f:
                f.write(chave_privada)
            print(f"Chave Privada: {chave_privada}")
            # Gerar chave pública
            print("|---------------------------- Gerando chave publica do servidor ---------------------------|")
            pub = subprocess.run(
                ["wg", "pubkey"],
                input=chave_privada,
                capture_output=True,
                text=True,
                check=True
            )
            chave_publica = pub.stdout.strip()
            with open("server_public.key", "w") as f:
                f.write(chave_publica)
            print(f"Chave Pública: {chave_publica}")
            print("|---------------------------- Chaves geradas com sucesso ---------------------------|")  
            
            print("|---------------------------- Preparando o arquivo de configuração ---------------------------|") 
            wireguardvpn_config_server ()
            input ("Clique enter para continuar...")          
            subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
            subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"], check=True)
            subprocess.run(["sudo", "sysctl", "-p"], check=True)
            
            
            print("|---------------------------- Iniciando o serviço ---------------------------|") 
            subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)
            print("|---------------------------- Serviço iniciado com sucesso---------------------------|") 
            

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def instalacao_wireguardvpn_cliente():
    result = subprocess.run(["dpkg", "-l", "wireguard"], capture_output=True, text=True)
    if result.returncode == 0 and "wireguard" in result.stdout:
        print("|---------------------------- WireGuard já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            subprocess.run(["sudo", "apt", "install", "curl"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando wireGuard ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "wireguard"], check=True)      
            subprocess.run(["wg", "--version"], check=True)
            print("|---------------------------- Wireguard Instalado com sucesso ----------------------------|")
            
            print("|---------------------------- Gerando chaves para o Cliente ---------------------------|")
            # Gerar chave privada
            print("|---------------------------- Gerando chave privada do servidor ---------------------------|")
            priv = subprocess.run(
                ["wg", "genkey"],
                capture_output=True,
                text=True,
                check=True
            )
            chave_privada = priv.stdout.strip()
            with open("client_private.key", "w") as f:
                f.write(chave_privada)
            print(f"Chave Privada: {chave_privada}")
            # Gerar chave pública
            print("|---------------------------- Gerando chave publica do servidor ---------------------------|")
            pub = subprocess.run(
                ["wg", "pubkey"],
                input=chave_privada,
                capture_output=True,
                text=True,
                check=True
            )
            chave_publica = pub.stdout.strip()
            with open("client_public.key", "w") as f:
                f.write(chave_publica)
            print(f"Chave Pública: {chave_publica}")
            print("|---------------------------- Chaves geradas com sucesso ---------------------------|") 
            
            print("|---------------------------- Preparando o arquivo de configuração ---------------------------|") 
            wireguardvpn_config_client ()
            input ("Clique enter para continuar...")          
            subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
            
            
            
            print("|---------------------------- Iniciando o serviço ---------------------------|") 
            subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)             
                        

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def desintslacao_wireguardvpn ():
    try:
        print("|---------------------------- Desinstalamndo o WiregroupVpn  ------------------------------|")
        subprocess.run(["sudo", "apt", "remove", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        print("|------------------------ Desinstalação bem sucedida --------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
# programas
def wireguardvpn_test_server ():
    try:
        print("|-------------------- Testando a conexão WireGuard --------------------|")
        print("Verificando se há troca de pacotes entre o peer do cliente e o servidor...")
        # Mostra o status atual do WireGuard
        subprocess.run(["sudo", "wg"], check=True)
        print("\nVerifique se o servidor tem conexão com o cliente.")
        # Solicita o IP do cliente
        ip = input("Indique o IP do Cliente: ")
        print(f"Testando conectividade com {ip}...")
        # Executa o ping para testar a conectividade
        subprocess.run(["ping", "-c", "4", ip], check=True)  # '-c 4' envia 4 pacotes
        print("\n|------------------------ Teste finalizado ------------------------|")
        print("Conexão estabelecida com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao executar o comando: {e}")
        print("Verifique se o WireGuard está ativo, se o IP está correto ou se há firewall bloqueando a conexão.")
    enter_clear ()
def wireguardvpn_test_client (): 
    try:
        print("|-------------------- Testando a conexão WireGuard (Cliente) --------------------|")
        print("Verificando se há troca de pacotes entre o cliente e o servidor...")
        # Mostra o status atual do WireGuard
        subprocess.run(["sudo", "wg"], check=True)
        print("\nVerifique se o cliente consegue se comunicar com o servidor.")
        # Solicita o IP do servidor
        server_ip = input("Indique o IP do Servidor: ")
        print(f"Testando conectividade com o servidor {server_ip}...")
        # Ping para verificar conectividade
        subprocess.run(["ping", "-c", "4", server_ip], check=True)
        print("\nVerificando o IP público da conexão...")
        # Curl para verificar IP público
        subprocess.run(["curl", "ifconfig.me"], check=True)
        print("\n|------------------------ Teste finalizado ------------------------|")
        print("Conexão do cliente com sucesso!")
        print("Podes ainda realizar testes com o comando traceroute...")
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao executar o comando: {e}")
        print("Verifique se o WireGuard está ativo, se o IP do servidor está correto ou se há firewall bloqueando a conexão.")
    enter_clear ()
def wireguardvpn_config ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_config_menu ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            try:
                                os.system("cls" if os.name == "nt" else "clear")
                                wireguardvpn_config_server ()
                                input ("Clique enter ara continuar... ")
                                subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
                            except subprocess.CalledProcessError as e:
                                print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
                            continue
                        case 2:
                            try:
                                os.system("cls" if os.name == "nt" else "clear")
                                wireguardvpn_config_client ()
                                input ("Clique enter ara continuar... ")
                                subprocess.run(["sudo", "nano", "/etc/sysctl.conf"], check=True) 
                                subprocess.run(["sudo", "sysctl", "-p"], check=True)
                            except subprocess.CalledProcessError as e:
                                print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
                            continue
                        case 3:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
def wireguardvpn_comandos ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_comandos_menu ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            start_wireguardvpn ()
                            continue
                        case 2:
                            enable_wireguardvpn ()
                            continue
                        case 3:
                            print ("Indisponivel no momento...")
                            enter_clear ()
                            continue
                        case 4:
                            stop_wireguardvpn ()
                            continue
                        case 5:
                            restart_wireguardvpn ()
                            continue
                        case 6:
                            version_wireguardvpn ()
                            continue
                        case 7:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
def wireguardvpn ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_menu_principal ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            instalacao_wireguardvpn_server ()
                            continue
                        case 2:
                            instalacao_wireguardvpn_cliente ()
                            continue
                        case 3:
                            wireguardvpn_config ()
                            continue
                        case 4:
                            wireguardvpn_comandos ()
                            continue
                        case 5:
                            wireguardvpn_config ()
                            continue
                        case 6:
                            wireguardvpn_test_server ()
                            continue
                        case 7:
                            wireguardvpn_test_client ()
                            continue
                        case 8:
                            desintslacao_wireguardvpn ()
                            continue
                        case 9:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue

try:
    wireguardvpn()
except KeyboardInterrupt:
    print("\nCMEasy encerrado!!")