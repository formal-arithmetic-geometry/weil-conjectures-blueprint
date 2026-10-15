+++
kind = "proof"
of = "sk-lem-brown-hypotheses"
+++
The ambient category is the derived category of a Grothendieck abelian category of module sheaves, hence
locally small, and so is its full subcategory $\Loc(\Dctf(-,\Lambda))$. It has direct sums by definition, so
idempotents split (Stacks, Tag 05QW) ([det-brown-hypotheses-ambient]). Constructibility and finite Tor
amplitude are preserved by shifts, cones and direct summands. For essential smallness: the admissible
constructible hearts have a set of representatives, and bounded complexes with such cohomology are obtained
by finitely many extensions classified by ambient Hom sets; the full subcategory with finite Tor amplitude
is contained in this set. The truncations used here are those of the ambient category
([det-brown-hypotheses-small]).

Compactness for finite $A$ is [sk-prop-ctf-finite-compact]. For $E$ and $\Qlb$ it is
[sk-thm-constructible-compactness], and for $\mathcal O_E$ it is [sk-prop-int-compactness]; in the integral and
rational cases $\Dctf=\Dbc$. Finally, suppose $K\in\Loc(\Dctf(X,\Lambda))$ receives no nonzero maps from shifts
of objects of a small skeleton. The objects $M$ with $\Hom(M[n],K)=0$ for all $n$ form a localizing
subcategory containing $\Dctf$, hence containing $K$. Thus $\mathrm{id}_K=0$, and the skeleton generates
([det-brown-hypotheses-generation]).

For integral coefficients, compactness is proved in the integral chapter, and only the structural,
Ext-continuity and compactness results of that chapter are used here. Their proofs use local coefficient
models, sections with closed support and torsion cohomological bounds; since $f^!$ and open direct image play
no role in them, the forward reference is not circular.
