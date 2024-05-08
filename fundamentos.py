# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input("Escreva aqui oque deseja conhecer sobre a arquitetura da AMAZON WEB SERVICES, sendo possíveis entradas agilidade, economia de custos, infraestrutura global, alta disponibilidade e elasticidade: ")

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "Na AWS, os modelos de preços flexíveis facilitam a otimização de gastos, permitindo aos usuários escolherem entre diversas opções de pagamento conforme suas necessidades, como pay-as-you-go e Reserved Instances. Isso maximiza o valor dos investimentos em nuvem."
    
    elif vantagem == "infraestrutura global":
        return "Na AWS, a entrega global eficiente de recursos é garantida pela ampla rede de data centers e pela Amazon CloudFront, proporcionando acesso rápido e confiável em qualquer lugar do mundo."
        
    elif vantagem == "alta disponibilidade":
        return "Na AWS, alta disponibilidade é alcançada através da distribuição de cargas de trabalho em várias zonas de disponibilidade dentro de uma região. Isso garante que os recursos estejam sempre acessíveis, mesmo em caso de falha em uma zona."
        
    elif vantagem == "elasticidade":
        return "Na AWS, elasticidade permite dimensionar recursos automaticamente conforme a demanda varia, garantindo desempenho e disponibilidade otimizados. Com serviços como Amazon EC2 Auto Scaling e AWS Lambda, isso é integrado, adaptando-se continuamente à carga de trabalho."
        
    elif  vantagem == "agilidade":
        return "Na AWS, a agilidade no desenvolvimento, teste e implantação é facilitada por serviços como AWS CodePipeline e AWS CodeDeploy. Com automação e escalabilidade, equipes podem lançar novos recursos de forma rápida e eficiente."
 
 
# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem".
print(descrever_vantagem(entrada))