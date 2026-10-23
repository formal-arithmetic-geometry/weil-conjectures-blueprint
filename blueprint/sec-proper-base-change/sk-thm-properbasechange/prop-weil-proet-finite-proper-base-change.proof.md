+++
kind  = "proof"
of    = "prop-weil-proet-finite-proper-base-change"
+++
View $F$ as the complex $F[0]$; its only cohomology sheaf is the torsion sheaf
$F$, so $F[0]$ has torsion cohomology. [thm-weil-pbc-bounded-below] applied to
$K=F[0]$ makes the derived exchange morphism $\Ex_{\square,F[0]}$ an
isomorphism in $\Dplus(Y'_{\Et})$; by [def-weil-pbc-derived-exchange] that
morphism for a complex concentrated in degree zero is the exchange morphism
$\Ex_{\square,F}$ of the sheaf $F$, giving the assertion.

The exchange morphisms $\Ex_{\square,F}$ are the components at $F[0]$ of the
natural transformation $\Ex_\square$, hence natural in $F$. For an identity
square the derived exchange morphism is the identity, since the units and
counits of the identity adjunctions are identities, and the derived
exchange morphism of a horizontally or vertically pasted square is the
composite of those of the two squares
[lemma-weil-pbc-derived-exchange-coherence]; evaluating at $F[0]$ gives the
remaining assertions.
