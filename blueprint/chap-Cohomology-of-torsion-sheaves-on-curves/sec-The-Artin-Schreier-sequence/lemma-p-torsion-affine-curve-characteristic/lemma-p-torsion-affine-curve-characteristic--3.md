+++
id = "lemma-p-torsion-affine-curve-characteristic--3"
kind = "lemma"
title = "Exactness of the Artin–Schreier sequence"
order = 1590005
aliases = ["bp-r495-3"]
lean = ["AlgebraicGeometry.Scheme.artinSchreierSequence_shortExact", "AlgebraicGeometry.Scheme.constantZModIsoKernelGaArtinSchreier"]
+++
Let $X$ be a scheme and $p$ a prime such that
$p=0$ in $\Gamma(X,\mathcal O_X)$. On $X_{\acute{e}t}$, put
$\varphi(a)=a^p$ and $K=\ker(\varphi-1:\mathbf G_a\to\mathbf G_a)$.
The sequence

$$
0\longrightarrow K\longrightarrow\mathbf G_a
\xrightarrow{\varphi-1}\mathbf G_a\longrightarrow0
$$

is short exact, and the map from the constant sheaf $\mathbf F_p$ to
$K$ is an isomorphism. Thus this is the Artin–Schreier sequence
$0\to\mathbf F_p\to\mathbf G_a\to\mathbf G_a\to0$.
