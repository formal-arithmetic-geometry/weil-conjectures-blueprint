+++
kind  = "proof"
of    = "lemma-weil-pbc-normalization-exact-sequence"
uses = ["def-weil-pbc-finite-open-comparison", "lemma-weil-pbc-finite-pushforward-extension-zero", "lem-weil-pbc-finite-pushforward-open-quotient-constant", "lem-weil-pbc-normalization-comparison-on-iso-locus", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $v:U^\nu\to U$ be the base change of $\nu$; it is surjective because
$\nu$ is. Define $\alpha$ as the composite

$$
j_!\underline{\Lambda/\ell}
\xrightarrow{j_!\eta}
j_!v_*v^{-1}\underline{\Lambda/\ell}\cong j_!v_*\underline{\Lambda/\ell}
\xrightarrow{\beta_{\nu,j}}
\nu_*j^\nu_!\underline{\Lambda/\ell},
$$

where $\eta$ is the unit of $v^{-1}\dashv v_*$, the middle isomorphism is the
identification of the pullback of a constant sheaf with the constant sheaf,
and $\beta_{\nu,j}$ is the finite-open comparison map of
[def-weil-pbc-finite-open-comparison]. Since $v$ is surjective, $v^{-1}$ is
faithful and $\eta$ is a monomorphism. Extension by zero $j_!$ is exact, so
$j_!\eta$ is a monomorphism, and $\beta_{\nu,j}$ is an isomorphism by
[lemma-weil-pbc-finite-pushforward-extension-zero]. Hence $\alpha$ is a
monomorphism.

The source $j_!\underline{\Lambda/\ell}$ is constructible (constant with
finite stalks on $U$ and zero outside), and so is the target by
[lem-weil-pbc-finite-pushforward-open-quotient-constant]; therefore the
cokernel $Q$ of $\alpha$ is constructible. Over $V$ the restrictions of the
source and the target are isomorphic
([lem-weil-pbc-normalization-comparison-on-iso-locus]), so at every geometric
point of $V$ the stalk of $\alpha$ is an injective map between finite sets of
the same cardinality, hence bijective. By conservativity of geometric stalks
([lemma-weil-pbc-geometric-stalk-conservative]) the restriction of $\alpha$
to $V$ is an isomorphism, and $Q$ restricts to zero on $V$. Finally,
$X\setminus V$ is a closed subset containing no generic point of $X$ (as $V$
is dense), so in the curve $X$ it is a finite set of closed points.
