+++
kind = "proof"
of = "sk-lem-tf-curve-supported-pairing"
uses = ["sk-d-trace-class", "sk-thm-sf-kunneth-verdier"]
+++
We show that the local term and the displayed composite are both
adjoint to one map $R\gamma_*\gamma^!P\to R\delta_*\omega_X$.
By external duality, $\gamma^!P$ is identified with
$\cHom((\Phi_X^m)^*K,K)$, so exceptional adjunction identifies $\psi$
with $[\psi]$. The map $\rho$ is constructed from the
two canonical arrows

$$
R\gamma_*\gamma^!P\longrightarrow P\longrightarrow R\delta_*\delta^*P.
$$

After restriction to $\Delta$, the source is supported on
$\Gamma\cap\Delta=\{(y,y)\}$, so the resulting map factors through
$R\Gamma_y(\Delta,\delta^*P)$. Equivalently, it is the ordinary pullback
of the object with supports, followed by the base change map to local
cohomology with support in the intersection.

The adjoint of $\mathrm{ev}_K:\delta^*P\to\omega_X$ is the map
$P\to R\delta_*\omega_X$ used to define the trace in
Lemma [sk-thm-sf-kunneth-verdier]. Hence the displayed composite, before
$\int_y$, is adjoint to the map

$$
R\gamma_*\gamma^!P\longrightarrow P\longrightarrow R\delta_*\omega_X.
$$

The local term is built from the same map: exceptional proper base change
for $\delta$ identifies its adjoint, which is supported on $y$, with the trace
map $\gamma^!P\to Ri_*\omega_y$ of Definition [sk-d-trace-class]. The triangle
identities of the ordinary and exceptional adjunctions then show that the
two constructions give the same element of $A$.

The constructions above also make sense on the constructible étale
models, where restriction to the strict localization is the filtered
limit over étale neighbourhoods. The comparison theorems identify
inverse images, exceptional adjunctions, duality and the support maps
on the two sites, and hence they identify the class obtained on the
étale models with the pro-étale local term of
Definition [sk-d-trace-class].
