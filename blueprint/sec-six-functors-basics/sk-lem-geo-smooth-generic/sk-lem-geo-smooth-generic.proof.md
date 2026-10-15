+++
kind = "proof"
of = "sk-lem-geo-smooth-generic"
uses = ["sk-prop-cohsm", "sk-prop-pe-finite-local-systems", "sk-prop-sf-existence"]
+++
Finite-presentation local-system comparison
([sk-prop-pe-finite-local-systems]) gives an étale antecedent of $L$. We make
the following duality and constructibility computation there, in the
categories $D(-_{\mathrm{ét}},\Fell)$, and then use the direct-image and
constructible comparisons to obtain the assertion on $X_{\mathrm{proét}}$ and
$S_{\mathrm{proét}}$.

The idea is to write $L$ as the dual of a complex $N$ relative to $\omega_f$.
Then $Rf_*L$ is the $\Fell$-linear dual of $Rf_!N$ (see (G16)). After
shrinking $S$, $Rf_!N$ has locally constant cohomology, and the dual of such a
complex is again of this kind and commutes with pullback. It remains to check
that the identification (G16) is compatible with base change.

$X$ is the disjoint union of finitely many open pieces of pure relative
dimension, so we may assume $f$ has pure relative dimension $d$. Let
$\omega_f=f^!\mathbf F_{\ell,S}$ as in [sk-prop-cohsm], and let

$$
N=\cHom_X(L,\mathbf F_{\ell,X})\otimes^{\mathbf L}\omega_f .
$$

By [sk-prop-cohsm], $\omega_f$ is locally $\mathbf F_{\ell,X}(d)[2d]$, so $N$
is bounded constructible and $\cHom_X(N,\omega_f)=L$.

*Duality.* There is a canonical isomorphism

$$
Rf_*L=\cHom_S(Rf_!N,\mathbf F_{\ell,S})\quad\text{in }D(S_{\mathrm{ét}},\Fell).
\qquad\text{(G16)}
$$

To see this, write $L=\cHom_X(N,f^!\mathbf F_{\ell,S})$. Test the canonical
pairing on shifts of $P=a_!\Fell$, where $a:V\to S$ is quasi-compact,
separated and étale. These free representable module sheaves lie in $\Dctf$
and their shifts detect isomorphisms in $D(S_{\mathrm{ét}},\Fell)$. Since
$f^*P\otimes^{\mathbf L}N$ lies in $\Dctf(X,\Fell)$, tensor-Hom adjunction, the
Brown adjunction $Rf_!\dashv f^!$ between $\Loc(\Dctf(X,\Fell))$ and
$\Loc(\Dctf(S,\Fell))$ of [sk-prop-sf-existence], and the projection formula
give, with Hom groups in $D(S_{\mathrm{ét}},\Fell)$,

$$
\Hom(P,Rf_*\cHom(N,f^!\mathbf F_{\ell,S}))
=\Hom(Rf_!(f^*P\otimes^{\mathbf L}N),\mathbf F_{\ell,S})
=\Hom(P\otimes^{\mathbf L}Rf_!N,\mathbf F_{\ell,S}).
$$

The canonical map adjoint to the pairing (G17) below realizes these bijections
for all shifts of the generators, hence is an isomorphism. This proves (G16)
in $D(S_{\mathrm{ét}},\Fell)$; the constructibility of $Rf_*L$ will be deduced
from it.

*Shrinking the base.* By Stacks, Tags
[0GL0](https://stacks.math.columbia.edu/tag/0GL0) and
[0G2A](https://stacks.math.columbia.edu/tag/0G2A), $Rf_!N$ is bounded
constructible. Each of its finitely many nonzero cohomology sheaves is locally
constant on a nonempty open of $S$; let $S_0$ be the intersection of these
opens. Over the field $\Fell$, a finite locally constant sheaf is locally free
of finite rank, its dual is exact, and evaluation identifies it with its double
dual. By induction on the number of nonzero cohomology sheaves, using
truncation triangles (the relevant canonical maps form morphisms of these
triangles), a bounded complex with finite locally constant cohomology is
dualizable, its dual is again of this kind, and forming the dual commutes with
every pullback. By (G16), this proves the first assertion over $S_0$.

*Base change.* The isomorphism (G16) is adjoint to the pairing in
$D(S_{\mathrm{ét}},\Fell)$

$$
Rf_!N\otimes^{\mathbf L}Rf_*L
 \longrightarrow Rf_!(N\otimes^{\mathbf L}L)
 \longrightarrow Rf_!\omega_f
 \xrightarrow{\epsilon_{\mathbf F_{\ell,S}}}\mathbf F_{\ell,S},
\qquad\text{(G17)}
$$

where the first arrow is the projection formula followed by the counit
$f^*Rf_*L\to L$, and the second is evaluation. Let $v:T\to S_0$ be a
finite-type $k$-scheme over $S_0$, and let $f_T:X_T\to T$ and $v_X:X_T\to X$
be the base changes. Base change for $Rf_!$ and (G12) of [sk-prop-cohsm]
identify $v_X^*N$, $v^*Rf_!N$ and $v_X^*\omega_f$ with the corresponding
objects for $f_T$. The base-change map $v^*Rf_*L\to Rf_{T,*}v_X^*L$ in
$D(T_{\mathrm{ét}},\Fell)$ is characterized by the fact that it carries the
pulled-back counit $f^*Rf_*L\to L$ to the counit for $f_T$. Hence the pullback
of (G17) is the pairing for $f_T$, composed with this base-change map. Since
$v^*Rf_!N$ is dualizable with dual $v^*\cHom(Rf_!N,\mathbf F_{\ell,S})$, the
base-change map for $Rf_*L$ is identified with the dual of the base-change
isomorphism for $Rf_!N$. It is therefore an isomorphism.
