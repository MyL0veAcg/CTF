from Crypto.Util.number import *
from gmpy2 import *

c_list = [115160381937982584844203740307577838723098158351957418441122614601623591983660763818632687780356276160948736372069790645353203889600947947986103143998329166834689942318893888708301301281562551160977302219525149679353759933981443072027067697468096562389932683462922210737666093435832826466628003451437224096856, 49075850210998345750668438773183257852433109528025140925301831872825185175515966185667869555589760504872818225880930677099751757950658906108858107638718843724483181266345338640929683320335626599933889035082982627593437797641718119231711526267722589589618406627508376448245393791578734899602353870635052162071]
e_list = [28927, 16993]
n = 152355319063431466172139269724665055858093458078950897484032623313450804994707940705280161558843346692642644606949693903750964494087135983703980138435557268626634601631134736839984918294167358499288195865310790330490302552302553920172898373940854014299952714216771929041094157237851916017967948833298657585477

a,s1,s2 = gcdext(e_list[0], e_list[1])
m = pow(c_list[0], s1, n) * pow(c_list[1], s2, n) % n
print(long_to_bytes(m)) 