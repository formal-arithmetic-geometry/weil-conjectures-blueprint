+++
id = "lem-finrepair-finite-surjection-cancellation"
kind = "lemma"
title = "Constructibility descends through a finite surjection"
order = 5196
lean = ["AlgebraicGeometry.Etale.hasConstructibleDirectImage_of_comp_finite_surjective"]
uses = ["def-finrepair-property-c", "lem-fin-finite-morphism"]
+++
Let $f:X\to S$ be a morphism between schemes of finite type over $k$, and
let $\pi:Y\to X$ be finite and surjective. If $\mathcal C(f\pi)$ holds, then
$\mathcal C(f)$ holds, with $\mathcal C$ as in [def-finrepair-property-c].

## Proof

Let $Q_0=F$ be any constructible $\Lambda$-sheaf on $X$. For every sheaf
$Q$, the unit $Q\to\pi_*\pi^*Q$ is injective: at a geometric point $\bar x$
it is the diagonal map
$$
Q_{\bar x}\longrightarrow\prod_{\bar y\in Y_{\bar x}}Q_{\bar x},
$$
and the finite indexing set is nonempty by surjectivity; conservativity of
geometric stalks detects this injectivity. The pullback of a constructible
sheaf is constructible, by pulling back its finite locally closed
stratification. Thus [lem-fin-finite-morphism] shows that $\pi_*\pi^*Q$ is
constructible whenever $Q$ is.

Define recursively
$$
G^a=\pi_*\pi^*Q_a,\qquad Q_{a+1}=\operatorname{coker}(Q_a\to G^a).
$$
Every $G^a$ and $Q_{a+1}$ is constructible by induction and the weak-Serre
property. Define the differential $G^a\to G^{a+1}$ as the quotient
$G^a\to Q_{a+1}$ followed by the injective unit $Q_{a+1}\to G^{a+1}$. Its
kernel is the image of $Q_a$, and the preceding differential has precisely
that image. We have therefore constructed an exact augmented complex
$$
0\longrightarrow F\longrightarrow G^0\longrightarrow G^1\longrightarrow G^2\longrightarrow\cdots.
$$

The finite morphism $\pi$ has exact direct image, so the composition
spectral sequence gives $R^bf_*G^a=R^b(f\pi)_*(\pi^*Q_a)$. Each such sheaf
is constructible by the hypothesis $\mathcal C(f\pi)$. Apply the
Cartan–Eilenberg spectral sequence to the displayed resolution, indexing it
as
$$
E_1^{a,b}=R^bf_*G^a\Longrightarrow R^{a+b}f_*F\qquad(a,b\geq0).
$$

Every successive page is formed by kernels and cokernels of maps between
constructible sheaves, so all its terms are constructible. For fixed total
degree $n$, only $0\leq a,b\leq n$ can contribute, and differentials
entering or leaving these terms vanish for sufficiently large page number by
the first-quadrant condition. The abutment has a finite filtration whose
quotients are those stable terms, so it is constructible by the extension
clause. This proves $\mathcal C(f)$.

The resolution is unbounded to the right; this argument makes no claim of a
uniform vanishing bound.

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-geometric-stalk-conservative, lem:weil-pbc-constructible-serre, lem:weil-pbc-grothendieck-spectral-sequence, thm:sp-if-e1
