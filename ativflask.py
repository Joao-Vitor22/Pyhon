from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo Profissional</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="resume-container">
        <!-- Cabeçalho / Contato -->
        <header>
            <h1>João Vitor Santos Carvalho
            </h1>
            <p class="contact-info">
                📞 (11) 99999-9999 | ✉️ seu.email@email.com | 📍 São Paulo, SP
            </p>
        </header>

        <!-- Experiência de Trabalho -->
        <section>
            <h2>Experiência Profissional</h2>
            
            <div class="item">
                <div class="item-header">
                    <span class="title">Desenvolvedor Júnior</span>
                    <span class="date">2024 - Presente</span>
                </div>
                <div class="company">Empresa Alfa</div>
                <p class="description">Desenvolvimento de sistemas web, manutenção de bancos de dados e automação de processos internos.</p>
            </div>

            <div class="item">
                <div class="item-header">
                    <span class="title">Estagiário de Tecnologia</span>
                    <span class="date">2022 - 2024</span>
                </div>
                <div class="company">Empresa Beta</div>
                <p class="description">Suporte técnico a usuários, testes de software e criação de relatórios automatizados.</p>
            </div>
        </section>

        <!-- Educação / Escolas -->
        <section>
            <h2>Formação Acadêmica</h2>
            
            <div class="item">
                <div class="item-header">
                    <span class="title">Graduação em Engenharia de Software</span>
                    <span class="date">2020 - 2024</span>
                </div>
                <div class="company">Universidade X</div>
            </div>

            <div class="item">
                <div class="item-header">
                    <span class="title">Ensino Médio Técnico em Informática</span>
                    <span class="date">2017 - 2019</span>
                </div>
                <div class="company">Escola Técnica Y</div>
            </div>
        </section>

        <!-- Cursos Complementares -->
        <section>
            <h2>Cursos e Certificações</h2>
            <ul class="bullet-list">
                <li>Curso Avançado de Desenvolvimento Web - Plataforma Online (40h)</li>
                <li>Metodologias Ágeis e Framework Scrum - Instituto Z (20h)</li>
                <li>Banco de Dados SQL Avançado - Escola de Tecnologia (30h)</li>
            </ul>
        </section>

        <!-- Idiomas e Proficiência -->
        <section>
            <h2>Idiomas</h2>
            <ul class="bullet-list">
                <li><strong>Inglês:</strong> Avançado</li>
                <li><strong>Espanhol:</strong> Intermediário</li>
            </ul>
        </section>
    </div>

</body>
</html>

    """


if __name__ == "__main__":
    app.run(debug=True)
