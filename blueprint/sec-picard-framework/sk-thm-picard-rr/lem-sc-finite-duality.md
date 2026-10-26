+++
id = "lem-sc-finite-duality"
kind = "lemma"
title = "Duality along a finite flat morphism of smooth curves"
lean = ["AlgebraicGeometry.Scheme.exists_isIso_pushforwardHomObjComparison", "AlgebraicGeometry.Scheme.nonempty_homObj_pushforward_iso_pushforward_homObj", "AlgebraicGeometry.Scheme.nonempty_homObj_pushforward_iso", "AlgebraicGeometry.Scheme.exists_isIso_pushforwardHomObjComparison_unit"]
order = 666
uses = ["def-sc-curves", "def-sc-invertible-module", "def-sc-kahler-differentials", "lem-pc-tensor-dual-invertible", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field, $C$ a scheme over $k$ which is smooth of
relative dimension $1$, and $f:C\to\mathbf P^1_k$
a finite flat morphism of $k$-schemes which is *generically
separable*: at every generic point $\xi$ of $C$ the field extension
$\kappa(\xi)\supseteq\kappa(f(\xi))=k(t)$ is separable (equivalently,
$\mathcal O_{\mathbf P^1,f(\xi)}\to\mathcal O_{C,\xi}$ is unramified).
For a finite locally free $\mathcal O_C$-module $\mathcal M$ (a
quasi-coherent module which is Zariski-locally isomorphic to
$\mathcal O_C^{\oplus r}$ for some $r\ge0$) write
$\mathcal M^{\vee}:=\mathcal H om_{\mathcal O_C}(\mathcal M,\mathcal O_C)$.
Then there is a trace map
$\tau:f_*\omega_C\to\omega_{\mathbf P^1}$ such that
$\varphi\mapsto\tau\circ f_*\varphi$ is an isomorphism of
$\mathcal O_{\mathbf P^1}$-modules
$f_*\mathcal H om_{\mathcal O_C}(\mathcal M,\omega_C)\cong
\mathcal H om_{\mathcal O_{\mathbf P^1}}(f_*\mathcal M,\omega_{\mathbf P^1})$
for every such $\mathcal M$, and on global sections an isomorphism,
natural in $\mathcal M$,

$$
\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}\bigl(f_*\mathcal M,\;
\omega_{\mathbf P^1}\bigr)\;\cong\;
H^0\bigl(C,\;\omega_C\otimes\mathcal M^{\vee}\bigr);
$$

in particular, for an invertible $\mathcal M$
([def-sc-invertible-module]) the right hand side is
$H^0(C,\omega_C\otimes\mathcal M^{-1})$. Here $\omega_{\mathbf P^1}:=\Omega^1_{\mathbf P^1_k/k}$ and
$\omega_C:=\Omega^1_{C/k}$
([def-sc-kahler-differentials]). The separability hypothesis cannot be
dropped: for an inseparable $f$ the trace of differentials vanishes.
