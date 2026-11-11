+++
kind = "proof"
of = "lemma-finite-generically-etale-map-line"
order = 1313
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "lemma-subobjects-quotients-weil-sheaves", "lemma-finite-quasi-finite-direct-images"]
+++
The map is given by a function with a single pole, at a point at
infinity, and we choose the order of this pole prime to $p$ so that
the map is generically étale. We find the function by Riemann–Roch,
we show by a local computation at the pole that its differential is
nonzero, and we check the assertions about $K$ stalk by stalk.

Let $\overline C_0$ be the smooth projective completion, choose a
closed point $s$ of $\overline C_0$ outside $C_0$, and choose $m$
prime to $p$ with $(m-1)\deg(s)>2g(\overline C_0)-2$. Both divisors
$ms$ and $(m-1)s$ then have degree $>2g-2$, so Riemann–Roch
(Theorem [theorem-riemann-roch-coherent-serre-duality]) gives
$h^0(\mathcal O(ns))=n\deg(s)+1-g$ for $n=m,m-1$, and hence

$$
h^0(\mathcal O(ms))-h^0(\mathcal O((m-1)s))=\deg(s)>0.
$$

Therefore there is a function $f$ whose only pole is at $s$, of exact
order $m$. The sections $1,f$ define a nonconstant map
$\overline C_0\to\mathbf P^1$ whose inverse image of infinity
is $\{s\}$, and this map is proper with finite fibres, hence finite.
To see that it is generically étale, choose a uniformizer $t$ at $s$
and write $f=t^{-m}u$ with $u$ a unit. Since $\kappa(s)/k_0$ is
separable and the curve is smooth, $dt$ generates the module of
differentials near $s$. Writing $du=u'\,dt$, we get

$$
df=t^{-m-1}(-mu+tu')\,dt\ne0,
$$

since $-mu+tu'$ is congruent to the unit $-mu$ modulo $t$, and $mu$ is
a unit because $p\nmid m$. The differential of this finite map between
smooth curves is therefore invertible at the generic point, and the map is
generically étale. We set $C'_0=\overline C_0\setminus\{s\}$ and
let $\pi$ be the restriction of the map to $C'_0$.

Over the open in the statement, $\pi$ is
finite étale and its inverse image lies in $C_0$, where $j_!F=F$.
Moreover, the direct image of a lisse sheaf under a finite étale map is lisse,
because étale locally the map is a disjoint union of copies of the
base. Hence $K$ is lisse there. For purity, note that at a closed point $y$ of this open,
the stalk of $K$ is a sum over the geometric points of the fibre, which
Frobenius permutes.
Consider such a cycle of length $e$, corresponding to a point over $y$ with
residue extension of degree $e$. On it the $e$th power of the operator is
the local Frobenius upstairs, so an eigenvalue $\beta$ satisfies
$|\iota\beta|^e=q_y^{ew/2}$, and the weight is still $w$. Since
$R\pi_!=\pi_*$ for the finite map $\pi$, the identification of cohomology
follows by composing direct images with compact support. It
commutes with Frobenius because the construction is defined over $k_0$.
