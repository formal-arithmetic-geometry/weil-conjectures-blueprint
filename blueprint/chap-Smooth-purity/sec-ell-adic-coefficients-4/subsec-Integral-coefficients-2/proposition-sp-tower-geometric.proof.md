+++
kind = "proof"
of = "proposition-sp-tower-geometric"
order = 774
+++
We repeat the construction of Section [sec-The-trace-map-of-affine-space] in the topos of towers. The construction
has two parts: on a chart we write down an explicit adjunction, built from
the trace of the projective line, and then we glue these local adjunctions
over a finite cover. The gluing is done with pairs consisting of an object
and a counit, as in Definition [definition-representing-objects], because such
pairs are unique up to unique isomorphism and so need no choice of
transition maps.

The Kummer sequence
$0\to(\mu_{\ell^n})_n\to(\mathbf G_m,(\cdot)^\ell)\to(\mathbf G_m,\mathrm{id})\to0$ is exact
in towers. Hence Chern classes, the diagonal class and the trace of the
projective line are single morphisms of towers. The identities
(9.9) are equalities of maps between
sheaves of towers in degree zero, so they can be checked at each level.
The construction of (9.10) then gives the adjunction for the
projective line in $D(\operatorname{Tow})$. Extension by zero and the
étale adjunction give local adjunctions on charts.

We glue the local adjunctions in $D(\operatorname{Tow})$, by induction on a
finite cover. Let $X=U\cup V$, and let $(H_U,\varepsilon_U)$ and
$(H_V,\varepsilon_V)$ be pairs representing $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$
on $U$ and on $V$. Put $W=U\cap V$. Both pairs restrict to pairs
representing this functor on $W$. By Yoneda there is a unique
counit-preserving isomorphism between the restrictions, and we call the
common restriction $H_W$. Let $H$ be the cone of
$j_{W!}H_W\to j_{U!}H_U\oplus j_{V!}H_V$, as in the triangle
(9.12). The counits $\varepsilon_U,\varepsilon_V$
agree on $Rf_{!,\bullet}j_{W!}H_W$. By the exact Hom sequence they
therefore lift to a counit $\varepsilon:Rf_{!,\bullet}H\to K_\bullet$. The
five lemma, applied as in the finite case, shows that $(H,\varepsilon)$
represents $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ on $X$. The
tower $H$ is constructible. Indeed, $H|_U\simeq H_U$ and $H|_V\simeq H_V$,
so the union of their intervals bounds its cohomology and Tor amplitude
uniformly in $n$.

Repeating this step over a finite cover of $X$ by charts gives a pair
representing $\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$ on all of
$X$. We let $f^!_\bullet K_\bullet$ be its object. By uniqueness of
representing pairs, this is functorial in $K_\bullet$ and gives the
adjunction (9.18).

The levels are the finite ones, because evaluation at level $n$ carries the
glued pair to a pair representing $\operatorname{Hom}(Rf_!(-),K_n)$ with
coefficients $\mathcal O_E/\ell^n$. Indeed, on each chart it is the local
finite adjunction, and the five lemma argument applies at level $n$. By
uniqueness this pair is the finite one. As the counit is one morphism of
towers, it commutes with the transition maps. Transposing this identity
gives the reduction maps.
