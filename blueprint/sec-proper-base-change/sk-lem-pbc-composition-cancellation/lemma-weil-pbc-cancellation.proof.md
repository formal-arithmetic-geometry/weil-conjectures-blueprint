+++
kind  = "proof"
of    = "lemma-weil-pbc-cancellation"
uses = ["lem-weil-pbc-retract-supplied", "lem-weil-pbc-vanishing-descends-retract", "lem-weil-pbc-grothendieck-spectral-sequence", "lemma-weil-pbc-property-iff-acyclicity"]
+++
Since $\Lambda$ is torsion, every sheaf of $\Lambda$-modules is torsion.

(1) Fix a cartesian square with $h$ on the right and $c:Z'\to Z$ at the bottom;
write $Y'=Y\times_ZZ'$, $X'=X\times_ZZ'$, $b:Y'\to Y$, $a:X'\to X$ and $f'$, $h'$
for the base-changed maps. Let $I$ be an injective sheaf of $\Lambda$-modules on
$Y$. Choose a monomorphism $f^{-1}I\hookrightarrow J$ with $J$ injective on $X$.
By [lem-weil-pbc-retract-supplied] ($f$ is surjective) the adjoint map
$s:I\to f_*J$ is a monomorphism, so by injectivity of $I$ it has a retraction
$r$ with $rs=\mathrm{id}_I$. Torsion base change for $f$ implies injective
acyclicity of $f$ and, at the injective sheaf $J$, that the underived exchange
$b^{-1}f_*J\to f'_*a^{-1}J$ is an isomorphism
([lemma-weil-pbc-property-iff-acyclicity]). Thus $a^{-1}J$ is $f'_*$-acyclic,
and the Grothendieck spectral sequence
[lem-weil-pbc-grothendieck-spectral-sequence] for $X'\xrightarrow{f'}Y'\xrightarrow{h'}Z'$
at $a^{-1}J$ collapses to its row $q=0$ and gives

$$
 R^qh'_*(b^{-1}f_*J)\cong R^qh'_*(f'_*a^{-1}J)\cong R^q(h'f')_*a^{-1}J=0
 \qquad(q>0)
$$

by injective acyclicity of $hf$. The sheaf $b^{-1}I$ is a retract of
$b^{-1}f_*J$ via $b^{-1}s$ and $b^{-1}r$, so
[lem-weil-pbc-vanishing-descends-retract] gives $R^qh'_*b^{-1}I=0$ for $q>0$.

(2) By (1), applied with the injective acyclicity of $hf$ implied by its torsion
base change, $h$ has injective acyclicity. Moreover the underived exchange
morphism $c^{-1}h_*G\to h'_*b^{-1}G$ is an isomorphism for every sheaf $G$ of
$\Lambda$-modules on $Y$: at $G=f_*J$ with $J$ injective this follows from the
vertical pasting of the exchange morphisms of $f$ and $hf$, both isomorphisms at
$J$; a general $G$ is the kernel of a map $f_*J_1\to f_*J_2$ of such sheaves
(the unit $G\to f_*f^{-1}G$ is a monomorphism since $f$ is surjective), and both
sides of the exchange are left exact. Injective acyclicity together with the
underived exchange isomorphism gives torsion base change for $h$
([lemma-weil-pbc-property-iff-acyclicity]). This is Stacks Project, Tag 0A4C.
