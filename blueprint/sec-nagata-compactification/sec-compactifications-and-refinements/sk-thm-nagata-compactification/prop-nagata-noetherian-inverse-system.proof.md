+++
kind  = "proof"
of    = "prop-nagata-noetherian-inverse-system"
uses = ["lemma-nagata-noetherian-inverse-system-affine", "pqf-lem-limit-qc-open-descends"]
+++
By quasi-compactness, $S=V_1\cup\dots\cup V_n$ for finitely many affine
opens $V_k$. We show by induction on $m$ that the open
$S_{\leq m}=V_1\cup\dots\cup V_m$ admits a Noetherian approximation; the
case $m=n$ is the claim. The empty open is affine, and affine schemes
admit Noetherian approximations by
[lemma-nagata-noetherian-inverse-system-affine]. For the induction step
([Stacks, Tag 07RN](https://stacks.math.columbia.edu/tag/07RN)) put $X=S_{\leq m+1}$, $U=S_{\leq m}$ and $V=V_{m+1}$,
so that $X=U\cup V$ is quasi-separated, $U$ is quasi-compact with a
Noetherian approximation $U=\varprojlim_{i}U_i$, and $V$ is affine.

*Descending the overlap.* By quasi-separatedness $W=U\cap V$ is
quasi-compact. By [pqf-lem-limit-qc-open-descends] there are an index
$i_0$ and a quasi-compact open $W_{i_0}\subseteq U_{i_0}$ with preimage
$W$; for $j\geq i_0$ let $W_j\subseteq U_j$ be its preimage, so that
$W=\varprojlim_{j\geq i_0}W_j$ and each $W_j$ is quasi-compact and
Noetherian. Since $W$ is a quasi-compact open of the affine $V$, choose
$b_1,\dots,b_n\in\Gamma(V,\mathcal O)$ with
$W=\bigcup_l D(b_l)$.

*Stages.* A stage $T$ consists of an index $j\geq i_0$, sections
$r_l\in\Gamma(W_j,\mathcal O)$ restricting to $b_l|_W$ whose basic opens
$D(r_l)$ are affine and cover $W_j$, and a finitely generated
$\mathbf Z$-subalgebra $A_T$ of the fibre product
$\Gamma(V,\mathcal O)\times_{\Gamma(W,\mathcal O)}\Gamma(W_j,\mathcal O)$
containing the pairs $(b_l,r_l)$ and such that every section over
$D(r_l)$ is, up to a power of $r_l$, the restriction of the second
component of an element of $A_T$. A morphism of stages is a morphism of
indices compatible with the $r_l$ and the algebras. The last condition
makes $\Gamma(D(r_l),\mathcal O)$ the localization of $A_T$ at
$(b_l,r_l)$, so the second projection induces an open immersion
$W_j\to\operatorname{Spec}A_T$ onto $\bigcup_l D(b_l,r_l)$ (Stacks,
Tags 01Z7, 01Z9). The stages form a cofiltered category, and the functor
$T\mapsto j$ to the indices $j\geq i_0$ is initial: lifts $r_l$ exist at
some index because $W=\varprojlim W_j$, two lifts agree further down,
and the generation condition is achieved by adjoining finitely many
elements, the sections over the affine $D(r_l)$ of the Noetherian $W_j$
being a finitely generated $\mathbf Z$-algebra.

*The extended system.* To a stage $T$ attach the scheme $X_T$ obtained by
gluing $U_j$ and $\operatorname{Spec}A_T$ along the open $W_j$. It is
covered by two schemes of finite type over $\mathbf Z$, hence is of finite
type over $\mathbf Z$, and the transition morphisms are affine, since they
restrict to the affine morphisms $U_{j'}\to U_j$ and
$\operatorname{Spec}A_{T'}\to\operatorname{Spec}A_T$ over the two charts.
The projection $U\to U_j$ and the morphism
$V\to\operatorname{Spec}\Gamma(V,\mathcal O)\to\operatorname{Spec}A_T$
given by the first projection agree on $W$, so they glue to compatible
morphisms $X\to X_T$.

*The limit property.* A cone over a cofiltered system of schemes is a limit
cone as soon as its restrictions over the members of an open cover of one
stage, and over their pairwise intersections, are limit cones. Fix a stage
$T_0$ and use the cover of $X_{T_0}$ by $U_{j_0}$ and
$\operatorname{Spec}A_{T_0}$. Over $U_{j_0}$ and over $W_{j_0}$ the system
restricts to the systems $U_j$ and $W_j$, whose limits are $U$ and $W$
(by initiality the limits may be computed over the stages). Over
$\operatorname{Spec}A_{T_0}$ it restricts to the system
$\operatorname{Spec}A_T$: every element of $\Gamma(V,\mathcal O)$ is the
first component of an element of some $A_T$ (lift its restriction to $W$
to some $W_j$), and two elements of $A_T$ with the same first component
become equal at a later stage (their second components agree on $W$, hence
on some $W_j$). So $\Gamma(V,\mathcal O)$ is the filtered colimit of the
$A_T$, and since $\operatorname{Spec}$ takes filtered colimits of rings
to limits, $V=\operatorname{Spec}\Gamma(V,\mathcal O)$ is the limit of the
$\operatorname{Spec}A_T$. Hence $X=\varprojlim_T X_T$ is a Noetherian
approximation of $X$, which completes the induction.
