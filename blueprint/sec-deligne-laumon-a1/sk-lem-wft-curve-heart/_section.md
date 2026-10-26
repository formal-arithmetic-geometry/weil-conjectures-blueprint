+++
id = "sk-lem-wft-curve-heart"
kind = "lemma"
title = "Perverse sheaves on a curve"
order = 3974
uses = ["sk-def-sf-weil-complexes", "sk-lem-coefficient-heart", "sk-p-real-integral"]
lean = ["AlgebraicGeometry.WeilComplex.IsCurvePerverseUpper", "AlgebraicGeometry.WeilComplex.IsCurvePerverseLower", "AlgebraicGeometry.WeilComplex.IsCurvePerverse"]
tags = ["sketch"]
+++
Let $C_0$ be a smooth curve over $k_0$ and $C=C_0\times_{k_0}k$. A
Weil sheaf on $C_0$ is called *punctual* if its support is a finite
set of closed points. On the triangulated category of Weil complexes
on $C_0$ ([sk-def-sf-weil-complexes]) we define two classes directly
by the cohomology Weil sheaves and their supports:

$$
 \begin{split}
 {}^pD^{\le0}&=\{K:\mathcal H^aK=0\ (a>0),\
                         \mathcal H^0K\text{ is punctual}\},\\
 {}^pD^{\ge0}&=\{K:\mathcal H^aK=0\ (a<-1),\
        \mathcal H^{-1}K\text{ has no nonzero punctual Weil subsheaf}\},
 \end{split}
$$

and ${}^pD^{\le n}={}^pD^{\le0}[-n]$,
${}^pD^{\ge n}={}^pD^{\ge0}[-n]$. A *perverse Weil sheaf* on $C_0$ is
a Weil complex lying in both classes. The same conditions on
$D^b_c(C_{\mathrm{pro\acute et}},\Qlb)$, for a smooth curve $C$ over
any perfect field, define the geometric classes and the geometric
heart.

These classes form a bounded t-structure; in particular
${}^pD^{\ge0}$ is the right orthogonal of ${}^pD^{\le-1}$. Its heart is
abelian and consists of the complexes in ordinary degrees $-1,0$ whose
$\mathcal H^0$ is punctual and whose $\mathcal H^{-1}$ has no punctual
subsheaf. In particular, a punctual sheaf in degree zero belongs to
the heart, and so does $(j_*M)[1]$ for a lisse sheaf $M$ on a dense
open $j:U\hookrightarrow C$, where $j_*$ is the ordinary direct image.
