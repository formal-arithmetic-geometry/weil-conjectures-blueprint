+++
id = "lem-sc-finite-duality"
kind = "lemma"
title = "Duality along a finite flat morphism of smooth curves"
lean = ["AlgebraicGeometry.Scheme.exists_isIso_pushforwardHomObjComparison", "AlgebraicGeometry.Scheme.nonempty_homObj_pushforward_iso_pushforward_homObj", "AlgebraicGeometry.Scheme.nonempty_homObj_pushforward_iso", "AlgebraicGeometry.Scheme.exists_isIso_pushforwardHomObjComparison_unit"]
order = 703
uses = ["def-sc-curves", "def-sc-invertible-module", "def-sc-kahler-differentials", "lem-sc-invertible-dual", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be an algebraically closed field, $C$ a smooth
connected curve over $k$, $f:C\to\mathbf P^1_k$
a finite flat morphism of smooth $k$-curves which is *separable*: the
function field extension $k(C)\supseteq k(t)$ is separable, equivalently
$f$ is unramified (étale) at the generic point of $C$. Let $\mathcal M$ be a
finite locally free $\mathcal O_C$-module (a quasi-coherent module which
is Zariski-locally isomorphic to $\mathcal O_C^{\oplus r}$ for some
$r\ge0$), with dual
$\mathcal M^{\vee}:=\mathcal H om_{\mathcal O_C}(\mathcal M,\mathcal O_C)$.
Then there is a canonical isomorphism

$$
\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}\bigl(f_*\mathcal M,\;
\omega_{\mathbf P^1}\bigr)\;\cong\;
H^0\bigl(C,\;\omega_C\otimes\mathcal M^{\vee}\bigr);
$$

in particular, for an invertible $\mathcal M$
([def-sc-invertible-module]) the right hand side is
$H^0(C,\omega_C\otimes\mathcal M^{-1})$. Here $\omega_{\mathbf P^1}:=\Omega^1_{\mathbf P^1_k/k}$ and
$\omega_C:=\Omega^1_{C/k}$
([def-sc-kahler-differentials]).

*Why separability is assumed.* The canonical isomorphism is induced by the
trace of differentials $f_*\omega_C\to\omega_{\mathbf P^1}$; at the generic
point it is $\operatorname{Tr}_{k(C)/k(t)}\otimes\mathrm{id}$ on
$\Omega^1_{k(C)/k}=k(C)\otimes_{k(t)}\Omega^1_{k(t)/k}$, an identification that
needs separability. If $k(C)/k(t)$ is inseparable the trace of differentials
vanishes (as does $\operatorname{Tr}_{k(C)/k(t)}$), and the construction of the proof gives no
isomorphism; for example the Frobenius $F:\mathbf P^1_k\to\mathbf P^1_k$,
$t\mapsto t^p$, is finite flat but not separable. Downstream uses choose a
separable $f$.
