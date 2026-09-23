+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-epsilon-direct-image-comparison"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-epsilon-direct-image-comparison"
order = 1709
uses = ["def-weil-pbc-epsilon-direct-image-comparison", "lemma-weil-pbc-epsilon-adjunction-equations-v1", "lemma-weil-pbc-epsilon-inverse-image-exact", "lemma-weil-pbc-epsilon-scheme-naturality"]
+++
The construction in Definition [def-weil-pbc-epsilon-direct-image-comparison] is a typed raw datum. Its theorem-valued naturality, comparison, descent, or coherence fields are isolated in this property lemma.

## Proof

The underived transformation is the adjoint of $f_*\eta^X$. Naturality of
$\eta^X$ proves naturality in $F$; the identity formula and the triangle
identities prove the identity and composition equations. Scheme naturality
identifies the two restrictions in the displayed equality
$f_{\mathrm{et},*}\epsilon_{X,*}=\epsilon_{Y,*}f_{\mathrm{proet},*}$ and
makes the construction compatible with Cartesian pullback.

For the derived map choose a bounded-below injective resolution
$L\to I^\bullet$ on $X_{\mathrm{et}}$, and then a bounded-below injective
resolution $\epsilon_X^{-1}I^\bullet\to J^\bullet$ on
$X_{\mathrm{proet}}$. Exactness of $\epsilon_X^{-1}$ and
$\epsilon_Y^{-1}$ identifies the two derived source representatives, and the
complex map

$$
\epsilon_Y^{-1}f_{\mathrm{et},*}I^\bullet
\xrightarrow{\delta_{f,I^\bullet}}
f_{\mathrm{proet},*}\epsilon_X^{-1}I^\bullet
\longrightarrow f_{\mathrm{proet},*}J^\bullet
$$

represents $D_f(L)$. Comparisons between two choices of either resolution
are unique up to homotopy; naturality of $\delta_f$ carries both comparison
homotopies to the target, so the localized map is independent of every
choice. The underived
identity, composition, and base-change equations persist after localization.
Thus $D_f(L)$ and all its stated coherence fields are well-defined.
