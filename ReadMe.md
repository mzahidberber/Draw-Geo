<img src="drawcad.png">
<hr>
<h6 align="center">
  <a href="https://drawprogram.org/">DrawCAD |</a>
  <a href="https://drawprogram.org/Home/DrawCAD">Doc |</a>
  <a href="https://drawprogram.org/Home/DrawApi">Api |</a>
  <a href="https://drawprogram.org/Home/DrawGeo">Geo |</a>
  <a href="https://drawprogram.org/Home/DrawAuth">Auth</a>
</h6>

<hr>

<p>
Geo hizmeti python ile geometrik hesaplamalar yapabilmek için tasarlanmış django api projesidir. Hizmette herhangi bir kayıt işlemi yapılmamaktadır.Sadece gönderilen isteğe göre hesaplamaları yapar ve geriye sonucu döner.Hizmeti kullanmak için token bilgisine gerek yoktur.Hizmeti ile yapabileceğiniz sorgular için <a href="https://drawprogram.org/Home/DrawGeo">doc</a> adresini ziyaret edebilirsiniz.
</p>
<h3>Başlangıç</h3>
<p>Kullanmak için dockerhubtan imageyi indirebilir</p>

```
docker pull mzahidberber/drawgeo:latest
```

<p>veya kaynak kodu indirip kendiniz image oluşturabilirsiniz</p>

```
docker build -t drawgeo .
```

<p>
Docker run ile çalıştırabilirsiniz.Environmentlerden allowed hosts ve debug zorunlu değildir.Allowed hosts environmentini göndermesenizde localde çalışacaktır.Debug ise varsayılan olarak false dir.
</p>

```
docker run --name geo -p 5001:5001 --env SECRET_KEY=<secretkey> --env ALLOWED_HOSTS=<ip> --env DEBUG=False drawgeo
```



