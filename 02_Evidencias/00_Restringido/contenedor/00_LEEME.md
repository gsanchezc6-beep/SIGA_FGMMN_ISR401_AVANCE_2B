# El contenedor de la zona restringida, dentro del repositorio

**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Que hay aqui

**272 fragmentos** de un unico archivo `SIGA_zona_restringida.7z`, cifrado con **AES-256** y
con los nombres de archivo tambien cifrados. Contiene el material que el consentimiento
firmado **no autoriza a publicar**, y que esta enumerado en
[`../README_Restringido.md`](../README_Restringido.md), apartado 2.

Los fragmentos **no se pueden abrir por separado**. Solo sirven los 272 juntos y en orden.

| | |
|---|---|
| Archivo original | `SIGA_zona_restringida.7z`, 6 822 192 770 bytes |
| SHA-256 del original | `d225b1929f89d1cfd7079e91d37445674bdc593a10bc39a528ac205649f05f8a` |
| Fragmentos | 272, de 24 MiB cada uno salvo el ultimo |
| Cifrado | AES-256, con cabecera de nombres cifrada |
| Fecha del contenedor | 2026-09-04 |

## 2. Por que esta partido, y por que esta aqui dentro

**Partido**, porque GitHub rechaza cualquier archivo de mas de 100 MB sin Git LFS, y este
repositorio no usa LFS a proposito --- consta en `.gitattributes`. Cortado en 24 MiB, cada
fragmento entra holgadamente y el conjunto viaja como objetos normales de Git.

**Aqui dentro**, y no en un servicio externo, porque un enlace es un punto unico de fallo.
Hasta el 2026-09-06 este contenedor vivia solo en el OneDrive institucional y el repositorio
publicaba su direccion. Eso significa que si el enlace caduca, si la cuenta institucional
cambia, o si quien evalua no puede abrirlo, **la evidencia restringida deja de existir a
efectos practicos**, aunque el archivo siga en alguna parte. Depositado aqui, viaja con el
repositorio, se clona con el y se archiva con el en Software Heritage.

**El enlace de OneDrive se conserva** como copia redundante, no como unica via. Las dos
rutas llevan al mismo archivo y su suma lo demuestra.

## 3. Como reconstruirlo y abrirlo

Con 7-Zip instalado basta **abrir el primer fragmento**; el programa reconoce la secuencia
y reune el resto solo:

```
02_Evidencias/00_Restringido/contenedor/SIGA_zona_restringida.7z.001
```

Pedira la contrasena, que **no consta en este repositorio** y se entrega al docente
responsable por el Sistema de Gestion Academica. Por linea de orden:

```bash
7z x SIGA_zona_restringida.7z.001
```

Sin 7-Zip, los fragmentos se reunen concatenandolos en orden:

```bash
cat SIGA_zona_restringida.7z.* > SIGA_zona_restringida.7z
```

## 4. Como comprobar que llegaron completos

Antes de pedir la contrasena a nadie, conviene comprobar que el clon trajo los 272
fragmentos intactos. Esto no necesita contrasena:

```bash
cat SIGA_zona_restringida.7z.* | sha256sum
```

Debe dar exactamente:

```
d225b1929f89d1cfd7079e91d37445674bdc593a10bc39a528ac205649f05f8a
```

Si coincide, el contenedor esta completo y sin alterar. Si no coincide, falta algun
fragmento o el clon se trunco: repetir el `git clone` antes de sospechar del cifrado.

La suma de cada fragmento por separado esta ademas en el manifiesto general del
repositorio, `checksums.sha256`, de modo que `sha256sum -c` localiza **cual** de los 272
vino mal.

## 5. Lo que esta comprobado y lo que no

**Comprobado:** que los 272 fragmentos reconstruyen el archivo original byte a byte. Se
calculo la suma SHA-256 del original y la de la concatenacion de los fragmentos, y
coinciden. Tambien que 7-Zip reconoce el conjunto como archivo cifrado desde el primer
fragmento.

**Comprobado tambien, el 2026-09-07:** que el contenedor **descifra y se extrae**. Lo hizo
quien custodia la contrasena, no consta aqui como se hizo, y el resultado son **49 archivos,
6,4 GB**: las grabaciones de video y audio de la ronda terminal y de las sesiones tecnicas,
las fotografias de sesion y el acta firmada de `WT-08`.

Las dos comprobaciones juntas cierran la cadena: los 272 fragmentos reconstruyen el archivo
**byte a byte** --- misma suma SHA-256 --- y ese archivo **se abre**. Si la concatenacion es
identica al original y el original descifra, la concatenacion descifra; no hay hueco entre
las dos afirmaciones.

> **Despues de extraerlo, borre la carpeta descomprimida.** Contiene 6,4 GB de material
> identificable sin cifrar: nombres, caras y voces de participantes que consintieron
> justamente lo contrario. El contenedor existe para que ese material **no** quede suelto en
> un escritorio.
