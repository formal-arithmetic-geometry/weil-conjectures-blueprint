+++
id = "det-pe-weak-contractible-equivalences"
kind = "lemma"
title = "Equivalent forms of weak contractibility"
lean = ["CategoryTheory.GrothendieckTopology.IsWeaklyContractible", "CategoryTheory.Sheaf.isLocallySurjective_iff_epi"]
order = 974
uses = ["det-pe-topos-functoriality-site", "det-pe-wcb-projective"]
+++
Let $W$ be an object of $X_{\mathrm{proét}}$ with representable sheaf
$h_W=\Hom_X(-,W)$ ([det-pe-topos-functoriality-site]). The following are equivalent:

1. every epimorphism of sheaves of sets $F\to h_W$ has a section;
2. $h_W$ is projective in $\Sh(X_{\mathrm{proét}})$: for every epimorphism $F\to G$ and every
   map $h_W\to G$ there is a lift $h_W\to F$;
3. for every epimorphism of sheaves $F\to G$ the map $F(W)\to G(W)$ is surjective.

An object satisfying these conditions is called *weakly contractible*. Every affine
$W=\operatorname{Spec}D$ with $D$ w-contractible is weakly contractible
([det-pe-wcb-projective]).
