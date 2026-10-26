+++
id = "lemma-weil-pbc-normalization-exact-sequence"
kind = "lemma"
title = "Normalization comparison exact sequence"
lean = ["AlgebraicGeometry.exists_mono_lowerShriek_constantModSheaf_lowerStar"]
order = 1488
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions"]
+++
Let $k$ be an algebraically closed field, $X$ a reduced curve over $k$, and
$\nu:X^\nu\to X$ a finite surjective morphism which is an isomorphism over a
dense open $V\subseteq X$ (for instance the normalization of $X$). Let
$j:U\hookrightarrow X$ be an open immersion and $j^\nu:U^\nu\hookrightarrow
X^\nu$ its pullback along $\nu$. Let $\Lambda$ be a commutative ring and
$\ell$ a prime with $\Lambda/\ell\Lambda$ finite, and write
$\underline{\Lambda/\ell}$ for the constant sheaf of $\Lambda$-modules. Then
there is a monomorphism

$$
\alpha:j_!\underline{\Lambda/\ell}\longrightarrow
\nu_*j^\nu_!\underline{\Lambda/\ell}
$$

whose cokernel $Q$ is constructible and restricts to zero on $V$. Thus

$$
0\longrightarrow j_!\underline{\Lambda/\ell}
\xrightarrow{\alpha}\nu_*j^\nu_!\underline{\Lambda/\ell}
\longrightarrow Q\longrightarrow0
$$

is exact, with $Q$ supported on the finite set $X\setminus V$.
