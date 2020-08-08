# TrBackdoor
<br/>![ConverotrExe](https://github.com/OgulcanKacarr/TrBackdoor/blob/master/ConfigImages/Command.png)
## Backdoor Ayarları
Not: sysupgrades ismini isterseniz değiştirebilirsiniz. Lakin backdoor'u hedefte saklamak istediğiniz zaman değiştirmiş olacağınız isim kullanıcıyı şüphelendirmemeli.<br/>
Öncelikle "sysupgrades.py" dosyamızı herhangi bir editör ile açınız ('SublimeText3').<br/>Daha sonra sınıfın dışında yani kod bloklarının altında yer alan"ConfigSocket = MySocket("<İP>"<PORT>) kısmına backdoor için bir ip adresi ve port numarası giriniz. Yani
<br/>![ConverotrExe](https://github.com/OgulcanKacarr/TrBackdoor/blob/master/ConfigImages/BackdoorConfig.png)
## Exe'ye Çevirme
"sysupgrades.py" backdoor'umuzu hedefimize göndermeden önce "pyinstaller" kullanarak exe'ye çevirelim.<br/> Burada size önerdiğim exe'ye çevirme işleminde mutlaka bir icon ekleyiniz ve noconsole komutunu kullanınız. Fakat dosyayı bir başka dosya ile (pdf) birleştirmeyiniz. Çünkü bağlantı sağladıktan sonra "migrate" komutunu kullandığınız sırada backdoor saklanacaktır. Kullanıcı bilgisayarını her başlattığında başlayacaktır. İşte bu başlatma sırasında her defasında backdoor ile birlikte pdf açılmasın ki kullanıcı şüphelenmesin diye exe'ye çevirirken bir dosya ile birleştirilmesini önermiyorum.<br/>
<br/>![ConverotrExe](https://github.com/OgulcanKacarr/TrBackdoor/blob/master/ConfigImages/ExeConvertor.png)<br/>
## Listener Ayarları
"Listener.py" dosyamızı yine bir editör ile açalım. Ardından yine alt tarafta yer alan<br/> "my_socket_listener = SocketListener("<İP>"<PORT>)" kısmını kendi local ip adresinizi giriniz. Yani<br/>
<br/>![ConfigListener](https://github.com/OgulcanKacarr/TrBackdoor/blob/master/ConfigImages/ListenerSettings.png)<br/>Böylece artık gelen bağlantıları dinlemeye hazırsınız.<br/>[!<br/>[![SC2 Video](https://github.com/OgulcanKacarr/TrBackdoor/blob/master/ConfigImages/TrBackdoor.gif)](https://www.youtube.com/watch?v=NVCAhal6wl8&feature=youtu.be)

