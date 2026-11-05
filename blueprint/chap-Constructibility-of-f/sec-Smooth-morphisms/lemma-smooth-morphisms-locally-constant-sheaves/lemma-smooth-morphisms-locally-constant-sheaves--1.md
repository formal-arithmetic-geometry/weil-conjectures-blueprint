+++
id = "lemma-smooth-morphisms-locally-constant-sheaves--1"
kind = "lemma"
title = "Compact dual presentation of a smooth direct image"
name_showing = false
order = 564001
aliases = ["bp-r170-1"]
lean = ["AlgebraicGeometry.Etale.exists_smooth_compact_dual_model"]
uses = ["definition-constructible-sheaves", "definition-derived-base-change-map"]
+++
The pro-étale repetition of the preceding lemma is bypassed by the Lean
route; the intermediate statement used there is the following étale
compact dual presentation.

Let $k$ be any field, let $\ell$ be a prime different from its
characteristic, and let $S$ be any scheme of finite type over $k$.
Let $f:X\to S$ be separated, smooth and of finite type, and let $L$ be a
finite locally constant $\Fell$-sheaf on $X_{\acute{e}t}$, regarded as a
complex in degree zero. There is a complex $C\in\Dbc(S,\Fell)$ with
the following properties. Write
$D_Y(M)=\cHom_Y(M,\Fell_Y)$ for the coefficient dual.

For every open immersion $j:U\hookrightarrow S$ and every cartesian
square with projections $p:X_U\to X$ and $f_U:X_U\to U$, put
$C_U=j^*C$ and $L_U=p^*L$. There is an isomorphism

$$
\delta_U:Rf_{U,*}L_U\xrightarrow{\sim}D_U(C_U).
$$

For every Noetherian scheme $T$ and morphism $v:T\to U$, and every
cartesian square with projections $v_X:X_T\to X_U$ and $f_T:X_T\to T$,
there is an isomorphism

$$
\delta_T:Rf_{T,*}v_X^*L_U\xrightarrow{\sim}D_T(v^*C_U).
$$

These isomorphisms identify the canonical ordinary base change map
$b_{v,L_U}:v^*Rf_{U,*}L_U\to Rf_{T,*}v_X^*L_U$ with the canonical
pullback map for the coefficient dual: if
$\gamma_{v,C_U}:v^*D_U(C_U)\to D_T(v^*C_U)$ is the transpose of
pulled-back evaluation, then

$$
\delta_T\circ b_{v,L_U}
=\gamma_{v,C_U}\circ v^*\delta_U.
$$

No integrality of $S$ or shrinking of the base is required for this
presentation; invertibility of $\gamma_{v,C_U}$ is not asserted here.
