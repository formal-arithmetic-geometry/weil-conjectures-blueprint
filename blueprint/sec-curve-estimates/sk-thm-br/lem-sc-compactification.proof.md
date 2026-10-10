+++
kind  = "proof"
of    = "lem-sc-compactification"
+++
By [lem-sc-curves-quasi-projective] there is a locally closed
immersion $i:C\hookrightarrow\mathbf P^N_k$. Let $X$ be the
scheme-theoretic closure of $i(C)$. By the definition of a locally
closed immersion, $C\hookrightarrow X$ is a dense open immersion.
The scheme $X$ is a closed subscheme of the proper scheme
$\mathbf P^N_k$, hence proper over $k$, and $\dim X=1$. The complement
$X\setminus C$ is a closed subset of dimension at most zero, hence
a finite set of closed points ([lem-sc-dim0-finite]). Let
$\nu:\overline C:=X^{\nu}\to X$ be the normalization in
$k(X)=k(C)$ ([def-sc-normalization]); by
[lem-sc-normalization-properties] it is finite (so
$\overline C$ is proper of dimension one) and an isomorphism over
the normal locus of $X$. Since $C$ is smooth it is normal
([lem-sc-smooth-normal]) and contained in the normal locus of
$X$, so the induced map $C\to\overline C$ is an open immersion;
its complement is $\nu^{-1}(X\setminus C)$, the preimage of a
finite set under a finite morphism, hence finite. Finally,
$\overline C$ is smooth over the perfect field $k$
by [lem-sc-normalization-properties](c).
