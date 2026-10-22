+++
id = "def-pd-degree-morphism"
kind = "definition"
title = "The constant integers sheaf and the degree morphism"
lean = ["AlgebraicGeometry.locallyConstantIntPresheaf", "AlgebraicGeometry.locallyConstantIntSheaf", "AlgebraicGeometry.picardDegreeMorphism", "AlgebraicGeometry.picardDegreeSubfunctor", "AlgebraicGeometry.range_picardFunctorDegree\u03b9", "AlgebraicGeometry.picardFunctorDegreeIsoSubfunctor", "AlgebraicGeometry.picardDegree"]
order = 849
uses = ["def-pc-fppf-site", "def-pc-picard-functor", "def-pc-picard-presheaf", "def-pc-subfunctor", "def-pd-fibrewise-degree", "def-sc-picard-functor", "lem-pd-degree-locally-constant"]
+++
Let $S$ be a scheme. The *constant sheaf* $\underline{\Z}$ on the fppf
site $(\mathit{Sch}/S)_{fppf}$ of [def-pc-fppf-site] is the presheaf whose
value on $T$ is the group of locally constant functions $T\to\Z$, with
restriction along $g:T'\to T$ given by composition with $g$. It is an fppf
sheaf: the members of an fppf covering $\{T_i\to T\}$ are open maps and jointly
surjective, so compatible locally constant functions on the $T_i$ come from a
unique function on $T$, and this function is locally constant.

Let now $f:X\to S$ be a morphism which is proper, flat and locally of finite
presentation, and let $\operatorname{Pic}_{X/S}$ be the
Picard functor. The *degree morphism*

$$
\deg:\operatorname{Pic}_{X/S}\longrightarrow\underline{\Z}
$$

is the morphism of fppf sheaves defined as follows. Let $T$ be an $S$-scheme,
$x\in\operatorname{Pic}_{X/S}(T)$ and $t\in T$. Since
$\operatorname{Pic}_{X/S}$ is the fppf sheafification of the
Picard presheaf, there are a flat morphism
$g:Z\to T$ locally of finite presentation, a point $z\in Z$ with $g(z)=t$ and
an invertible $\mathcal{O}_{X_Z}$-module $\mathcal{L}$ whose class in
$\operatorname{Pic}_{X/S}(Z)$ is the pullback $g^*x$; put
$\deg(x)(t):=\deg_Z(\mathcal{L})(z)$, the fibrewise degree of
[def-pd-fibrewise-degree]. This is independent of the choices: for a second
choice $(g',z',\mathcal{L}')$ pick a point $w$ of $Z\times_TZ'$ over $z$ and $z'$;
the pullbacks of $\mathcal{L}$ and $\mathcal{L}'$ to $X_{Z\times_TZ'}$ have the
same image in $\operatorname{Pic}_{X/S}$, so they become isomorphic after
pullback along an fppf covering of $Z\times_TZ'$, and evaluating at a point over
$w$ the two values agree by [lem-pd-degree-locally-constant](3). The function
$\deg(x):T\to\Z$ is locally constant by [lem-pd-degree-locally-constant](1),
as $g$ is open; for $h:T'\to T$ one has $\deg(h^*x)=\deg(x)\circ h$; and for
the class $x$ of an invertible module $\mathcal{L}$ on $X_T$ one has
$\deg(x)=\deg_T(\mathcal{L})$. So $\deg(x)\in\underline{\Z}(T)$ and $\deg$ is a
morphism of sheaves.

For $d\in\Z$ the subfunctor
$\operatorname{Pic}^d_{X/S}\subseteq\operatorname{Pic}_{X/S}$, in the sense of
[def-pc-subfunctor], consists of the classes whose degree function is
identically $d$. The *degree-zero part* of the Picard functor is

$$
\operatorname{Pic}^0_{X/S}:=\ker(\deg)\subseteq\operatorname{Pic}_{X/S} .
$$

If $S=\Spec(k)$ for a field $k$, these agree with the functors of
[def-sc-picard-functor] (with $X$ in place of $C$): the canonical morphism
from the fppf sheafification of the subpresheaf of classes of fibrewise
degree $d$ to $\operatorname{Pic}_{X/k}$ is a monomorphism whose image is
$\operatorname{Pic}^d_{X/k}$. Indeed, by [lem-pd-degree-locally-constant](4) an
invertible module $\mathcal{L}$ on $X_T$ has degree $d$ after pullback along
every $k$-morphism $\Spec(K)\to T$ from a field if and only if
$\deg_T(\mathcal{L})$ is identically $d$; sheafification preserves
monomorphisms, and membership in $\operatorname{Pic}^d_{X/k}$ is fppf local.
In particular $\operatorname{Pic}^0_{X/k}=\ker(\deg)$.
