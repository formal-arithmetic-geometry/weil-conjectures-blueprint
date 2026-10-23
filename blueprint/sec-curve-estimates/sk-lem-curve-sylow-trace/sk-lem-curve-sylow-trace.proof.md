+++
kind = "proof"
of = "sk-lem-curve-sylow-trace"
uses = ["sk-prop-pe-finite-local-systems", "sk-lem-curve-finite-support", "sk-lem-curve-dense-open", "sk-lem-curve-normalization", "sk-lem-pbc-finite", "sk-thm-br"]
+++
By [sk-prop-pe-finite-local-systems], $G$ is the pullback of a finite étale
local system, which corresponds to a finite continuous representation of the
fundamental group. Let $H$ be the finite image of this representation, choose
an $r$-Sylow subgroup $P$, and take the cover associated to its inverse image
in the fundamental group. Its degree is $[H:P]$, prime to $r$, and the
restricted action factors through $P$. The augmentation ideal of
$\mathbf F_r[P]$ is nilpotent, so the simple modules of the finite $r$-group
$P$ are trivial of dimension one, and a composition series gives the required
filtration (Stacks, Tag 0A3R).

The unit $G\to v_*v^*G$ is the diagonal on a fibre, and the trace map
$\operatorname{Tr}\colon v_*v^*G\to G$ adds the $d$ entries of a fibre. Hence
the composite is multiplication by $d$, which is invertible on an
$\mathbf F_r$-sheaf, and $d^{-1}\operatorname{Tr}$ is a retraction.

*Application to $j_!G$.* To apply this to $j_!G$ on a reduced curve $C$, take
for $U$ a dense smooth open on which $G$ is locally constant. Normalizing $C$
in the finite extensions of function fields defined by $V$ gives a finite
morphism $\bar v\colon Y\to C$ with $V$ the inverse image of $U$, and an open
immersion $j'\colon V\hookrightarrow Y$. The cartesian square formed by these
maps and the stalk formula for finite morphisms
([sk-lem-curve-finite-support]) give

$$
j_!v_*v^*G=\bar v_*j'_!v^*G,
$$

which is also the finite open–closed exchange of (Stacks, Tag 0GJ1). If $C$ is
proper, $Y$ is proper; if $C$ is affine, $Y$ is affine.

The filtration of $v^*G$, exactness of $j'_!$, and the calculation for
constant sheaves extended by zero ([sk-lem-curve-dense-open],
[sk-lem-curve-normalization]) therefore give the assertions $(C_1)$–$(C_8)$
of [def-weil-pbc-eight-curve-assertions] for $j'_!v^*G$. Exactness of $\bar v_*$ passes them to $j_!v_*v^*G$, and the
trace splitting passes them to its direct summand $j_!G$. For invariance
under field extension, the splitting maps commute with ground-field
extension, so the isomorphism for the larger sheaf is block diagonal for the
induced decomposition. This is the argument of (Stacks, Tag 03SD).

If $C$ is not equidimensional, first choose a dense open which is smooth and
is the disjoint union of the regular loci of the one-dimensional components
and the isolated points. The isolated points have exact sections. Treat each
connected one-dimensional piece as above; finite direct sums preserve all the
assertions.
