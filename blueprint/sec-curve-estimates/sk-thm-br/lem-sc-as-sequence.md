+++
id = "lem-sc-as-sequence"
kind = "lemma"
title = "The Artin–Schreier sequence"
lean = ["AlgebraicGeometry.Scheme.artinSchreierSequence_shortExact", "AlgebraicGeometry.Scheme.constantZModIsoKernelGaArtinSchreier", "AlgebraicGeometry.Scheme.isLocallySurjective_gaArtinSchreier"]
order = 1389
uses = ["def-sc-curves"]
+++
Let $p$ be a prime and $X$ a scheme with $p=0$ in $\Gamma(X,\mathcal O_X)$
(for instance a curve over a field $k$ of characteristic $p$). The
sequence of etale sheaves on $X_{\Et}$

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\ \wp\ }\mathbf G_a\longrightarrow0,
\qquad \wp(x)=x^p-x,
$$

is exact; that is, $\wp$ is an epimorphism of etale sheaves and the
constant sheaf $\mathbf F_p$, mapped to $\mathbf G_a$ by $c\mapsto c\cdot1$,
is its kernel.
