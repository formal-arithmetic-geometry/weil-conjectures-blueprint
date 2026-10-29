+++
kind  = "proof"
of    = "sk-prop-wgen-relative-line"
+++
*Localization.* The reductions here and in [sk-thm-dl-general-sheaf]
rest on the following observation (details in
[det-l-dl-general-excision]). By [sk-r-real-linear], mixed
sheaves of weights at most $u$ are closed under subquotients and
extensions. Hence, if $A\to B\to C$ is exact and $A,C$ have this
bound, so does $B$, since it is an extension of a quotient of $A$ by a
subobject of $C$. Consequently, if $A\to B\to C\to A[1]$ is a
geometric distinguished triangle with compatible Weil structures and
$A,C\in D_{\leq w}$, then $B\in D_{\leq w}$; indeed, in the
Frobenius-equivariant cohomology sequence, the term of degree $n$ is an
extension of subquotients of the two outer terms in the same degree.

We use this on both sides of a morphism $f$. On the source we use the
triangle $j_!j^*K\to K\to i_*i^*K\to$ for an open subscheme and its
closed complement ([sk-prop-sf-open-closed-triangle]), together with
the composition isomorphism for $Rf_!$ ([sk-thm-sf-comp-composition]).
On the target we use compact-support base change ([det-prop-sf-cbc])
followed by the same triangle. Restrictions preserve weights, and
extension by zero and closed direct image preserve pure weights.
Applying these localization triangles successively, we reassemble a
finite stratification; their long exact cohomology sequences are
Frobenius-equivariant by naturality.

*The relative line.* Using a finite mixed filtration of $G$, we reduce to the case where
$G$ is pure and constructible of weight $v\leq w$. We first construct
the strata over an integral affine target $Y_0=\operatorname{Spec}B$;
then $\mathbf A^1_{Y_0}$ is integral. Choose a dense open $U$ on which
$G$ is lisse, and let $I\subset B[T]$ be the ideal of its reduced
complement. If the complement is nonempty, choose a nonzero $g\in I$
and invert its nonzero leading coefficient $b$. The resulting monic
relation shows that $B_b[T]/I$ is finite over $B_b$. If $g$ has degree
zero, the complement becomes empty, and this case is allowed.

Thus over $D(b)$ the complement is finite, while the open $U$ is
smooth of relative dimension one with affine fibres, each of which is
an affine line minus finitely many points. We apply
[sk-p-dl-general-relative-line] on $U$ and
[sk-l-dl-general-quasifinite] on the complement, and the localization
sequence on the source gives the desired bound over $D(b)$.

If the reduced target has several components, take disjoint integral
affine opens containing their generic points and perform this
construction on each of them. Their union is open, and its complement
has smaller dimension, so we may argue by induction on this closed
complement. Constructibility permits finite affine refinements
throughout, and nilpotents do not change the category of sheaves
([sk-i-topology]). Gluing on the target as described above finishes
the proof. To keep the construction Weil-equivariant, we make all
choices over one finite constant extension and intersect the finitely
many Frobenius conjugates of each dense open on which $G$ is lisse;
localizing as above again makes the complement finite. If a constant
extension was necessary, its trace retraction, as in the proof of
[sk-i-dl-general-real], descends the bound.
