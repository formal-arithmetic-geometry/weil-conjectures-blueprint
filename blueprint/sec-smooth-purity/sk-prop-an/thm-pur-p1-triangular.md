+++
id = "thm-pur-p1-triangular"
kind = "theorem"
title = "Projective-line triangular identities"
order = 2069
uses = ["def-exchange-projection", "def-pur-conventions", "def-pur-p1-integration", "def-pur-td-datum", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-p1-diagonal-class", "lem-pur-p1-kunneth", "lem-pur-td-kernel", "thm-pur-p1-decomposition", "thm-pur-td-criterion"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $Y$ be separated finite type, $q:\mathbf P^1_Y\to Y$, and
let $L_P=\Lambda_{\mathbf P^1_Y}(1)[2]$. With the trace
$\operatorname{tr}_q$ of [def-pur-p1-integration] and the
diagonal class $\operatorname{cl}_\Delta:\Delta_!\Lambda_P\to p_2^*L_P$ of [lem-pur-p1-diagonal-class], the two
triangular composites of
[def-pur-td-datum] for $(q,L_P)$ are the identity, naturally.

## Proof

The unit and counit are the maps specified in [def-pur-td-datum]. In the computation use the diagonal class of [lem-pur-p1-diagonal-class] and the two summands of [thm-pur-p1-decomposition]; the contraction uses the projection transformation of [def-exchange-projection] and the tensor reassociations of [def-weil-derived-tensor], [def-weil-derived-pullback-tensor-hom].
Step 1: the contraction of the diagonal. The composite
$p_{2*}\circ(\operatorname{cl}(\Delta)\cup p_1^*(-))$, read via the
Kunneth comparison [lem-pur-p1-kunneth](2), is

$$
p_{2*}\bigl(p_1^*\alpha\cup \operatorname{cl}(\Delta)\bigr)
=\alpha\qquad(\alpha=1,h),
$$

the two values being computed from $(p_2)_*(h_1+h_2)=1$ and
$(p_2)_*(h_1(h_1+h_2))=h_2$ (the latter equals $(p_2)_*(h_1h_2)$
since $h_1^2=0$, the class of the point $(\infty,\infty)$
pushing to $h_2$; the vanishing of the $h_1^2$-part is the
cohomological dimension of the curve, $h^2=0$ in
$H^4(\mathbf P^1,\Lambda(2))=0$).

Step 2: the first composite. Unwinding the kernel identification
of [lem-pur-td-kernel], in the first triangular composite

$$
Rq_!A\xrightarrow{\ Rq_!\eta_A\ }Rq_!G_{L_P}Rq_!A
\xrightarrow{\ \epsilon_{Rq_!A}\ }Rq_!A
$$

the two occurrences of the graph of $q$ compose with the diagonal:
the resulting morphism of kernels is the endomorphism of
$\Delta_!\Lambda_P$ given by the contraction of Step 1 followed by
the trace; by Step 1 and the normalization
$\operatorname{tr}_q(1)=0,\ \operatorname{tr}_q(h)=1$ of
[def-pur-p1-integration] it is the identity (the $h$-component
of the contracted class contributes $1$, the unit component
contributes $0$). Tensoring these kernel identities with arbitrary
$A\in D^b_{ctf}(Y,\Lambda)$ via the base change and projection
formula computations of [lem-pur-p1-kunneth] proves the first
identity.

Step 3: the second composite. The second triangular composite is
the analogous convolution in the other variable
($G_{L_P}\epsilon$-side), with the roles of $p_1,p_2$ exchanged;
the computations of Step 1 and [lem-pur-p1-kunneth](1) apply
symmetrically (the diagonal class is symmetric and the trace is the
second projection, so the same contraction and normalization give
the identity).
