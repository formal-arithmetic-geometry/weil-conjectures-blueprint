+++
id = "lem-chow-scheme-theoretic-closure"
kind = "lemma"
title = "Scheme-theoretic closure of a dense open"
order = 1052
lean = ["AlgebraicGeometry.Scheme.Opens.iInf_preimage_imageι", "AlgebraicGeometry.Scheme.Opens.iSup_preimage_imageι_eq_top", "AlgebraicGeometry.Scheme.Opens.isAffineOpen_preimage_imageι", "AlgebraicGeometry.Scheme.Opens.isIso_morphismRestrict_imageι", "AlgebraicGeometry.Scheme.Opens.isSchemeTheoreticallyDominant_preimage_imageι", "AlgebraicGeometry.Scheme.Opens.surjective_imageι_ι"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $X$ be a scheme, let $U\subseteq X$ be an open subscheme and let
$X^{*}\subseteq X$ be the scheme-theoretic image of the inclusion
$u\colon U\to X$. Assume that $u$ is quasi-compact. Then:

1. $X^{*}\to X$ is a closed immersion which is an isomorphism over $U$; if
$U$ is dense in $X$, it is surjective;
1. $U=X^{*}\cap U$ is a scheme-theoretically dense open subscheme of $X^{*}$.

Moreover, without assuming $u$ quasi-compact, for opens of $X$ and their
traces $V^{*}:=X^{*}\cap V$ on $X^{*}$:

3. if $V\subseteq X$ is an affine open, then $V^{*}$ is affine;
4. if the opens $V_i$ cover $X$, then the $V_i^{*}$ cover $X^{*}$;
5. if $V_1,\dots,V_m$ are finitely many opens with
$V_1\cap\dots\cap V_m=U$, then $V_1^{*}\cap\dots\cap V_m^{*}=X^{*}\cap U$.

In particular, if $X=U_1\cup\dots\cup U_m$ is a finite affine open covering
with $U=U_1\cap\dots\cap U_m$, then the opens $U_i^{*}$ are affine, cover
$X^{*}$, and satisfy $U_1^{*}\cap\dots\cap U_m^{*}=U$.

## Proof

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
