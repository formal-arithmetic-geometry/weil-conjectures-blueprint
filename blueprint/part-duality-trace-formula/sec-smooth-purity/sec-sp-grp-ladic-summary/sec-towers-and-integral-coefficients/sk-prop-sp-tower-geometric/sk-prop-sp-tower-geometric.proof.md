+++
kind = "proof"
of = "sk-prop-sp-tower-geometric"
uses = ["sk-lem-sp-tower-levels", "sk-prop-geo-p1-adjunction", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction"]
+++
We repeat Section [sec-sp-grp-finite] in the topos of towers. The Kummer sequence
$0\to(\mu_{\ell^n})_n\to(\mathbf G_m,(\cdot)^\ell)\to(\mathbf G_m,\mathrm{id})\to0$ is exact
in towers, so Chern classes, the diagonal class and the trace of the projective line are
single morphisms of towers. The identities (10.5) are
equalities of maps between sheaves of towers in degree zero, so they can be checked at each
level, and the construction of (10.6) gives the adjunction for the projective line in
$D(\operatorname{Tow})$. Extension by zero and the étale adjunction give local
adjunctions on charts, and we glue them in $D(\operatorname{Tow})$, by induction on a
finite cover. Let $X=U\cup V$, and let $(H_U,\varepsilon_U)$ and
$(H_V,\varepsilon_V)$ be pairs representing $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$
on $U$ and on $V$; put $W=U\cap V$. Both restrict to pairs representing this functor on $W$,
so by Yoneda there is a unique counit-preserving isomorphism between the restrictions;
call the common restriction $H_W$. Let $H$ be the cone of
$j_{W!}H_W\to j_{U!}H_U\oplus j_{V!}H_V$, as in the triangle
(10.8). The counits $\varepsilon_U,\varepsilon_V$ agree on
$Rf_{!,\bullet}j_{W!}H_W$, so by the exact Hom sequence they lift to a counit
$\varepsilon:Rf_{!,\bullet}H\to K_\bullet$, and the five lemma, applied as in the
finite case, shows that $(H,\varepsilon)$ represents
$\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ on $X$. The tower $H$ is
constructible: $H|_U\simeq H_U$ and $H|_V\simeq H_V$, so the union of their intervals
bounds its cohomology and Tor amplitude uniformly in $n$.
Evaluation at
level $n$ carries the glued pair to a pair representing
$\operatorname{Hom}(Rf_!(-),K_n)$ with coefficients $\mathcal O_E/\ell^n$, which is
the finite one by uniqueness. Finally, the counit is one morphism of towers, so it commutes
with the transition maps, and transposing this identity gives the reduction maps.
