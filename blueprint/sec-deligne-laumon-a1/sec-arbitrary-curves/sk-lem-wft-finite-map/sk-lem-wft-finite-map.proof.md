+++
kind = "proof"
of = "sk-lem-wft-finite-map"
+++
The map is given by a function with a single pole, at a point at
infinity, and the order of this pole is chosen prime to $p$ so that
the map is generically étale.
Let $\overline C_0$ be the smooth projective completion, choose a
closed point $s$ of $\overline C_0$ outside $C_0$, and choose $m$
prime to $p$ with $(m-1)\deg(s)>2g(\overline C_0)-2$. Both divisors
$ms$ and $(m-1)s$ then have degree $>2g-2$, so Riemann–Roch
(Theorem [sk-thm-picard-rr]) gives
$h^0(\mathcal O(ns))=n\deg(s)+1-g$ for $n=m,m-1$, and hence

$$
h^0(\mathcal O(ms))-h^0(\mathcal O((m-1)s))=\deg(s)>0.
$$

Therefore there is a function $f$ whose only pole is at $s$, of exact
order $m$. The sections $1,f$ define a nonconstant map
$\overline C_0\to\mathbf P^1$ whose inverse image of infinity
is $\{s\}$. This map is proper with finite fibres, hence finite.
To see that it is generically étale, choose a uniformizer $t$ at $s$
and write $f=t^{-m}u$ with $u$ a unit. Since $\kappa(s)/k_0$ is
separable and the curve is smooth, $dt$ generates the module of
differentials near $s$. Writing $du=u'\,dt$, we get

$$
df=t^{-m-1}(-mu+tu')\,dt\ne0,
$$

since $-mu+tu'$ is congruent to the unit $-mu$ modulo $t$, and $mu$ is
a unit because $p\nmid m$. Thus the differential of this finite map between
smooth curves is invertible at the generic point, and so the map is
generically étale. We set $C'_0=\overline C_0\setminus\{s\}$ and
let $\pi$ be the restriction of the map to $C'_0$.

It remains to study $K$. Over the open in the statement, $\pi$ is
finite étale and its inverse image lies in $C_0$, so that $K$ is
lisse there. At a closed point $y$ of this open, the stalk of $K$ is a
sum over the geometric points of the fibre, which Frobenius permutes.
On a cycle of length $e$, corresponding to a point over $y$ with
residue extension of degree $e$, the $e$th power of the operator is
the local Frobenius upstairs. Hence an eigenvalue $\beta$ satisfies
$|\iota\beta|^e=q_y^{ew/2}$, and the weight is still $w$. Finally,
$R\pi_!=\pi_*$ because $\pi$ is finite, and the identification of cohomology
follows by composing direct images with compact support. Since the
construction is defined over $k_0$, this identification commutes with
Frobenius.
