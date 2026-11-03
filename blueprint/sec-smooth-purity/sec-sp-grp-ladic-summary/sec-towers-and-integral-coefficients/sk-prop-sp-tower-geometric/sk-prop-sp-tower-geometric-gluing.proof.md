+++
kind = "proof"
of = "det-sp-tower-gluing"
+++
*Local pairs.* By [det-sp-tower-p1-adjunction], restricting to
$\mathbf A^1_S\subset\mathbf P^1_S$ by extension by zero (the open-immersion
adjunction $j_{!,\bullet}\dashv j^*_\bullet$ composes with the projective-line one),
we get an adjunction $Rp_{1,!,\bullet}\dashv p^*_{1,\bullet}(-)(1)[2]$ for
$\mathbf A^1_S\to S$; iterating $d$ times gives one for $p_d:\mathbf A^d_Y\to Y$
with right adjoint $p_{d,\bullet}^*(-)(d)[2d]$, and composing with the étale
adjunction $e_{!,\bullet}\dashv e^*_\bullet$ (levelwise extension by zero, counit
the fibre sum) gives on a chart $U$ the pair
$(e_\bullet^*p_{d,\bullet}^*K_\bullet(d)[2d],\varepsilon_U)$ representing
$\operatorname{Hom}(R(f|_U)_{!,\bullet}-,K_\bullet)$. These local counits are the iterated
integrations and fibre sums, as maps of towers.

*Gluing.* For an open cover $X=U\cup V$ with the representing pairs on $U$,
$V$, $U\cap V$, the restriction maps between them are determined by
uniqueness of representing pairs; form the fibre (the cone shifted by $[-1]$) of
the difference map
$Rj_{U,*}G_U\oplus Rj_{V,*}G_V\to Rj_{U\cap V,*}G_{U\cap V}$, whose components are the
restriction units $G\to Rj_*j^*G$ followed by the identifications
$G_U|_{U\cap V}\simeq G_{U\cap V}\simeq G_V|_{U\cap V}$ (pushed forward along the open
immersions by $Rj_*$, the right adjoint of $j^*$, not by extension by zero; it is
the dual of the open-cover triangle for $M_\bullet$:
$j_{U\cap V,!}M\to j_{U,!}M\oplus j_{V,!}M\to M$). Applying
$\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ to this triangle gives a long exact Hom
sequence; the compatible local counits define an element of the fibre product
of the Hom groups of $U$ and $V$ over $U\cap V$, which lifts by exactness to a
counit on the glued object, and the five lemma applied to the two Hom sequences
(for the glued pair and for $\operatorname{Hom}(Rf_{!,\bullet}-,K_\bullet)$) shows that the glued
pair represents the functor on $X$. By quasi-compactness, finitely many charts
suffice and induction on their number gives the pair on $X$.

*Uniformity.* On each chart the glued object is
$e_\bullet^*p_{d,\bullet}^*K_\bullet(d)[2d]$, whose levels have the cohomological and
Tor bounds of $K_\bullet$ shifted by $2d$, independent of $n$; with
[det-sp-tower-bound-uniform] for $Rf_{!,\bullet}$ this shows that both functors
stay inside the constructible tower categories.

*Uniqueness and functoriality.* A representing pair with its counit is unique
up to unique isomorphism, so the construction defines the functor $f^!_\bullet$
and its action on morphisms without choosing cones functorially; the counits
then form a natural transformation and $Rf_{!,\bullet}\dashv f^!_\bullet$.

*Levels.* Evaluation at level $n$ is exact, commutes with the operations
([det-sp-tower-shriek-levels]) and carries the local counits to the finite local
counits. Repeating the gluing argument after evaluation shows that
$((f^!_\bullet K_\bullet)_n,\varepsilon_n)$ represents the finite functor
$\operatorname{Hom}(Rf_{!,\mathcal O_E/\ell^n}-,K_n)$; uniqueness identifies it with
$f^!_{\mathcal O_E/\ell^n}K_n$ compatibly with counits, hence with units. The
coefficient comparisons $c_{n,m}$ have the same chart description (the
canonical isomorphisms of [det-sp-reduction-exceptional]), so by uniqueness the
transition maps of $f^!_\bullet K_\bullet$ are identified with them.
