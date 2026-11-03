+++
kind = "proof"
of = "det-sp-tower-gluing"
uses = ["det-sp-representing-pair-gluing", "det-sp-reduction-direct-image"]
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

*Gluing.* Let $X=U\cup V$ be an open cover, put $W=U\cap V$, and let
$(G_U,\varepsilon_U)$, $(G_V,\varepsilon_V)$ be pairs representing
$\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ on $U$ and on $V$. Both restrict to pairs
representing this functor on $W$, so by uniqueness of representing pairs there is
a unique counit-preserving isomorphism $G_U|_W\simeq G_V|_W$; call the common
restriction $(G_W,\varepsilon_W)$. Let $a:j_{W!}G_W\to j_{U!}G_U$ be $j_{U!}$ of the
transpose $j_{W,U!}G_W\to G_U$ (under $j_{W,U!}\dashv j_{W,U}^*$, with
$j_{W,U}:W\to U$) of the identification $G_W\simeq G_U|_W$, and define
$b:j_{W!}G_W\to j_{V!}G_V$ in the same way. Form, in the derived category of towers,
$$
G=\operatorname{Cone}\Bigl(j_{W!}G_W\xrightarrow{(a,-b)}j_{U!}G_U\oplus j_{V!}G_V\Bigr).
$$
Restricting to $U$ (restriction is exact, $j_U^*j_{U!}=\mathrm{id}$ and
$j_U^*j_{V!}G_V\simeq j_{W,U!}(G_V|_W)\simeq j_{W,U!}G_W$) gives
$$
G|_U\simeq\operatorname{Cone}\Bigl(j_{W,U!}G_W\xrightarrow{(a',-1)}G_U\oplus j_{W,U!}G_W\Bigr)\simeq G_U,
$$
where $a'$ is the transpose above: the second component is an isomorphism, so the
map from $G_U$ to the cone is an isomorphism. Similarly $G|_V\simeq G_V$, and under
these isomorphisms the maps $j_{U!}G_U\to G$, $j_{V!}G_V\to G$ of the triangle are
the counits $j_{U!}j_U^*G\to G$, $j_{V!}j_V^*G\to G$. Constructibility of $G$ and
uniform (in the level) bounds on its cohomology and Tor amplitude are local, so
they follow from those of $G_U$ and $G_V$; no preservation theorem for $Rj_*$ is
needed.

Applying $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ to the triangle
$j_{W!}G_W\to j_{U!}G_U\oplus j_{V!}G_V\to G\to$ and using
$Rf_{!,\bullet}j_{W!}=R(f|_W)_{!,\bullet}$ gives an exact sequence
$$
\operatorname{Hom}(Rf_{!,\bullet}G,K_\bullet)\to
\operatorname{Hom}(R(f|_U)_{!,\bullet}G_U,K_\bullet)\oplus\operatorname{Hom}(R(f|_V)_{!,\bullet}G_V,K_\bullet)
\to\operatorname{Hom}(R(f|_W)_{!,\bullet}G_W,K_\bullet).
$$
The pair $(\varepsilon_U,\varepsilon_V)$ maps to $\varepsilon_W-\varepsilon_W=0$, because
the overlap identification preserves counits, so it lifts to a counit
$\varepsilon:Rf_{!,\bullet}G\to K_\bullet$ whose restrictions to $U$ and $V$ are
$\varepsilon_U$ and $\varepsilon_V$. For $M_\bullet$ on $X$, apply
$\operatorname{Hom}(-,G)$ and $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ to the
open-cover (Mayer–Vietoris) triangle
$j_{W!}(M_\bullet|_W)\to j_{U!}(M_\bullet|_U)\oplus j_{V!}(M_\bullet|_V)\to M_\bullet\to$ and
to all its shifts; $b\mapsto\varepsilon\circ Rf_{!,\bullet}(b)$ is a morphism between
the two long exact sequences which, via $j_!\dashv j^*$, is a bijection at the terms
for $U$, $V$ and $W$ in every shift by the local adjunctions. The five lemma
then shows that $(G,\varepsilon)$ represents the functor on $X$, exactly as in
[det-sp-representing-pair-gluing]. By quasi-compactness, finitely many charts
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
$f^!_{\mathcal O_E/\ell^n}K_n$ compatibly with counits, hence with units.
For the transitions, write $G=f^!_\bullet K_\bullet$, and for $m\ge n$ let
$\rho_G:(G_m)_{\mathcal O_E/\ell^n}\to G_n$ and
$\rho_K:(K_m)_{\mathcal O_E/\ell^n}\to K_n$ be the reduction maps. The counit
$\varepsilon$ is one morphism of towers, so it commutes with the transition maps:
$\varepsilon_n\circ Rf_{!,n}(\rho_G)=\rho_K\circ(\varepsilon_m)_{\mathcal O_E/\ell^n}\circ b^{-1}$,
with $b$ the comparison of [det-sp-reduction-direct-image]. By the defining
identity of $c_{n,m}=c_{\mathcal O_E/\ell^m,\mathcal O_E/\ell^n}(K_m)$ in
[det-sp-reduction-exceptional] and naturality of the counit, the right-hand side
equals $\varepsilon_n\circ Rf_{!,n}\bigl(f^!(\rho_K)\circ c_{n,m}\bigr)$. Transposing
under $Rf_{!,n}\dashv f^!_{\mathcal O_E/\ell^n}$ gives
$\rho_G=f^!(\rho_K)\circ c_{n,m}$. (That $c_{n,m}$ and the transitions of $G$ have
the same description on each chart would not by itself prove this equality of
morphisms in the derived category.)
