+++
kind = "proof"
of = "sk-lem-geo-smooth-generic"
uses = ["sk-prop-pe-finite-local-systems", "sk-prop-cohsm", "sk-prop-sf-existence"]
+++
By [sk-prop-pe-finite-local-systems], the local system $L$ comes from an étale
local system, and we work with it on the étale site.

Since $X$ is the disjoint union of finitely many open pieces of pure relative
dimension, we may assume that $f$ has pure relative dimension $d$. Let
$\omega_f=f^!\mathbf F_{\ell,S}$ as in [sk-prop-cohsm], and let

$$
N=\cHom_X(L,\mathbf F_{\ell,X})\otimes^{\mathbf L}\omega_f .
$$

By [sk-prop-cohsm], $\omega_f$ is locally $\mathbf F_{\ell,X}(d)[2d]$. Hence
$N$ is bounded constructible and $\cHom_X(N,\omega_f)=L$.

*Duality.* Consider the pairing

$$
Rf_!N\otimes^{\mathbf L}Rf_*L
 \longrightarrow Rf_!(N\otimes^{\mathbf L}L)
 \longrightarrow Rf_!\omega_f
 \xrightarrow{\varepsilon_{\mathbf F_{\ell,S}}}\mathbf F_{\ell,S},
\qquad\text{(G17)}
$$

where the first arrow is the projection formula followed by the counit
$f^*Rf_*L\to L$, and the second is evaluation. Its adjoint is a map

$$
Rf_*L\longrightarrow \cHom_S(Rf_!N,\mathbf F_{\ell,S}),
\qquad\text{(G16)}
$$

and we claim that it is an isomorphism. To see this, write
$L=\cHom_X(N,f^!\mathbf F_{\ell,S})$. We check (G16) on Hom groups out of the
objects $P[n]$, where $P=u_!\Fell$ and $u:V\to S$ is quasi-compact, separated
and étale. The objects $u_!\Fell$ are constructible of finite Tor amplitude,
and their shifts detect isomorphisms in $D(S_{\mathrm{ét}},\Fell)$. Since
$f^*P\otimes^{\mathbf L}N$ lies in $\Dctf(X,\Fell)$, we may use tensor-Hom
adjunction, the adjunction $Rf_!\dashv f^!$ of [sk-prop-sf-existence] between
$\Loc(\Dctf(X,\Fell))$ and $\Loc(\Dctf(S,\Fell))$, and the projection formula.
With Hom groups in $D(S_{\mathrm{ét}},\Fell)$, we obtain

$$
\Hom(P,Rf_*\cHom(N,f^!\mathbf F_{\ell,S}))
=\Hom(Rf_!(f^*P\otimes^{\mathbf L}N),\mathbf F_{\ell,S})
=\Hom(P\otimes^{\mathbf L}Rf_!N,\mathbf F_{\ell,S}).
$$

By tensor-Hom adjunction, the last group is
$\Hom(P,\cHom_S(Rf_!N,\mathbf F_{\ell,S}))$. Unwinding the adjunctions, the
composite bijection is the map induced by (G16), and the same holds for every
shift of $P$. Hence (G16) is an isomorphism.

*Shrinking the base.* By the finiteness theorem for $Rf_!$
([Stacks, Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0),
[Stacks, Tag 0G2A](https://stacks.math.columbia.edu/tag/0G2A)), $Rf_!N$ is
bounded constructible. Each of its finitely many nonzero cohomology sheaves is
locally constant on a nonempty open of $S$, and we let $S_0$ be the
intersection of these opens. Recall that over the field $\Fell$, a finite
locally constant sheaf is locally free of finite rank, its dual is exact, and
evaluation identifies it with its double dual. By induction on the number of
nonzero cohomology sheaves, it follows that a bounded complex with finite
locally constant cohomology is dualizable, that its dual is again of this
kind, and that forming the dual commutes with every pullback, since the
relevant canonical maps form morphisms of the truncation triangles. By (G16),
this proves the first assertion over $S_0$.

*Base change.* Let $v:T\to S_0$ be a $k$-scheme of finite type over $S_0$, and
let $f_T:X_T\to T$ and $v_X:X_T\to X$ be the base changes. Base change for
$Rf_!$ and (G12) of [sk-prop-cohsm] identify $v_X^*N$, $v^*Rf_!N$ and
$v_X^*\omega_f$ with the corresponding objects for $f_T$. The base change map
$v^*Rf_*L\to Rf_{T,*}v_X^*L$ is characterized by the fact that it carries the
pullback of the counit $f^*Rf_*L\to L$ to the counit for $f_T$. Hence the
pullback of (G17) is the pairing for $f_T$, composed with this base change map.
Since $v^*Rf_!N$ is dualizable with dual
$v^*\cHom(Rf_!N,\mathbf F_{\ell,S})$, the base change map for $Rf_*L$ is
identified with the dual of the base change isomorphism for $Rf_!N$, and
therefore it is an isomorphism.
