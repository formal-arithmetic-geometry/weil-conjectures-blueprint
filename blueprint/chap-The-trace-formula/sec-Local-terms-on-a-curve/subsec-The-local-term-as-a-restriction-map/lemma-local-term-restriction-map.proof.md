+++
kind = "proof"
of = "lemma-local-term-restriction-map"
order = 967
uses = ["definition-trace-morphism"]
+++
We show that the local term and the displayed composite are both
adjoint to one map $R\gamma_*\gamma^!P\to R\delta_*\omega_X$. Once the class
$[\psi]$ and the map $\rho$ are built, the comparison is formal, and
computing on étale models changes nothing.

By external duality, $\gamma^!P$ is identified with
$\cHom((\Phi_X^m)^*K,K)$, so exceptional adjunction identifies $\psi$
with $[\psi]$. The map $\rho$ is constructed from the
two canonical arrows

$$
R\gamma_*\gamma^!P\longrightarrow P\longrightarrow R\delta_*\delta^*P.
$$

After restriction to $\Delta$, the source is supported on
$\Gamma\cap\Delta$. By Lemma [lemma-frobenius-fixed-scheme] the scheme
$\Gamma\cap\Delta$ is reduced, and on $T$ it is the single point
$(y,y)$. Hence the resulting map factors through
$R\Gamma_y(\Delta,\delta^*P)$. Equivalently, it is the ordinary pullback
of the object with supports, followed by the base change map to local
cohomology with support in the intersection.

The adjoint of $\mathrm{ev}_K:\delta^*P\to\omega_X$ is the map
$P\to R\delta_*\omega_X$ used to define the trace morphism in
Definition [definition-trace-morphism]. Hence the displayed composite, before
$\int_y$, is adjoint to the map

$$
R\gamma_*\gamma^!P\longrightarrow P\longrightarrow R\delta_*\omega_X.
$$

The local term is built from the same map. Indeed, by exceptional proper base change
for $\delta$, the adjoint of this map, which is supported on $y$, is the trace
map $\gamma^!P\to Ri_*\omega_y$ of Definition [definition-trace-class-local-terms]. The triangle
identities of the ordinary and exceptional adjunctions then show that the
two constructions give the same element of $A$.

The constructions above also make sense on the constructible étale
models, where restriction to the strict localization is the filtered
limit over étale neighbourhoods. The comparison theorems identify
inverse images, exceptional adjunctions, duality and the support maps
on the two sites, and hence they identify the class obtained on the
étale models with the pro-étale local term of
Definition [definition-trace-class-local-terms].
