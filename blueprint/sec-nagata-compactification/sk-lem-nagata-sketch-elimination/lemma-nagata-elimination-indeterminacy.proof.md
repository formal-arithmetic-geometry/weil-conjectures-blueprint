+++
kind  = "proof"
of    = "lemma-nagata-elimination-indeterminacy"
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-composition-of-blowups-comparison", "def-nagata-constructible-closed-support", "def-nagata-dense-compactification", "def-nagata-qc-open-complement-ideal", "def-nagata-scheme-image-comparison", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "lemma-nagata-constructible-closed-support", "lemma-nagata-dense-flat-pullback", "lemma-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-strict-transform-over-complement", "thm-nagata-composition-of-blowups", "thm-nagata-conrad-elimination", "thm-nagata-global-blowup-proper"]
+++
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
