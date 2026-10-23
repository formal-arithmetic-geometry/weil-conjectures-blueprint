+++
kind = "proof"
of = "lem-weil-pbc-constructible-finite-pushforward-noetherian"
uses = ["lem-weil-pbc-constructible-finitely-presented", "lem-weil-pbc-constructible-noetherian-finite-selection", "lem-weil-pbc-normal-constant-generic"]
+++
*Step 1: the local model at a point.* For every geometric point $\bar x\to U$,
constructibility gives a finite separable extension $K/\kappa(x)$ and a
finitely generated $\Lambda$-module $M$ for which $C$ is constant with value $M$
over $\operatorname{Spec}K$. Let $Z\subset U$ be the reduced closure of $x$, let
$V\to Z$ be the normalization of $Z$ in $K$, and let
$\operatorname{Spec}K\to V$ be the generic inclusion. The scheme $V$ is
integral and normal with function field $K$; this is the classical
normalization of an integral scheme in a finite extension of its function
field (Stacks Project, Morphisms, Lemma 29.54.13, Tag
[035L](https://stacks.math.columbia.edu/tag/035L)).

*Step 2: the generic map.* The identification
$C|_{\operatorname{Spec}K}\cong\underline M$ is a map
$C|_{\operatorname{Spec}K}\to\underline M$, and
[lem-weil-pbc-normal-constant-generic], applied to the normal integral $V$ and
the inclusion $g:\operatorname{Spec}K\to V$ of its generic point, identifies
$g_*\underline M$ with $\underline M$. Hence that map adjoints to
$C|_V\to\underline M$, and adjoints again to a map

$$
 C\longrightarrow h_*\underline M,\qquad h:V\to U
$$

of sheaves on $U$, the morphism $h$ being the composite of the normalization
with $V\to Z\hookrightarrow U$. This is the step that the former pending note
recorded as unjustified: the justification is exactly the normality of $V$,
and no locally constant sheaf is extended across a boundary.

*Step 3: the stalk map at $\bar x$.* Choose a lift $\bar y$ of $\bar x$ to
$V$. The diagram

$$
\begin{array}{ccc}
C_{\bar x}&\xrightarrow{\ \sim\ }&(C|_V)_{\bar y}\\
\downarrow&&\downarrow\\
(h_*\underline M)_{\bar x}&\longrightarrow&\underline M_{\bar y}
\end{array}
$$

is commutative, and $\underline M_{\bar y}=M$, so the stalk map of Step 2 is
injective at $\bar x$.

*Step 4: the finite approximation of $h_*\underline M$.* The normalization map
is integral, not finite in general: writing its affine coordinate algebra as
the filtered union of its finite $\mathcal O_Z$-subalgebras, the induced
direct image is the filtered colimit of the corresponding finite pushforwards,

$$
 h_*\underline M=\varinjlim_i(h_i)_*\underline M,
$$

which over an etale finite-presentation object $W\to U$ is the section formula
$\varinjlim_i\underline M(W\times_UV_i)=\underline M(W\times_UV)$ applied to
the affine limit $V=\varprojlim_iV_i$.

*Step 5: factorization through one finite stage.* The map $C\to h_*\underline
M$ of Step 2 is a morphism from a constructible sheaf into a filtered colimit
of sheaves, so by [lem-weil-pbc-constructible-finitely-presented] it factors
through one stage: there are an index $i$ and a map $C\to(h_i)_*\underline M$
whose composite with the transition map is the given map. Hence $\bar x$
admits a finite pushforward $h_i:V_i\to U$, the morphism $V_i\to Z$ being
finite by construction, detecting its stalk.

*Step 6: finite selection.* For a finite ring $\Lambda$ the finite-selection
statement [lem-weil-pbc-constructible-noetherian-finite-selection] produces a
finite set of the maps of Step 5 whose joint map
$C\to\bigoplus_i(h_i)_*\underline{M_i}$ is a monomorphism. For a general
Noetherian ring $\Lambda$ the same argument applies: for every finite subfamily
the kernel of the joint map is a subsheaf of the constructible sheaf $C$, hence
constructible, so the locus of points where the joint map fails to be injective
on the geometric stalk is constructible; these loci have empty intersection
(each point is detected by the map of Step 5 built at that point), so by
compactness of the constructible topology finitely many subfamilies already have
empty intersection of failure loci, and their union gives a joint map injective
on every geometric stalk, hence a monomorphism by conservativity of geometric
stalks. This is the Noetherian construction of Stacks Project, Lemma 59.74.3
(Tag [09Z6](https://stacks.math.columbia.edu/tag/09Z6)).

*Remark (the Nagata case).* If $U$ is Nagata, for instance of finite type over
a field, the normalization $V\to Z$ is finite already, so Step 4 is
unnecessary and the embedding is produced by Steps 1 to 3 and 6 directly. This
is the case used in the applications below.
