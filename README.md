<img src="https://raw.githubusercontent.com/mikarrega/dosepet/d392bf05eb50f0c73952c03cff2e53a90cd7f007/public/dosepet-logo-vertical.svg" width="400" />
Sobre o projeto
<p>Ajudamos a manter a saúde do seu animal de estimação em dia</p> <p>Enviamos lembretes de vacinação e medicamentos por e-mail</p>
Como rodar o projeto
Para Windows (CMD):

<p>Utilize <code> python -m venv venv </code> para criar um ambiente virtual</p> <p>Utilize <code> source venv/Scripts/activate </code> para ativar o ambiente virtual</p> <p>Utilize <code> source venv/bin/activate </code> para ativar o ambiente virtual # No Linux/macOS </p> <p>Utilize <code> pip install -r requirements.txt </code> para instalar as bibliotecas necessárias </p> <p>Utilize <code> flask db init </code> para iniciar o ambiente de migração do banco de dados </p> <p>Utilize <code> flask db migrate -m "Migration inicial" </code> para gerar os scripts de migração com base nos modelos </p> <p>Utilize <code> flask db upgrade </code> para aplicar as migrações ao banco de dados </p> <p>Utilize <code> flask run </code> para iniciar o servidor local de desenvolvimento </p> <p>A página deverá ser acessada através da URL: <code> http://127.0.0.1:5000/ </code></p>
Observações
<p>Este projeto está em desenvolvimento inicial</p> <p>O backend usa Python com Flask e SQLite como banco de dados</p> <p>Neste momento temos construído as rotas de autenticação e atualização de dados do tutor</p> <p>Todo o frontend será desenvolvido em JavaScript utilizando Next.js</p> <p>A biblioteca de componentes ainda não foi decidida</p>
Desenvolvedoras
<p>Backend: <a href="https://www.linkedin.com/in/mirian-nascimento/" target="_blank" rel="noopener noreferrer">Miris</a></p> <p>Frontend: <a href="https://www.linkedin.com/in/michaeladafne/" target="_blank" rel="noopener noreferrer">Mika</a></p>
