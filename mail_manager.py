import smtplib
from email.mime.text import MIMEText
 
def send_email(receiver, contents):
    # 세션 생성
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # TLS 보안 시작
    s.starttls()
    
    # 로그인 인증
    s.login('너의 아이디', '코드')
    
    # 보낼 메시지 설정
    msg = MIMEText(str(contents))
    msg['Subject'] = 'To ' + str(receiver)
    
    # 메일 보내기
    s.sendmail('informationdoor04@gmail.com', str(receiver), msg.as_string())
    print("Sending...")
    # 세션 종료
    s.quit()
    return 'done'
