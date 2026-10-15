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

(3) By \stacks{09C2} and \stacks{09C7}, every $K\in\Dbc(X,\cO_E)$ is bounded, and on each stratum
of a finite stratification it is pro-étale locally a bounded complex of finite free
$\cO_{E,X}$-modules.

*Inverse image.* By [sk-prop-sfb-cartesian-coefficients], $f^*$ sends finite free
$\cO_{E,Y}$-modules to finite free $\cO_{E,X}$-modules, so the local description is preserved.

*Tensor product.* Tensoring with a complex that is locally a bounded complex of finite free
modules preserves derived completeness, and its reduction modulo $\pi_E$ is the tensor product
of the reductions, which is constructible. To globalize, use the finite open–closed
dévissage along the strata, and the identity
$$
(a_!L)\otimes^{\mathbf L}M\simeq a_!(L\otimes^{\mathbf L}a^*M)
$$
in $D(X_{\mathrm{proét}},\cO_E)$, for a locally closed immersion $a$ and
$L\in D(S_{\mathrm{proét}},\cO_E)$, $M\in D(X_{\mathrm{proét}},\cO_E)$. To prove it, compare
restrictions: on the stratum both sides restrict to $L\otimes^{\mathbf L}a^*M$, and on the
complementary strata both restrict to $0$, by the exactness of open and closed restriction.
These restrictions are jointly conservative by \stacks{09AD}.

*Extension by zero.* The functor $a_!=i_*u_!$ preserves derived completeness: $u_!$ for a
quasi-compact open immersion $u$ preserves limits by \stacks{09BP}, and $i_*$ is exact and
preserves limits by \stacks{09AA} and \stacks{09BM}. Both functors commute with reduction
modulo $\pi_E$ and preserve constructibility of the reductions. Details:
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
