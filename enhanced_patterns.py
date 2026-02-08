#!/usr/bin/env python3
"""
PATTERNS EXPANDIDOS para análise de vendas
De 26 patterns originais para ~80+ patterns organizados por categoria
"""

def get_enhanced_patterns():
    """
    Retorna dicionário expandido de patterns para análise de vendas
    Organizado em 15 categorias vs 7 originais
    """
    
    return {
        # ========================================
        # 1. PRODUTOS (expandido de 4 para 10)
        # ========================================
        'seguro_carga': r'\b(seguro\s+carga|carga|transporte\s+carga)',
        'seguro_garantia': r'\b(seguro\s+garantia|garantia|performance\s+bond)',
        'seguro_vida': r'\b(seguro\s+vida|vida\s+grupo|beneficiário)',
        'seguro_empresarial': r'\b(seguro\s+empresarial|empresarial|corporativo)',
        'fiança': r'\b(fiança|fiança\s+locatícia)',
        'rc': r'\b(rc|responsabilidade\s+civil|r\.c\.)',
        'd_o': r'\b(d&o|d\s+e\s+o|diretores\s+oficiais)',
        'patrimonial': r'\b(patrimonial|incêndio|roubo)',
        'frota': r'\b(frota|veículos|automotivo)',
        'saude': r'\b(saúde|plano\s+saúde|médico)',
        
        # ========================================
        # 2. PROCESSOS (expandido de 5 para 12)
        # ========================================
        'cotacao': r'\b(cotação|cotar|cotando|orçamento)',
        'proposta': r'\b(proposta|propostas|enviar\s+proposta)',
        'licitacao': r'\b(licitação|licitações|licitar|edital)',
        'contrato': r'\b(contrato|contratar|contratação|assinar)',
        'apolice': r'\b(apólice|apolice|emissão)',
        'renovacao': r'\b(renovação|renovar|renovando|vencimento)',
        'sinistro': r'\b(sinistro|sinistros|acionamento|acionar)',
        'vistoria': r'\b(vistoria|inspeção|laudo)',
        'aprovacao': r'\b(aprovação|aprovar|aprovado|aceito)',
        'analise_risco': r'\b(análise\s+risco|risco|underwriting)',
        'followup': r'\b(retornar|retorno|voltar\s+falar|dar\s+retorno)',
        'encerramento': r'\b(fechado|finalizar|concluir|assinado)',
        
        # ========================================
        # 3. DOCUMENTAÇÃO (expandido de 4 para 8)
        # ========================================
        'minuta': r'\b(minuta|minuta\s+contrato)',
        'cnpj': r'\b(cnpj|razão\s+social)',
        'nota_fiscal': r'\b(nota\s+fiscal|nf|fatura)',
        'documento': r'\b(documento|documentação|documentos)',
        'certidao': r'\b(certidão|certidoes|regularidade)',
        'contrato_social': r'\b(contrato\s+social|estatuto)',
        'procuracao': r'\b(procuração|procurador|representante\s+legal)',
        'anexo': r'\b(anexo|anexos|anexar|enviar\s+anexo)',
        
        # ========================================
        # 4. VALORES/FINANCEIRO (expandido de 4 para 10)
        # ========================================
        'valor': r'\b(valor|valores|preço|custo)',
        'desconto': r'\b(desconto|descontar|redução)',
        'parcela': r'\b(parcela|parcelamento|parcelar|dividir)',
        'pagamento': r'\b(pagamento|pagar|quitação)',
        'premio': r'\b(prêmio|premio|mensalidade)',
        'comissao': r'\b(comissão|remuneração)',
        'franquia': r'\b(franquia|franquias)',
        'is': r'\b(is|importância\s+segurada|cobertura)',
        'orcamento': r'\b(orçamento|orçar)',
        'condicao_pagamento': r'\b(condição\s+pagamento|forma\s+pagamento|à\s+vista)',
        
        # ========================================
        # 5. TEMPO/URGÊNCIA (expandido de 3 para 7)
        # ========================================
        'urgente': r'\b(urgente|urgência)',
        'prazo': r'\b(prazo|prazos|deadline)',
        'rapido': r'\b(rápido|rapidamente|agilizar|agilidade)',
        'hoje': r'\b(hoje|agora|imediato)',
        'amanha': r'\b(amanhã|próximo|semana)',
        'aguardando': r'\b(aguardando|esperar|esperando)',
        'atrasado': r'\b(atrasado|atraso|vencido)',
        
        # ========================================
        # 6. DÚVIDAS/PROBLEMAS (expandido de 3 para 6)
        # ========================================
        'duvida': r'\b(dúvida|duvida|dúvidas|duvidas)',
        'problema': r'\b(problema|problemas|dificuldade)',
        'erro': r'\b(erro|erros|incorreto)',
        'confusao': r'\b(confusão|confuso|não\s+entendi)',
        'pendencia': r'\b(pendência|pendências|falta)',
        'reclamacao': r'\b(reclamação|reclamar|insatisfeito)',
        
        # ========================================
        # 7. POSITIVO/ENGAJAMENTO (expandido de 3 para 8)
        # ========================================
        'perfeito': r'\b(perfeito|ótimo|otimo|excelente)',
        'obrigado': r'\b(obrigado|obrigada|agradeço|agradecimento)',
        'entendi': r'\b(entendi|compreendi|certo|ok)',
        'interessado': r'\b(interessado|interesse|interessante)',
        'acordo': r'\b(acordo|concordo|de\s+acordo)',
        'confianca': r'\b(confiança|confiar|recomendação)',
        'satisfeito': r'\b(satisfeito|satisfação|feliz)',
        'gostei': r'\b(gostei|gostar|legal)',
        
        # ========================================
        # 8. OBJEÇÕES (NOVA CATEGORIA - 9 patterns)
        # ========================================
        'caro': r'\b(caro|cara|muito\s+caro|preço\s+alto)',
        'concorrente': r'\b(concorrente|concorrência|outra\s+seguradora)',
        'ja_tenho': r'\b(já\s+tenho|já\s+possuo|tenho\s+seguro)',
        'pensar': r'\b(pensar|vou\s+pensar|deixa\s+ver)',
        'nao_interesse': r'\b(não\s+interesse|sem\s+interesse|não\s+preciso)',
        'decisao': r'\b(decisão|decidir|sócio|gerente|diretor)',
        'comparar': r'\b(comparar|comparação|analisar|avaliar)',
        'depois': r'\b(depois|mais\s+tarde|outra\s+hora)',
        'fornecedor_atual': r'\b(fornecedor\s+atual|corretor\s+atual|já\s+trabalho)',
        
        # ========================================
        # 9. SINAIS DE FECHAMENTO (NOVA - 7 patterns)
        # ========================================
        'quando': r'\b(quando|prazo\s+entrega|prazo\s+emissão)',
        'como_funciona': r'\b(como\s+funciona|processo|procedimento)',
        'proximo_passo': r'\b(próximo\s+passo|próxima\s+etapa|o\s+que\s+preciso)',
        'enviar': r'\b(enviar|mandar|pode\s+enviar)',
        'comecar': r'\b(começar|iniciar|vamos\s+fazer)',
        'assinar': r'\b(assinar|assinatura|onde\s+assino)',
        'prosseguir': r'\b(prosseguir|continuar|vamos\s+prosseguir)',
        
        # ========================================
        # 10. NEGOCIAÇÃO (NOVA - 6 patterns)
        # ========================================
        'negociar': r'\b(negociar|negociação)',
        'melhor_preco': r'\b(melhor\s+preço|baixar\s+preço|reduzir)',
        'concessao': r'\b(concessão|conceder|flexibilizar)',
        'contraoferta': r'\b(contra\s+oferta|propor|sugerir)',
        'alinhamento': r'\b(alinhamento|alinhar|combinar)',
        'fechar_negocio': r'\b(fechar\s+negócio|bater\s+martelo|temos\s+acordo)',
        
        # ========================================
        # 11. RELACIONAMENTO (NOVA - 6 patterns)
        # ========================================
        'parceria': r'\b(parceria|parceiro|longo\s+prazo)',
        'confianca_marca': r'\b(empresa\s+grande|tradicional|mercado)',
        'indicacao': r'\b(indicação|indicar|recomendar)',
        'atendimento': r'\b(atendimento|suporte|apoio)',
        'facilidade': r'\b(fácil|facilidade|prático)',
        'personalizacao': r'\b(personalizado|personalizar|sob\s+medida)',
        
        # ========================================
        # 12. TÉCNICO/COMPLIANCE (NOVA - 7 patterns)
        # ========================================
        'clausula': r'\b(cláusula|condição|cobertura)',
        'exclusao': r'\b(exclusão|excluir|não\s+cobre)',
        'regulamento': r'\b(regulamento|norma|legislação)',
        'susep': r'\b(susep|regulador|fiscalização)',
        'apice': r'\b(ápice|limite|máximo)',
        'carencia': r'\b(carência|período\s+carência)',
        'vigencia': r'\b(vigência|período|duração)',
        
        # ========================================
        # 13. COMPETITIVO (NOVA - 5 patterns)
        # ========================================
        'diferencial': r'\b(diferencial|vantagem|benefício)',
        'comparacao': r'\b(melhor|superior|diferente)',
        'inovacao': r'\b(inovação|inovador|novidade)',
        'exclusivo': r'\b(exclusivo|único|especial)',
        'benchmark': r'\b(mercado|padrão|referência)',
        
        # ========================================
        # 14. RISCO/SEGURANÇA (NOVA - 5 patterns)
        # ========================================
        'risco': r'\b(risco|riscos|exposição)',
        'protecao': r'\b(proteção|proteger|segurança)',
        'prevencao': r'\b(prevenção|prevenir|mitigar)',
        'cobertura': r'\b(cobertura|coberto|protege)',
        'indenizacao': r'\b(indenização|indenizar|ressarcir)',
        
        # ========================================
        # 15. OPERACIONAL (NOVA - 5 patterns)
        # ========================================
        'sistema': r'\b(sistema|plataforma|portal)',
        'email': r'\b(email|e-mail|correio)',
        'telefone': r'\b(telefone|ligar|contato)',
        'reuniao': r'\b(reunião|meeting|encontro)',
        'apresentacao': r'\b(apresentação|apresentar|demonstração)',
    }


def categorize_patterns():
    """Retorna os patterns organizados por categoria para análise"""
    patterns = get_enhanced_patterns()
    
    categories = {
        'Produtos': [
            'seguro_carga', 'seguro_garantia', 'seguro_vida', 'seguro_empresarial',
            'fiança', 'rc', 'd_o', 'patrimonial', 'frota', 'saude'
        ],
        'Processos': [
            'cotacao', 'proposta', 'licitacao', 'contrato', 'apolice', 'renovacao',
            'sinistro', 'vistoria', 'aprovacao', 'analise_risco', 'followup', 'encerramento'
        ],
        'Documentação': [
            'minuta', 'cnpj', 'nota_fiscal', 'documento', 'certidao',
            'contrato_social', 'procuracao', 'anexo'
        ],
        'Financeiro': [
            'valor', 'desconto', 'parcela', 'pagamento', 'premio',
            'comissao', 'franquia', 'is', 'orcamento', 'condicao_pagamento'
        ],
        'Urgência': [
            'urgente', 'prazo', 'rapido', 'hoje', 'amanha', 'aguardando', 'atrasado'
        ],
        'Problemas': [
            'duvida', 'problema', 'erro', 'confusao', 'pendencia', 'reclamacao'
        ],
        'Positivo': [
            'perfeito', 'obrigado', 'entendi', 'interessado', 'acordo',
            'confianca', 'satisfeito', 'gostei'
        ],
        'Objeções': [
            'caro', 'concorrente', 'ja_tenho', 'pensar', 'nao_interesse',
            'decisao', 'comparar', 'depois', 'fornecedor_atual'
        ],
        'Fechamento': [
            'quando', 'como_funciona', 'proximo_passo', 'enviar',
            'comecar', 'assinar', 'prosseguir'
        ],
        'Negociação': [
            'negociar', 'melhor_preco', 'concessao', 'contraoferta',
            'alinhamento', 'fechar_negocio'
        ],
        'Relacionamento': [
            'parceria', 'confianca_marca', 'indicacao', 'atendimento',
            'facilidade', 'personalizacao'
        ],
        'Técnico': [
            'clausula', 'exclusao', 'regulamento', 'susep', 'apice', 'carencia', 'vigencia'
        ],
        'Competitivo': [
            'diferencial', 'comparacao', 'inovacao', 'exclusivo', 'benchmark'
        ],
        'Risco': [
            'risco', 'protecao', 'prevencao', 'cobertura', 'indenizacao'
        ],
        'Operacional': [
            'sistema', 'email', 'telefone', 'reuniao', 'apresentacao'
        ]
    }
    
    return {cat: {k: patterns[k] for k in keys} for cat, keys in categories.items()}


def print_pattern_summary():
    """Imprime resumo dos patterns disponíveis"""
    cats = categorize_patterns()
    
    print("="*80)
    print("📊 PATTERNS EXPANDIDOS - RESUMO")
    print("="*80)
    
    total = 0
    for cat, patterns in cats.items():
        count = len(patterns)
        total += count
        print(f"\n{cat:20s} ({count:2d} patterns)")
        for key in list(patterns.keys())[:3]:
            print(f"  • {key}")
        if count > 3:
            print(f"  ... +{count-3} mais")
    
    print("\n" + "="*80)
    print(f"TOTAL: {total} patterns (vs 26 originais)")
    print("="*80)


if __name__ == "__main__":
    print_pattern_summary()

