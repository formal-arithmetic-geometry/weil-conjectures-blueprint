+++
kind  = "proof"
of    = "sk-lem-integral-models"
+++
(1) and (2). The map from the constant sheaf $\cO_E$ to $\cO_{E,X}$ is flat and induces
isomorphisms modulo every $\pi_E^n$ (\stacks{099L}). Hence restriction of scalars is an
equivalence on derived complete objects, by \stacks{099I}; this is (1)
([det-prop-integral-criterion-constant-coefficients]). By \stacks{09C1}, an object of
$\Dc(X,\cO_E)$ is a derived complete complex whose reduction modulo $\pi_E$ is constructible of
finite Tor dimension over $\cO_E/\pi_E$. Since $\cO_E/\pi_E$ is a field, every bounded complex
has finite Tor dimension over it, so this is the description of $\Dbc(X,\cO_E)$ in
[sk-prop-integral-criterion]; together with (1) this gives (2). Details:
[det-lem-integral-models-stacks].

(3) By [sk-prop-integral-criterion], an object of $D(X_{\mathrm{proét}},\cO_E)$ lies in
$\Dbc(X,\cO_E)$ if and only if it is derived complete with constructible reduction modulo
$\pi_E$ (condition (2)), and if and only if it admits a finite stratification such that on each
stratum $S$, pro-étale locally, $K|_S\simeq\cO_{E,S}\otimes_{\cO_E}P^\bullet$ for a bounded
complex $P^\bullet$ of finite free $\cO_E$-modules (condition (3)). The implication from (2) to
(3) is [sk-prop-integral-local-structure]. For each of the three operations we check one of
these two conditions.

*Inverse image.* By [sk-prop-sfb-cartesian-coefficients], $f^*$ sends finite free
$\cO_{E,Y}$-modules to finite free $\cO_{E,X}$-modules, so the local description is preserved.

*Extension by zero.* The functor $a_!=i_*u_!$ preserves derived completeness: $u_!$ for a
quasi-compact open immersion $u$ preserves limits by \stacks{09BP}, and $i_*$ is exact and
preserves limits by \stacks{09AA} and \stacks{09BM}. Both functors commute with reduction
modulo $\pi_E$ and preserve constructibility of the reductions.

*Tensor product.* Let $K,M\in\Dbc(X,\cO_E)$, and choose a stratification for $K$ as above.
Derived completeness and constructibility of the reduction modulo $\pi_E$ are both preserved
by cones, so $\Dbc(X,\cO_E)$ is closed under cones. The localization triangles along the
strata exhibit $K$ as a finite iterated extension of the objects $a_!a^*K$, for the strata
$a\colon S\hookrightarrow X$, and $-\otimes^{\mathbf L}M$ preserves these triangles. Hence it
suffices to show that $(a_!a^*K)\otimes^{\mathbf L}M$ lies in $\Dbc(X,\cO_E)$. For this we use
the projection formula for a locally closed immersion: for $L\in D(S_{\mathrm{proét}},\cO_E)$
and $M\in D(X_{\mathrm{proét}},\cO_E)$ the canonical map
$$
(a_!L)\otimes^{\mathbf L}M\longrightarrow a_!(L\otimes^{\mathbf L}a^*M)
$$
is an isomorphism. To see this, write $a=i\circ u$ with $u$ open and $i$ closed, so that
$a_!=i_*u_!$. On $S$ the map restricts to the identity of $L\otimes^{\mathbf L}a^*M$, and on
every complementary stratum both sides restrict to zero. Restriction to the strata is exact,
and these restrictions are jointly conservative by \stacks{09AD}. By the parts on inverse image
and extension by zero, it therefore remains to see that $a^*K\otimes^{\mathbf L}a^*M$ lies in
$\Dbc(S,\cO_E)$. Since $a^*K$ is pro-étale locally a bounded complex of finite free modules,
tensoring with it preserves derived completeness. The reduction modulo $\pi_E$ of the tensor
product is the tensor product of the reductions, which is constructible. Details:
[det-lem-integral-models-operations]; compare the preservation statements of
[sk-def-sfb-dc-restricted-functors].

(4) For $\Qlb$, first descend to a finite $E$ by [sk-thm-sfb-qlbar-two-colimit]. By
[sk-cor-coefficient-heart-ii], every object of $\Dbc(X,E)$ is obtained by finitely many cones
and shifts from sheaves $a_!L$ with $L$ lisse. By [sk-lem-stratified-lattice], after refining
the stratum $S$ by a finite stratification (which replaces $a_!L$ by finitely many extensions
of such sheaves), $L$ contains a lattice $L_0$ with $L_0[1/\ell]=L$, so
$a_!L=(a_!L_0)[1/\ell]$. The reduction of $L_0$ modulo $\pi_E^n$ is a locally constant sheaf of
finitely presented $\cO_E/\pi_E^n$-modules, so it comes from the étale site by \stacks{099Y}.
Hence $L_0\in\Dbc(S,\cO_E)$, so $a_!L_0\in\Dbc(X,\cO_E)$ by (3), and its reductions are
classical. Details: [det-lem-integral-models-generators].
