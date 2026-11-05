+++
kind = "proof"
of = "lemma-scheme-frobenius-geometric-frobenius--2"
order = 953005
uses = ["definition-weil-structure", "definition-frobenius-correspondences-their-operators"]
+++
Induct on $m$. At $m=0$, both morphisms are the canonical identification
$(\operatorname{id}_X)^*K\to K$, after removing an identity morphism.
For the successor step, both constructions use the composite

$$
\Phi_{m+1}^*K\simeq\Phi^*\Phi_m^*K
\xrightarrow{\Phi^*\psi_m}\Phi^*K\xrightarrow{\psi}K.
$$

Taking the underlying morphism of a composite or a pulled-back isomorphism
commutes with these operations. The induction hypothesis therefore identifies
the two composites.
