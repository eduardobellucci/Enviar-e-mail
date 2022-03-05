import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
class Enviaremail():
    def __init__(self) -> None:
       self.usuario='e-mail'
       self.password='senha'
       self.email_smt_server='smtp.gmail.com'
       self.msg=MIMEMultipart()
       self.destinatario('e-mail1','e-mail2')
       self.assuntodoemail('teste','teste')
       self.cabecario()
       self.mensagempraenviar('ola','teste')
       self.conexaocomoservidor()
    def destinatario(self,*emailpraenviar):
        self.destinatario1=[*emailpraenviar]
        return self.destinatario1
    def assuntodoemail(self,*assunto):
        self.assunto=[*assunto]
        return self.assunto
    def cabecario(self):
        self.msg['From']=self.usuario
        self.msg['Subject']=','.join(self.assunto)
        self.msg["To"]=','.join(self.destinatario1)
    def mensagempraenviar(self,*mensagem):
       self.mensagem_enviada=[*mensagem]
       self.convertestringmensagemenviada=','.join(self.mensagem_enviada)
       msg_text=MIMEText(self.convertestringmensagemenviada,'html')
       self.msg.attach(msg_text)
    def conexaocomoservidor(self):
        try:
            self.smtp=smtplib.SMTP(self.email_smt_server,587)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.ehlo()
            self.smtp.login(self.usuario,self.password)
            self.smtp.sendmail(self.usuario,self.destinatario1,self.msg.as_string())
            print(self.destinatario1)
            self.smtp.quit()
            print('deu certo')
        except Exception as err:
            print(f'ocorreu algum erro:{err}')
        
a=Enviaremail()