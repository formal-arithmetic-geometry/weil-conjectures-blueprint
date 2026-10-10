+++
kind  = "proof"
of    = "sk-thm-picard-hilb-curves"
+++
*Hypothesis check (with the seam $S_1$).* A finite set of
points of $X$ lies in an affine open: take $D_0=\sum_j[P_j]$ with
$m=\sum_j[\kappa(P_j):k]\ge1$; by [sk-thm-picard-rr] (G) (applicable:
$X$ is geometrically irreducible and smooth, hence geometrically
integral, so $H^0(X,\cO_X)=k$) the module
$\cO_X(D_0)$ is ample, and by [sk-thm-picard-rr] (H) the complement of
$\operatorname{Supp}(D_0)$ is affine and contains the points.
*Smoothness.* $\Hilb^0_{X/k}=\Spec k$ and
$\Hilb^1_{X/k}\cong X$ (degree-$1$ closed subschemes are graphs of
sections); the addition morphism $H_d\times_kX\to H_{d+1}$ is finite
locally free of degree $d+1$, hence faithfully flat, so smoothness
descends along faithfully flat morphisms — induction on $d$ giving
$\Hilb^d$ smooth of dimension $d$.
*Properness, integrality.* The iterated addition
$\pi_d:X^d\to H_d$ is finite locally free of degree $d!$ and
surjective (over $\bar k$ a finite flat scheme of rank $d$ is a sum
of closed points), hence $H_d=\pi_d(X^d)$ is proper and irreducible;
with smoothness, a variety of dimension $d$. The same holds after any
field extension $k'/k$ ($\pi_d$ stays surjective, $(X_{k'})^d$ is
irreducible and $(H_d)_{k'}$ smooth), so $H_d$ is geometrically integral.
*Points (seam $S_2$ at work).* By the Cartier criterion
($X_T\to T$ smooth of relative dimension $1$: finite locally free
$\iff$ relative effective Cartier), the points are the effective
Cartier divisors of degree $d$. *Universal divisor*: the
universal closed subscheme is a relative effective Cartier divisor
by the same criterion, and by the Yoneda lemma the point classified by
$h:T\to\underline{\Hilb}^d_{X/k}$ is its pullback along $h\times\mathrm{id}_X$;
the fibre of its module over $[D]$ is $\cO_X(D)$.
