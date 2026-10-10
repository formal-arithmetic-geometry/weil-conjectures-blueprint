+++
kind  = "proof"
of    = "lemma-nagata-proper-separated-valuation-extension"
+++
Recall that $f$ is proper if and only if it is separated, quasi-compact,
locally of finite type and universally closed.

**Proper implies the conditions.** A proper morphism is quasi-compact,
separated (so quasi-separated) and locally of finite type. Existence of a
lift is the output of
[lemma-nagata-proper-valuative-criterion-existence-api], since $f$ is
universally closed. If $h$ and $h'$ are two lifts, their generic
restrictions are the prescribed morphism, so
[lemma-nagata-separated-valuation-lift-unique] gives $h=h'$.

**The conditions imply proper.** By
[lemma-nagata-proper-valuative-criterion-existence-api], quasi-compactness
and existence of lifts make $f$ universally closed. It remains to see
that $f$ is separated. Since $f$ is quasi-separated, the diagonal
$\Delta\colon Y\to Y\times_SY$ is a quasi-compact immersion, so it is a
closed immersion as soon as its image is stable under specialization, because the closure of
the image of a quasi-compact morphism consists of the specializations of
image points. Let $z'=\Delta(y')$ specialize
to $z$. As in the proof of
[lemma-nagata-proper-valuative-criterion-existence-api], choose a valuation
ring $A$ of $K=\kappa(y')$ dominating the local ring at $z$ of the
reduced closure of $z'$; this gives
$\operatorname{Spec}(A)\to Y\times_SY$ sending the generic point to $z'$
and the closed point to $z$. Its two projections
$h_1,h_2\colon\operatorname{Spec}(A)\to Y$ restrict on
$\operatorname{Spec}(K)$ to the same map (the point $y'$), and both lie
over the same morphism $\operatorname{Spec}(A)\to S$. They are thus two
lifts of one valuative square, so $h_1=h_2$ by uniqueness. Hence the map
factors through $\Delta$, and $z\in\Delta(Y)$.
