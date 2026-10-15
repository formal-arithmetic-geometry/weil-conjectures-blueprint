+++
kind = "proof"
of = "sk-prop-sf-existence"
uses = ["sk-lem-brown-hypotheses", "sk-prop-sf-comp-coherence"]
+++
For $N\in\Loc(\Dctf(Y,\Lambda))$, the functor

$$
\Loc(\Dctf(X,\Lambda))^{\mathrm{op}}\longrightarrow\Ab,\qquad
M\longmapsto\Hom(Rf_!M,N)
$$

is cohomological and sends direct sums to products ($Rf_!$ is exact and
preserves direct sums by [sk-prop-sf-comp-coherence]). By
[sk-lem-brown-hypotheses], Brown representability (Stacks, Tag 0A8F) gives a
representing object $f^!N$. The Yoneda lemma makes these objects into a right
adjoint, and a right adjoint of an exact functor of triangulated categories is
exact (Stacks, Tag 0A8G).

For direct sums, test the canonical map
$\bigoplus_\alpha f^!N_\alpha\to f^!(\bigoplus_\alpha N_\alpha)$ in
$\Loc(\Dctf(X,\Lambda))$ on a compact generator $G\in\Dctf(X,\Lambda)$ and its
shifts. Both $G$ and $Rf_!G\in\Dctf(Y,\Lambda)$ are compact, so adjunction
identifies the two Hom groups with $\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha)$. The
generators detect isomorphisms, which proves the assertion.
