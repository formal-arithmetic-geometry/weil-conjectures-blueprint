+++
id = "sk-lem-wft-curve-heart"
kind = "lemma"
title = "Perverse sheaves on a curve"
order = 3967
uses = ["sk-def-sf-weil-complexes", "sk-lem-coefficient-heart", "sk-p-real-integral"]
tags = ["sketch"]
+++
Let $C$ be a smooth curve over a perfect field. A constructible
sheaf is called *punctual* if its support is a finite set of closed
points. We define two classes of objects of
$D^b_c(C_{\mathrm{pro\acute et}},\Qlb)$ by

$$
 \begin{split}
 {}^pD^{\le0}&=\{K:\mathcal H^aK=0\ (a>0),\
                         \mathcal H^0K\text{ is punctual}\},\\
 {}^pD^{\ge0}&=\{K:\mathcal H^aK=0\ (a<-1),\
        \mathcal H^{-1}K\text{ has no nonzero punctual subsheaf}\}.
 \end{split}
$$

For $C=C_0\times_{k_0}k$, a *perverse Weil sheaf* is a
Frobenius-equivariant object in the heart of this geometric t-structure,
with morphisms as in [sk-def-sf-weil-complexes].

These classes form a bounded t-structure. Its heart is abelian and
consists of the complexes in ordinary degrees $-1,0$ whose
$\mathcal H^0$ is punctual and whose $\mathcal H^{-1}$ has no punctual
subsheaf. In particular, a punctual sheaf in degree zero belongs to
the heart, and so does $(j_*M)[1]$ for a lisse sheaf $M$ on a dense
open $j:U\hookrightarrow C$, where $j_*$ is the ordinary direct image.
Over $k_0$, the perverse Weil sheaves form an abelian category, and
the forgetful functor to the geometric heart is exact and reflects
exactness.
