+++
kind = "proof"
of = "sk-lem-tf-curve-supported-pairing"
uses = ["sk-d-trace-class", "sk-thm-sf-kunneth-verdier"]
+++
By external duality, $a^!P$ identifies with
$R\mathcal Hom((\Phi_X^m)^*K,K)$, so exceptional adjunction identifies $v$
with $[v]$. The supported restriction is constructed from the
two canonical arrows

$$
 Ra_*a^!P\longrightarrow P\longrightarrow Rb_*b^*P.
$$

After restriction to $b$, its source is supported on
$a\cap b=\{y\}$, so the resulting map factors through
$R\Gamma_y(b,b^*P)$. Equivalently it is the ordinary pullback
of the support object, followed by the exchange morphism to local
cohomology with support in the intersection.

The adjoint of $\mathrm{ev}_K:b^*P\to\omega_X$ is the map
$P\to Rb_*\omega_X$ used to define the trace in
[sk-thm-sf-kunneth-verdier]. Thus both descriptions of the
displayed composite are adjoint to the same map

$$
 Ra_*a^!P\longrightarrow P\longrightarrow Rb_*\omega_X.
$$

Exceptional proper base change for $b$ identifies its supported
adjoint with the defining trace map $a^!P\to Ri_*\omega_y$, and the
triangle identities of the ordinary and exceptional adjunctions prove
equality, including the evaluation normalization and Koszul
symmetry.

All these constructions may first be carried out on the
constructible étale models; restriction to the strict localization
is the filtered limit over étale neighbourhoods. The comparison
theorems identify inverse images, exceptional adjunctions, duality
and the support maps, and hence identify the resulting class with
the proétale local term of [sk-d-trace-class].
