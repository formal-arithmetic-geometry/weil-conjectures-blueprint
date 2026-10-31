+++
kind  = "proof"
of    = "thm-sf-dual-perfect"
+++
Step 1: the definition. By [def-pod-conventions],
$\mathbb D_XK=R\mathcal Hom_X(K,\omega_{X,\Lambda})$ with
$\omega_{X,\Lambda}=Ra_X^!\Lambda$, and
$K^\vee=R\mathcal Hom_X(K,\Lambda_X)$.

Step 2: the smooth purity input. The smooth dualizing-complex
identification of [cor-pur-finite-stage-smooth-dualizing-complex]
(at the finite stage $A=A_{E,n}$) and its transport
[cor-pur-adic-and-rational-smooth-dualizing-complexes] (at the
$\mathcal O_E$-, $E$- and $\overline{\mathbf Q}_\ell$-stages) provide the
canonical orientation

$$
\eta_X:\omega_{X,\Lambda}\xrightarrow{\ \sim\ }\Lambda_X(d)[2d],
$$

which at the finite stage is the case $f=a_X$ of an orientation datum in
the sense of [def-sf-orientation]. Its compatibility with finite reduction
$A_{E,n}\to A_{E,m}$ is [thm-pur-finite-reduction-of-purity]; at the
$\mathcal O_E$-, $E$- and $\overline{\mathbf Q}_\ell$-stages it is obtained by
transport from the finite stages, by inverting $\ell$ and by extension of
scalars from a finite $E$ ([cor-pur-adic-and-rational-smooth-dualizing-complexes]);
and it is compatible with shifts.

Step 3: substitution and interchange. Substituting $\eta_X$ into the
internal Hom and using the shift of the second variable,

$$
\mathbb D_XK\cong R\mathcal Hom_X\bigl(K,\Lambda_X(d)[2d]\bigr)
\cong\bigl(R\mathcal Hom_X(K,\Lambda_X(d))\bigr)[2d]
\cong K^\vee(d)[2d],
$$

the second isomorphism being the shift axiom of the derived internal Hom
of [def-weil-derived-pullback-tensor-hom], the third being
[lem-sf-twist-interchange] with $m=d$ (its hypothesis is the
perfectness of $K$ over $\Lambda_X$).

Step 4: canonicality and compatibilities. The composite is canonical
because its ingredients are: the orientation is the canonical one of the
purity chapter, and the twist interchange and the shift identification
are canonical maps of the tensor–internal-Hom adjunction (natural in
$K$; on the generators $K=\Lambda_X^r$ they are the coordinate
isomorphisms; the shift index is the constant $2d$). Naturality in $K$
and compatibility with finite reduction, scalar extension and shifts
follow from the corresponding properties of $\eta_X$ recorded in
[cor-pur-finite-stage-smooth-dualizing-complex],
[thm-pur-finite-reduction-of-purity] and
[cor-pur-adic-and-rational-smooth-dualizing-complexes], and of the
derived tensor and internal Hom recorded in
[def-weil-derived-pullback-tensor-hom]. The compatibility with the
canonical evaluation is the compatibility of the twist interchange with
the tensor–internal-Hom adjunction of
[def-weil-derived-pullback-tensor-hom]: the evaluation is the counit,
and the interchange carries the counit for $K\otimes^L\Lambda_X(d)$ to
the counit for $K$ tensored with the identity of $\Lambda_X(d)$, after
unwinding $K^\vee(d)\otimes\Lambda_X(d)$ through the associativity and
commutativity coherence of the derived tensor product.

Step 5: biduality and the anti-equivalence. By [prop-sf-dualizable],
$K^\vee$ is perfect and the evaluation $K\otimes^L_{\Lambda_X}K^\vee\to\Lambda_X$
is defined. Choose locally a bounded complex $P^\bullet$ of finite
projective $\Lambda_X$-modules with a quasi-isomorphism $P^\bullet\to K$.
By [prop-sf-dualizable-hom] (with $M=\Lambda_X$) the dual $K^\vee$ is
represented by $P^{\bullet\vee}$, again bounded with finite projective
terms, and applying this once more $K^{\vee\vee}$ is represented by
$P^{\bullet\vee\vee}$; the canonical map $K\to K^{\vee\vee}$ is then
termwise the double-dual map $P^j\to P^{j\vee\vee}$, an isomorphism by
[lem-sf-hom-finite-projective], compatible with the differentials,
so $K\to K^{\vee\vee}$ is an isomorphism (the statement being local on
the site). Applying Step 3 twice,
$\mathbb D_X\mathbb D_XK\cong\bigl(K^\vee(d)[2d]\bigr)^\vee(d)[2d]\cong K^{\vee\vee}$,
where $\bigl(K^\vee(d)[2d]\bigr)^\vee\cong R\mathcal Hom_X(K^\vee,\Lambda_X(-d)[-2d])\cong K^{\vee\vee}(-d)[-2d]$
by the tensor–internal-Hom adjunction of
[def-weil-derived-pullback-tensor-hom] (moving the invertible twist
$\Lambda_X(d)$ of the first variable to $\Lambda_X(-d)$ in the second)
and [lem-sf-twist-interchange] with $m=-d$ applied to the perfect
complex $K^\vee$; and
under this identification the biduality map is $K\to K^{\vee\vee}$.
Hence $K\mapsto\mathbb D_XK\cong K^\vee(d)[2d]$ preserves perfect
objects and is its own quasi-inverse on them, i.e. an anti-equivalence of
the perfect objects.
