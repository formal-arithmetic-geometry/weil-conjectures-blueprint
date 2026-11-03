+++
id = "def-sp-exact-couple"
kind = "definition"
title = "Bigraded exact couples"
lean = ["CategoryTheory.ExactCouple", "CategoryTheory.ExactCouple.derived", "CategoryTheory.ExactCouple.spectralSequence"]
order = 513
uses = ["def-sp-abelian"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian]. An *exact couple*
$(D,E,\alpha,f,g)$ inside the bigraded objects $D=\bigoplus D^{p,q}$,
$E=\bigoplus E^{p,q}$ consists of maps of bidegrees

$$
 \alpha:D^{p,q}\to D^{p-1,q+1}\quad(-1,+1),\qquad
 f:E^{p,q}\to D^{p+2,q-1}\quad(+2,-1),\qquad
 g:D^{p,q}\to E^{p,q}\quad(0,0)
$$

such that the composite of two consecutive structure maps is zero and at
every $(p,q)$ the following exactness conditions hold (each comparing
subobjects of one single object):

$$
 \ker\!\Bigl(\alpha:D^{p,q}\to D^{p-1,q+1}\Bigr)
  =\operatorname{im}\!\Bigl(f:E^{p-2,q+1}\to D^{p,q}\Bigr),
$$

$$
 \ker\!\Bigl(f:E^{p,q}\to D^{p+2,q-1}\Bigr)
  =\operatorname{im}\!\Bigl(g:D^{p,q}\to E^{p,q}\Bigr),
$$

$$
  \ker\!\Bigl(g:D^{p,q}\to E^{p,q}\Bigr)
   =\operatorname{im}\!\Bigl(\alpha:D^{p+1,q-1}\to D^{p,q}\Bigr).
$$

Setting $d:=g\circ f:E^{p,q}\to E^{p+2,q-1}$ (bidegree
$(+2,-1)$), the identity $f\circ g=0$ gives $d\circ d=0$, and the *derived
couple* is

$$
 D'^{p,q}:=\operatorname{im}\!\bigl(\alpha:D^{p+1,q-1}\to D^{p,q}\bigr),
 \qquad
 E'^{p,q}:=\frac{\ker\!\bigl(d:E^{p,q}\to E^{p+2,q-1}\bigr)}
                    {\operatorname{im}\!\bigl(d:E^{p-2,q+1}\to E^{p,q}\bigr)},
$$

with

$$
 \alpha':=\alpha|_{D'},\qquad
 f'(x):=f(x)\ \ (x\in\ker d),\qquad
 g'(y):=\overline{g(y')}\ \ (y=\alpha(y')\in D'^{p,q}).
$$

The *spectral sequence of the couple* is $E_2=E$, $d_2=d$, $E_3=E'$,
$d_3=g'\circ f'$ (bidegree $(+3,-2)$), and recursively $E_{r+1}=E'_r$, so
that $d_r$ has bidegree $(+r,1-r)$ for $r\geq2$.

The bidegrees are those of the truncation couple of a t-structure
filtration, with the abutment in total degree $p+q$; they are the convention
in which the hypercohomology spectral sequence has
$E_2^{p,q}\Rightarrow\mathcal H^{p+q}$.

More generally, for an abelian group $\kappa$ of indices and degrees
$a,b,c\in\kappa$, an *exact couple of degrees $(a,b,c)$* consists of
$\kappa$-graded objects $D=(D^i)$, $E=(E^i)$ and maps
$\alpha:D^i\to D^{i+a}$, $f:E^i\to D^{i+b}$, $g:D^i\to E^{i+c}$ such that
the composite of two consecutive structure maps is zero and the three
sequences above are exact at every index. The same formulas define its
derived couple, an exact couple of degrees $(a,b,c-a)$, and the spectral
sequence of the couple starting at a page $r_0$ has as $r$-th page
($r\geq r_0$) the complex $(E,g\circ f)$ of the $(r-r_0)$-th derived couple.
The bigraded couples above are the case $\kappa=\mathbb Z^2$,
$a=(-1,1)$, $b=(2,-1)$, $c=(0,0)$, $r_0=2$; the couple of a filtered complex
is the case $b=(1,0)$, $r_0=1$.
