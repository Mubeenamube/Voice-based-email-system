from text_speech import *
from send import *
from listmessages import *



while True :


 text_to_speech('say send to send a message !')
 text_to_speech('say receive to receive messages !')
 text_to_speech('say close to close the application !')
 text_to_speech('Speak')
 first_response=speech_to_text()

 if first_response == 'send' :
  send_message()
  text_to_speech('Message Send Successfully! ')

 elif first_response == 'receive' or first_response == 'tu' or first_response == 'two' or first_response == 'Tu' or first_response == 'to' or first_response == 'To' :
  text_to_speech('say receive for top ten messages')
  text_to_speech('say search to search for a sender')
  text_to_speech('Speak')
  receive_response=speech_to_text()
  if receive_response == 'receive' :
   get_message_list()
  if receive_response == 'search' or receive_response == 'Tu' or receive_response == 'tu' or receive_response == 'two' or receive_response == 'To' or receive_response == 'to':
   text_to_speech('Say the E-Mail of the sender!')
   text_to_speech('Speak')
   email=speech_to_text()
   words=email.split()
   modified_mail=str()
   for word in words:
     if word == 'underscore':
       modified_mail=modified_mail+'_'
     elif word == 'dot':
       modified_mail=modified_mail+'.'
     else:
       modified_mail=modified_mail+word

   modified_mail=modified_mail.lower()
   #query=speech_to_text()
   searched_message(modified_mail)
 elif first_response == 'close':
  exit()
 else:
  text_to_speech('Sorry you were not clear with your vocals !')
  continue
  
 


 

