+++
kind  = "proof"
of    = "thm-pur-general-admissibility"
+++
On a chart $U\subseteq f^{-1}(V)$ with $V$ affine the morphism
$U\to V$ is affine of finite type, so the presentation of its
coordinate ring as a quotient of a polynomial algebra over
$\mathcal O_V(V)$ exhibits it as a closed subscheme
$i_U:U\hookrightarrow\mathbf A^{d_U}_V$ ([def-sbc-affine-space]);
write $\pi_U:\mathbf A^{d_U}_V\to V$ for the projection and
$u_U:U\hookrightarrow X$ for the open immersion (an open immersion, since
$U\subseteq f^{-1}(V)\subseteq X$), so that $fu_U=\pi_Ui_U$.
All right adjoints below are the right adjoints relative to the
bounded-below objects of étale origin of [thm-sf-ambient-adjoint-class]
(for open immersions, the inverse image, which is right adjoint to extension
by zero on the whole derived category, [prop-exc-open-adjoint]). The exact
functors $u_{U!}$, $i_{U*}=R(i_U)_!$ and extension by zero along an open
immersion carry bounded-below objects of étale origin to such objects, and
the values of these right adjoints on bounded-below objects of étale origin
are again bounded below of étale origin; so relative adjunctions compose, and
the Yoneda lemma inside the full subcategory of bounded-below objects of étale
origin identifies two such right adjoints of the same functor.
Step 1: the right adjoint of the chart. The compact-support direct image
of a composite is the composite of the compact-support direct images, and
the right adjoint of a composite of functors is the composite of their
right adjoints, so

$$
R(fu_U)^{\times}\;\cong\;R(i_U)^{\times}\circ R(\pi_U)^{\times},
\qquad
Lu_U^*\circ Rf^{\times}\;\cong\;R(fu_U)^{\times},
$$

the second because $R(u_U)_!=u_{U!}$ has right adjoint $Lu_U^*$ by
[prop-exc-open-adjoint]. Hence it suffices to bound
$R(i_U)^{\times}R(\pi_U)^{\times}$.
Step 2: the chartwise bounds. Fix $V$ and a chart $U\subseteq f^{-1}(V)$, and write $d=d_U$, $c'=c_U$. The projection $\pi_U$ is
smooth of pure relative dimension $d$, so
[cor-pur-smooth-admissibility] gives, for
$L\in D_c^{[a,b]}(V,A)$,

$$
R(\pi_U)^{\times}L\in D_c^{[a-2d,b-2d]}(\mathbf A^{d}_V,A),
$$

and for $K$ with finite Tor amplitude in $[a,b]$, finite Tor amplitude
in $[a-2d,b-2d]$; for the closed immersion $i_U$ the étale right
adjoint entering $R(i_U)^{\times}=\nu^*i_U^{\times}R\nu_*$ is the
closed-support functor of [lem-exc-closed-ambient], and the
closed-support computations [lem-exc-closed-amplitude] and
[prop-exc-closed-tor], applied to the pair $(i_U,W_U)$ under the
assumed open-complement condition, move the interval to
$[a-2d,b-2d+c'+1]$. The exact restriction $Lu_U^*$ preserves both
kinds of bound ([thm-exc-explicit-preservation] for the open immersion $u_U$), so each chart carries the interval
$[a-2d_U,b-2d_U+c_U+1]$, which is contained in
$[a-2D,b-2D+c]$ by the choice of $D$ and $c$.
Step 3: passage from the affine opens of the base to the base. For an
affine open $V\subseteq Y$ with open immersion $g_V:V\hookrightarrow Y$
and $f_V:f^{-1}(V)\to V$, with $g'_V:f^{-1}(V)\hookrightarrow X$ the
base-changed open immersion, one has $g_{V!}Rf_{V!}\cong Rf_!g'_{V!}$, and
$Lg_V^*$, $Lg_V'^*$ are right adjoint to $g_{V!}$, $g'_{V!}$
([prop-exc-open-adjoint]). Passing to right adjoints relative to the
bounded-below objects of étale origin as above gives
$Lg_V'^*\circ Rf^{\times}\cong Rf_V^{\times}\circ Lg_V^*$ on bounded-below
objects of étale origin, in particular on the bounded constructible
complexes $K\in D_c^{[a,b]}(Y,A)$; no base-change theorem and no ambient
datum is used. Applying Step 2 to the
separated finite-type morphism $f_V$ over the affine scheme $V$
therefore bounds $Lg_V'^*(Rf^{\times}K)\cong Rf_V^{\times}(Lg_V^*K)$ on
$f^{-1}(V)$, hence on each chart $U\subseteq f^{-1}(V)$.
Step 4: conclusion. Vanishing of a cohomology sheaf, and vanishing of the
cohomology of a complex tensored with a coefficient sheaf, are local on the
site, and the charts $U$ cover $X$; hence the chartwise bounds of
Steps 2–3 give the two displayed assertions for the global object
$Rf^{\times}K$.
