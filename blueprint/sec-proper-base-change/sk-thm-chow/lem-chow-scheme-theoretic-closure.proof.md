+++
kind  = "proof"
of    = "lem-chow-scheme-theoretic-closure"
uses = ["def-nagata-scheme-image-factor", "lemma-nagata-immersion-open-in-scheme-image"]
+++
By construction $X^{*}\to X$ is a closed immersion, and $U$ factors through it.
Its image is a closed subset containing the dense subset $U$, hence is all of
$X$, so $X^{*}\to X$ is surjective. The quasi-coherent ideal sheaf of $X^{*}$
is $\ker(\mathcal O_X\to u_*\mathcal O_U)$, whose restriction to $U$ is
$\ker(\mathcal O_U\to\mathcal O_U)=0$; hence $X^{*}\cap U=U$ and $X^{*}\to X$
is an isomorphism over $U$. This proves (1). Since formation of the
scheme-theoretic image commutes with restriction to opens, the
scheme-theoretic image of $U\to X^{*}$ is $X^{*}$, which is (2). For (3), each
$U_i^{*}$ is a closed subscheme of the affine scheme $U_i$, hence affine, and
$U_1^{*}\cap\dots\cap U_m^{*}=X^{*}\cap U=U$.
