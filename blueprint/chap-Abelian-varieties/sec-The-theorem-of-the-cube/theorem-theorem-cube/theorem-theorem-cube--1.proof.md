+++
kind = "proof"
of = "theorem-theorem-cube--1"
order = 1486002
uses = []
+++
Put $\mathcal L=\mathcal M\otimes\mathcal N^{-1}$, let
$\pi:X\times Y\times Z\to Y\times Z$ be the projection, and let
$\sigma$ be its section through $x$. The hypotheses give local
generators of $\mathcal L$ over $X\times Y\times U$ and a global
generator $\gamma$ of $\sigma^*\mathcal L$.

Since $X$ is proper and geometrically integral,
$H^0(X,\mathcal O_X)=k$. Flat base change therefore identifies
$\Gamma(V,\mathcal O_{Y\times Z})$ with
$\Gamma(\pi^{-1}V,\mathcal O_{X\times Y\times Z})$ for affine opens
$V\subset Y\times Z$. These identifications extend to all opens by
the sheaf property; pullback along $\sigma$ is their inverse.

Choose the neighbourhoods $U_t$ in the hypothesis and put
$V_t=Y\times U_t$. They cover $Y\times Z$. Multiply each local
generator $e_t$ of $\mathcal L$ on $\pi^{-1}V_t$ by a unit pulled
back from $V_t$ so that $\sigma^*e_t=\gamma|_{V_t}$. On an overlap,
two normalized generators differ by a unit $w$. The preceding
identification writes $w=\pi^*a$ for a function $a$ on the overlap
in $Y\times Z$. Pulling back along $\sigma$ gives $a=1$, so $w=1$.
Thus the generators agree and glue to a global generator of
$\mathcal L$. This is the argument of
`AlgebraicGeometry.Scheme.Modules.exists_isFreeGenerator_top_of_comp_eq_id`.
It gives $\mathcal L\simeq\mathcal O$, and tensoring with
$\mathcal N$ gives $\mathcal M\simeq\mathcal N$.
