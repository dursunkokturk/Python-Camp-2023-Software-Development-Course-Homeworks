HTML Nedir ?— HTML Locators Nedir ?— Selenium’da aksiyonlar (send_keys, click vb..) Nelerdir?
HTML Nedir ?

    HTML, Hyper Text Markup Language kelimelerinin kısaltılmışı halidir.
    Bu nedenle HTML bir programlama dili değil, bir işaretleme dili olarak ele alınır. HTML komutları, metin, resim, ses, video gibi içeriklerin sayfadaki yerleşimini ve ziyaretçiye gösterilmesini sağlar.
    HTML sayfalarının dosya uzantısı .htm veya .html’dir. HTML dili 1980 yılında CERN laboratuvarlarında görevli olan Tim Berners-Lee tarafından geliştirilmiştir.
    HTML sayfası isimlendirilirken Türkçe karakterlere yer verilmez.
    HTML sayfası isimlendirilirken boşluklara yer verilmez. Her kelime arasına — konularak yazılabilir.

HTML Locators Nedir ?

    Browser’ı açtıktan sonra giriş yapılan sitede neler yapılabileceğine bakıyoruz.
    Giriş yapılan sitede sitenin açılma hızını kontrol edebiliriz.
    Kullanıcı girişi yapılıyorsa, kullanıcı girişinde hatalı bilgiler girildiğinde ortaya çıkan sonucu kontrol edebiliriz.
    Kullanıcı girişi kontrolü yapmak için HTML Tag ları içinden belirli tag ları kullanarak Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.
    HTML Taglarını kullanarak locator işlemini yapmak için çalışılacak objenin HTML kodları görmek gerekiyor.
    Site kontolü yapılması için HTML Tag ları içinde HTML tag larının tercih sırası:
    ID
    Name
    ClassName
    TagName
    LinkText
    CssSelector
    XPath

XPath Selenium Aksiyonları :

    click() = Tıklamak için kullanılır.
    clear() = İçeriği temizlemek için kullanılır.
    submit = Teslim etmek/göndermek için kullanılır.
    select_by_visible_text = Görünür bir metne tıklamak için kullanılır.
    Scroll = Aşağı veya yukarı kaydırmak için kullanılır.
    Switch to Frame = Bir frame’in içine geçmek için kullanılır.
    Switch to Window = Bir pencereye geçmek için kullanılır.
    Back() = Önceki sayfaya gitmek için kullanılır.
    Forward() = Sonraki sayfaya gitmek için kullanılır.
    Refresh() = Sayfayı yenilemek için kullanılır.
    Bu HTML Tag larını kullanabilmek için By class ını proje dosyasına import etmek gerekiyor. Çünkü HTML kodlarını sadece By class ı üzerinden proje içinde kullanabiliriz.
