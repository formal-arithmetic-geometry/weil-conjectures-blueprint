+++
kind  = "proof"
of    = "det-prop-scalar-six-direct-image"
uses = ["det-prop-scalar-six-pullback", "det-prop-scalar-six-ctf", "sk-prop-ctf-finite-comparison", "sk-cor-pe-bounded-continuity", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sf-ctf-stability", "sk-prop-sfb-cartesian-coefficients"]
+++
*(2) Formal properties.* $\gamma_{f,K}$ is the mate of the pullback identification
$f^*((-)_{\Lambda'})\simeq(f^*-)_{\Lambda'}$ under the adjunctions $f^*\dashv Rf_*$ over
$\Lambda$ and over $\Lambda'$. Mates of natural isomorphisms compatible with
composition are compatible with composition, and the stated compatibility with
units and counits is the triangle identity for mates. Naturality is clear. Note
that $Rf_*$ commutes with restriction of scalars (it is computed on the
underlying complexes of abelian sheaves), and restriction of scalars is
conservative; so to see that $\gamma_{f,K}$ is an isomorphism we may regard it as a
map of complexes of $\Lambda$-modules.

*Preservation.* $K_{\Lambda'}\in\Dctf(X,\Lambda')$ by [det-prop-scalar-six-ctf], and $Rf_*$
preserves $\Dctf$ ([sk-thm-sf-ctf-stability]); so both sides of $\gamma_{f,K}$ lie in
$\Dctf(Y,\Lambda')$. It remains to prove that $\gamma_{f,K}$ is an isomorphism, and by
[det-prop-scalar-six-pullback] (3) and compatibility of the mates with composition
of coefficient maps it suffices to treat the elementary maps.

*Finite rings $A\to B$.* By [sk-prop-ctf-finite-comparison], $K=\nu_X^*K'$ for some
$K'\in\D(X_{\mathrm{ét}},A)$, and $Rf_*$ and pullback on $\D(-_{\mathrm{proét}})$ agree with
their classical étale versions transported by $\nu^*$. The functor $\nu^*$ commutes
with extension of scalars by the argument of [det-prop-scalar-six-pullback] (1)
(it is the pullback of a morphism of ringed topoi with $\nu^{-1}A=A$). So it
suffices to show that the étale comparison $(Rf_*K')_B\to Rf_*(K'_B)$ is an
isomorphism in $\D(Y_{\mathrm{ét}},B)$. Let $V\to Y$ be a quasi-compact étale test object and
$X_V=X\times_YV$. The scalar projection formula (Stacks, Tag 0F12), which only needs
the cohomological dimension bounds for $\ell$-primary coefficients valid on the
standing schemes and therefore applies to every $B$ regardless of its projective
dimension over $A$, gives on $V$ and on $X_V$
$$
R\Gamma(V,(Rf_*K')_B)\simeq R\Gamma(V,Rf_*K')\otimes^{\mathbf L}_AB=R\Gamma(X_V,K')\otimes^{\mathbf L}_AB\simeq R\Gamma(X_V,K'_B)=R\Gamma(V,Rf_*(K'_B)),
$$
and this composite is $R\Gamma(V,\gamma)$, since all maps are the canonical ones. The
isomorphisms commute with restriction along $V'\to V$, so on cohomology sheaves
(sheafifications of $V\mapsto H^q(V,-)$) $\gamma$ induces isomorphisms. Hence $\gamma$ is
an isomorphism in $\D(Y_{\mathrm{ét}},B)$, and so in $\D(Y_{\mathrm{proét}},B)$.

*Finite free and finitely presented coefficient extensions.* For a complex $F$ of
condensed $\Lambda$-modules, finite free in each degree and bounded, consider the
natural map $F_Y\otimes_{\Lambda_Y}Rf_*K\to Rf_*(F_X\otimes_{\Lambda_X}K)$ defined in the same way.
It is an isomorphism for $F=\Lambda$, it is compatible with finite sums, and it is a
morphism of triangles for a cone, because $Rf_*$ is exact. Hence it is an
isomorphism for every bounded complex of finite free modules.
- For $\mathcal O_E\to\mathcal O_F$ and $E\to F$, $\Lambda'_X$ is finite free over $\Lambda_X$
  ([sk-prop-sfb-cartesian-coefficients] (2)); take $F=\Lambda'$.
- For $\mathcal O_E\to A$ with $A$ finite, $A$ is a finitely generated torsion
  $\mathcal O_E$-module, so there is an exact sequence
  $0\to\mathcal O_E^m\xrightarrow{\phi}\mathcal O_E^m\to A\to0$. Its condensed version is exact: a
  continuous map from a profinite set to the finite discrete quotient $A$ is locally
  constant, hence lifts on a finite clopen partition. Pulling back along $p_X$ gives
  an exact sequence $0\to\mathcal O_{E,X}^m\to\mathcal O_{E,X}^m\to A_X\to0$, a finite free
  resolution of $A_X$. Hence $K_A\simeq\operatorname{cone}(\phi\colon K^m\to K^m)$ as
  $\mathcal O_E$-modules, and the case $F=[\mathcal O_E^m\xrightarrow{\phi}\mathcal O_E^m]$ applies.

*$\mathcal O_E\to E$.* By [sk-prop-sfb-qlbar-colimit-x], $E_X=\varinjlim(\mathcal O_{E,X}\xrightarrow{\ell}\mathcal O_{E,X}\xrightarrow{\ell}\cdots)$,
which is flat over $\mathcal O_{E,X}$. So $K_E$ is represented by the termwise colimit of
$K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$ for a bounded representative $K$; these
complexes vanish below a common degree. By [sk-cor-pe-bounded-continuity], $R^qf_*$
commutes with this filtered colimit, so
$\mathcal H^q(Rf_*(K_E))=\varinjlim(\mathcal H^qRf_*K\xrightarrow{\ell}\cdots)=\mathcal H^q((Rf_*K)_E)$, and
the identification is induced by $\gamma$ (which is compatible with the transition
maps). Hence $\gamma$ is an isomorphism.

*$E\to\Qlb$.* By [sk-prop-sfb-qlbar-colimit-x], $\QbarX=\varinjlim_FF_X$ over the finite
extensions $F/E$ in $\Qlb$, a filtered colimit of finite free $E_X$-modules. So
$K_{\Qlb}=\varinjlim_FK_F$ termwise, with a common lower bound. Combine
[sk-cor-pe-bounded-continuity] with the case $E\to F$ treated above.
