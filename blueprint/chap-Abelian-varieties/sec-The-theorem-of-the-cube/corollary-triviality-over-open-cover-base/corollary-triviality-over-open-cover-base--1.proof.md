+++
kind = "proof"
of = "corollary-triviality-over-open-cover-base--1"
order = 1478002
uses = []
+++
Put $\mathcal L=\mathcal M\otimes\mathcal N^{-1}$, let
$\pi:X\times Y\times Z\to Y\times Z$ be the projection, and let
$\sigma:Y\times Z\to X\times Y\times Z$ be its section through $x$.
The hypotheses give local free generators of $\mathcal L$ over
$\pi^{-1}(Y\times U)$ and a global free generator $\gamma$ of
$\sigma^*\mathcal L$.

Since $X$ is proper and geometrically integral,
$H^0(X,\mathcal O_X)=k$. Flat base change gives an isomorphism
$$
\Gamma(V,\mathcal O_{Y\times Z})\longrightarrow
\Gamma(\pi^{-1}V,\mathcal O_{X\times Y\times Z})
$$
for every affine open $V$ of $Y\times Z$. The sheaf condition and
$\pi\circ\sigma=\id$ extend this to all opens $V$.

Multiply each local generator by a unit pulled back from $Y\times U$
so that its pullback along $\sigma$ agrees with $\gamma$. On an
overlap two such generators differ by a unit $w$. By the surjectivity
on sections just proved, write $w=\pi^*a$. Pulling back along $\sigma$
shows $a=1$, so the generators agree. They glue to a global free
generator of $\mathcal L$, as in
`AlgebraicGeometry.Scheme.Modules.exists_isFreeGenerator_top_of_comp_eq_id`.
Thus $\mathcal M\otimes\mathcal N^{-1}$ is trivial, and tensoring with
$\mathcal N$ gives $\mathcal M\simeq\mathcal N$.
