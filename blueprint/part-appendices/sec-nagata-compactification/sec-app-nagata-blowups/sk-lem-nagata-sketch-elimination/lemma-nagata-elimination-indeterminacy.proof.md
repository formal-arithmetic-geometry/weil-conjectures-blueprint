+++
kind  = "proof"
of    = "lemma-nagata-elimination-indeterminacy"
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-composition-of-blowups-comparison", "def-nagata-qc-open-complement-ideal", "def-nagata-dense-compactification", "def-nagata-scheme-image-comparison", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-admissible-blowup-preserves-density", "thm-nagata-global-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-dense-flat-pullback", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-strict-transform-over-complement", "thm-nagata-composition-of-blowups", "thm-nagata-conrad-elimination"]
+++
Form the construction of [def-nagata-elimination-indeterminacy] and write
$X'=X^{\mathrm{el}}(q,U)$ and $Z'=Z^{\mathrm{el}}(q,U)$. The blow-up
$X'\to X$ is $U$-admissible, as recorded there. It remains to show that the
strict transform $q^{\mathrm{el}}\colon Z'\to X'$ is an open immersion.

Via $X'\cong\operatorname{Bl}_{\mathcal I}(X_1)$ over $X$, regard $W$ as an
open of $X'$ containing the inverse image $U'$ of $U$. The extension
$\widetilde s$ has graph $\Gamma\subseteq Z\times_XX'
=(Z\times_XX_1)\times_{X_1}X'$, which is closed and maps isomorphically
onto $W$. Since the support of $K$ is exactly $X\setminus U$, the open $U'$
is scheme-theoretically dense in $X'$
([lemma-nagata-admissible-blowup-preserves-density]), hence in $W$.

By [def-nagata-strict-transform], $Z'$ is the
scheme-theoretic closure in $Z\times_XX'$ of the part lying over $U'$,
which, as $q$ is an isomorphism over $U$, is the graph of $s$ over $U'$,
i.e. the part of $\Gamma$ over $U'$. This part is scheme-theoretically dense
in $\Gamma\cong W$, and $\Gamma$ is closed, so $Z'=\Gamma\cong W$ and
$q^{\mathrm{el}}\colon Z'\to X'$ is the open immersion $W\subseteq X'$.
