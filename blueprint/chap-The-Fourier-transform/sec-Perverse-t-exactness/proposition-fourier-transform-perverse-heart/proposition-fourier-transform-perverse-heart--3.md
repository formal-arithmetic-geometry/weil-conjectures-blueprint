+++
id = "proposition-fourier-transform-perverse-heart--3"
kind = "proposition"
title = "Restriction to curve perverse Weil complexes"
name_showing = false
order = 1260003
aliases = ["bp-r390-3"]
lean = []
uses = ["lemma-artin-schreier-character-sheaf", "definition-weil-structure", "definition-perverse-sheaves-curve"]
+++
The passage from a geometric exact equivalence to an exact equivalence
of perverse Weil sheaves is bypassed by the Lean route, which works
directly with Weil complexes.

For a nontrivial additive character
$\psi:k_0\to\overline{\mathbf Q}_\ell^\times$, where $k_0=\Fq$ and
$\ell\ne\operatorname{char}k_0$ is prime, $\operatorname{FT}_\psi$
restricts to an equivalence of the full subcategories of curve perverse
Weil complexes on the two dual affine lines. This categorical
restriction is used in Lean to preserve simple objects. A separate
assertion of exactness for abelian perverse hearts, or a passage through
the functor forgetting the Weil structure, is not supplied by these
declarations.
