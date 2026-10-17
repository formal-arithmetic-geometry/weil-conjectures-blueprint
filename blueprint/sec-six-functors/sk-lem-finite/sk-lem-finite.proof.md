+++
kind  = "proof"
of    = "sk-lem-finite"
uses = ["sk-thm-sf-ctf-stability", "sk-thm-sf-direct-image-tor-amplitude", "sk-prop-scalar-six", "sk-prop-integral-criterion", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
At a geometric point a constructible finite-coefficient complex has
bounded finite cohomology; its finite Tor amplitude makes it perfect.
Explicitly, take a bounded-above resolution by finite free modules and
truncate below the Tor bound. The remaining last syzygy is finitely
presented and flat, hence projective. With integral coefficients the
constructible complexes on the point are those with bounded finitely
generated $\Oe$-cohomology; a discrete valuation ring has
global dimension one, so these complexes are perfect. With field
coefficients bounded finite-dimensional complexes are perfect. These
descriptions also follow from the comparisons of the subsection on the
geometric point and continuous cohomology.

Proposition [sk-thm-sf-ctf-stability] applies to the two direct images of
$a_X$, so both lie in $\Dctf(s,\Lambda)$. A bounded
finite-projective representative has a bounded finite-projective
termwise dual. Termwise double evaluation is an isomorphism, with
the usual signs for complexes. This proves all the assertions.

*Complement.* Let first $\Lambda=A_{E,n}$ and let $K$ be a
bounded constructible complex of finite Tor amplitude. The structure
morphism $a_X$ is separated of finite type over the field $k$, so the
finiteness theorems for constructible sheaves apply: the sheaves $R^qa_{X,*}K$ and
$R^qa_{X,!}K$ are constructible and, if the cohomology sheaves of $K$
lie in degrees $[a,b]$, both vanish for $q\notin[a,b+2\dim X]$: the
compact-support ones by the finiteness theorem for $Ra_{X!}$ and its
comparison with the proper case, the ordinary ones by the
fibrewise cohomological-dimension bound, each applied to the
cohomology sheaves of $K$ through the spectral sequence of the truncations
(for $K=\Lambda[-1]$ on a point the bound is $1$, not $2\dim X=0$).

Now let $\Lambda=\Oe$ and $K\in\Dbc(X,\Oe)$ with cohomology sheaves in
$[a,b]$, and put $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}\AEn$. Reduction
modulo $\pi_E^n$ commutes with $Ra_{X*}$ and $Ra_{X!}$ ([sk-prop-scalar-six]),
so $\RGammac(X,K)\otimes^{\mathbf L}_{\Oe}\AEn\simeq\RGammac(X,K_n)$, and
likewise for $\RGamma$. By the main part both are perfect over $\Oe$, hence
lie in $D^b_{\mathrm{fg}}(\Oe)$. Their lower bound is $a$, because $Ra_{X*}$
and $Ra_{X!}=R\bar a_*j_!$ are left t-exact. For the upper bound, $K_1$ has
cohomology sheaves in $[a-1,b]$ (the sequence
$0\to\mathcal H^q(K)/\pi_E\to\mathcal H^q(K_1)\to\mathcal H^{q+1}(K)[\pi_E]\to0$),
so by the torsion case $\RGammac(X,K_1)$ has cohomology in degrees
$\le b+2\dim X$. If $C$ is a perfect $\Oe$-complex and $i$ is the largest
degree with $H^i(C)\neq0$, then $H^i(C\otimes^{\mathbf L}_{\Oe}A_{E,1})=
H^i(C)/\pi_E\neq0$ by Nakayama, so $i\le b+2\dim X$. Thus both complexes have
cohomology in $[a,b+2\dim X]$. A perfect complex over $\Oe$ is represented by
a bounded complex of finite free modules, and its reductions are perfect of
one Tor amplitude independent of $n$.

For $\Lambda=E$, $K$ is obtained by finitely many cones and shifts from objects
$(a_!L_0)[1/\ell]$ with $L_0$ lisse over $\mathcal O_{E,S}$ and placed in the
degrees of the cohomology sheaves of $K$, by dévissage along the truncation
triangles, [sk-lem-coefficient-heart] and [sk-lem-integral-models]. Since
$\RGammac$ and $\RGamma$ commute with $-\otimes_{\Oe}E$
([sk-prop-scalar-six]), which is exact, the integral case gives the degree
bound and finite-dimensionality. For $\Lambda=\Qlb$, $K$ descends to some
$K'\in\Dbc(X,E')$ with the same cohomological range
([sk-thm-sfb-qlbar-two-colimit]; extension of scalars along $E'_X\to\Qlb_X$
is exact and faithful, $\Qlb_X$ being a filtered colimit of the finite free
$E'_X$-modules $F_X$ in which $E'_X$ is a direct summand), and flat extension of scalars gives the claim.
The dual of a bounded complex of finite projective modules
is again one, termwise.
