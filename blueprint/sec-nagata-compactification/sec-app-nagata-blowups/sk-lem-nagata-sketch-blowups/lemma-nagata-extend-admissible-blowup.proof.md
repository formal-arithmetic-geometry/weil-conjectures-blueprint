+++
kind  = "proof"
of    = "lemma-nagata-extend-admissible-blowup"
uses = ["def-nagata-qc-open-complement-ideal", "def-nagata-invertible-ideal", "def-nagata-finite-type-ideal-extension", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-dense-flat-pullback", "lemma-nagata-finite-type-ideal-extension-exists", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
By [lemma-nagata-finite-type-ideal-extension-exists], the ideal
$\mathcal I_X(\mathcal J)$ is finite type, restricts to $\mathcal J$ on
$W$, and restricts to the unit ideal on $U$. Its blow-up is therefore
$U$-admissible. The open immersion $W\to X$ is flat, so
[thm-nagata-blowup-flat-base-change] identifies the pullback of the
constructed blow-up with $\operatorname{Bl}_{\mathcal J}(W)$. On an
affine chart, that comparison is induced degreewise by the canonical map
from the pullback of the Rees algebra to the Rees algebra of the restricted
ideal; it sends every standard chart generator to itself. Hence the local
comparisons commute with restriction to basic overlaps and glue to the
stated canonical isomorphism. Over $U\cap W$ both ideals are the unit
ideal, so the same formula is the selected identity of the two trivial
blow-ups. This also verifies compatibility with the chosen admissibility
isomorphism.
