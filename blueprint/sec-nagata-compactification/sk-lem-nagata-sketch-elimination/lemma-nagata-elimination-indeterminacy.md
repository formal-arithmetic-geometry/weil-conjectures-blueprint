+++
id = "lemma-nagata-elimination-indeterminacy"
kind = "lemma"
title = "Elimination of indeterminacy, [stacks-project]"
order = 229
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap"]
uses = ["cor-nagata-blowup-product-common-refinement", "cor-nagata-conrad-proper-target-extension", "def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-composition-of-blowups-comparison", "def-nagata-constructible-closed-support", "def-nagata-dense-compactification", "def-nagata-elimination-indeterminacy", "def-nagata-global-blowup", "def-nagata-qc-open-complement-ideal", "def-nagata-scheme-image-comparison", "def-nagata-strict-transform", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "lemma-nagata-constructible-closed-support", "lemma-nagata-dense-flat-pullback", "lemma-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent", "thm-nagata-composition-of-blowups", "thm-nagata-conrad-elimination", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be a quasi-compact open, and let
$q\colon Z\to X$ be separated and of finite type such that
$q^{-1}(U)\to U$ is an isomorphism. Then there is a $U$-admissible
blow-up $X'\to X$ such that the strict transform $Z'\to X'$ of $Z$ is an
open immersion.

## Proof

Fix an isomorphism $e_U\colon q^{-1}(U)\xrightarrow{\sim}U$ over $U$ (the
inverse of the given isomorphism) and form the construction of
[def-nagata-elimination-indeterminacy]; write $X'=X^{\mathrm{el}}(q,U)$ and
$Z'=Z^{\mathrm{el}}(q,U)$. The blow-up $X'\to X$ is $U$-admissible by
[lemma-nagata-admissible-blowup-comp], as recorded in
[def-nagata-elimination-indeterminacy]. It remains to show that the
strict transform $q^{\mathrm{el}}\colon Z'\to X'$ is an open immersion.

The quasi-domination $(W,\widetilde s)$ supplied by
[thm-nagata-conrad-elimination] pulls back along the domination
$X'\to\operatorname{Bl}_{\mathcal I}(X_1)$ of
[cor-nagata-blowup-product-common-refinement] to an open $W'\subseteq X'$
containing $U$ and a morphism $s'\colon W'\to Z_1$ extending $s$. Because
$Z_1\to X_1$ is separated, the graph $\Gamma_{s'}$ is closed in
$X'\times_{X_1}Z_1$ and $\Gamma_{s'}\cong W'$. Since
$X'\setminus V(\mathcal I\mathcal I_1)=U$, the open $U$ is
scheme-theoretically dense in $X'$, hence in $W'$.

By [lemma-nagata-strict-transform-closure-characterization], $Z'$ is the
scheme-theoretic closure in $X'\times_{X_1}Z_1$ of the part lying over
$X'\setminus V(\mathcal I\mathcal I_1)=U$, which is the graph of $s$. It is
therefore contained in the closed subscheme $\Gamma_{s'}\cong W'$. So $Z'$ is
a closed subscheme of $W'$ containing $U$ as a scheme-theoretically dense
open subscheme, whence $Z'=W'$ and $q^{\mathrm{el}}\colon Z'\to X'$ is the
open immersion $W'\subseteq X'$.
